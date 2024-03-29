#Tomasz Bonifacy Turek
#31.08.2023
#v1.0
#Ważne!!! Używam wyłącznie ' - pojedyńczego, NIE podwójnego.
#Podwójny występuje wyłącznie w plikach, na których operuje program. 

import os
import shutil
from pathlib import Path
import zipfile
import fileinput
from time import sleep

#Definicja kolejnych funkcji

#Funkcja zwraca name z końcówką .txt
def check_txt(name):
    temp = name
    if temp.find('.txt') == -1:
        temp += '.txt'
    return temp
#Funkcja zwraca znak systemu plików, tzn. '\' lub '/'
def check_sys(cwd):
    temp = str(cwd)
    if temp.find('\\') != -1:
        return '\\'
    elif temp.find('/') != -1:
        return '/'
#Funkcja tworzy folder o danej sciezce, o ile jeszcze nie istnieje
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path) 
#Funkcja usuwa znak nowej linii z końca ciągu znaków
def delete_newline(word):
    if word.find('\n') != -1:
        return str(word.replace('\n', ''))
    else:
        return str(word)

###########
#Lista najważniejszych zmiennych
#cwd - current working direction - string, ścieżka do programu
#sys_id - string, '\' lub '/'
#school_folder_name - string, nazwa folderu, gdzie są zapisane pliki.txt z listą dokumentów do zrobienia oraz danymi do wpisania
#f_docx_list - plik, odczyt, lista dokumentów do uzupełnienia
#xml_good - string, nazwa pliku xml, z zastępionymi lukami (najlepsza wersja w danej chwili)
#xml_bad - string, nazwa pomocniczego pliku xml, do usunięcia 
###########

#Pobranie katalogu
cwd = os.path.dirname(__file__)
sys_id = check_sys(cwd)
print('Twoj folder to:')
print(cwd)

#Pobranie nazwy folderu z danymi i stworzenie podfolderu 
school_folder_name = input('Podaj nazwę folderu z danymi szkoły oraz listą dokumentów do wyczarowania: ')
if not os.path.exists(cwd + sys_id + school_folder_name + sys_id + school_folder_name):
    os.mkdir(cwd + sys_id + school_folder_name + sys_id + school_folder_name)

#Otwieramy listę z dokumentami do wyczarowania
with fileinput.input(files = (cwd + sys_id + school_folder_name + sys_id + 'scheme_docx_list.txt')) as f_docx_list:
    #Będzimy kopiować i edytować dokumenty według kolejnych nazw zapisanch w pliku
    for document_name in f_docx_list:
        document_name = delete_newline(document_name)
        print(document_name)
        #Przepakowywanie kolejnych plików z .docx do .zip i kopia document.xml
        shutil.copy(cwd + sys_id + 'documents' + sys_id + document_name + '.docx', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp.zip')
        with zipfile.ZipFile(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp.zip') as zip_var:
            zip_var.extractall(path = cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp')
        
        #Kopiowanie orginalnego document.xml w celu jego przeszukiwania i zastępowania
        #Oba pliki mają też zmienioną nazwę, ponieważ
        #szukamy luk w jednym pliku, zastępujemy, zapisujemy do drugiego
        #Później szukamy luk w drugim i zapisujemy do pierwszego.
        #Szukając ciągle w jednym nadpisywalibyśmy tekstem, który nie miałby zastąpionych poprzednich luk
        xml_good = 'document'
        xml_bad = 'document_1'
        shutil.copy(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + 'document.xml', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + xml_bad + '.xml')
        os.rename(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + 'document.xml',cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + xml_good + '.xml')
        
        #Argumenty po kolei: cwd; sys_id; school_folder_name
        os.system('python3 ' + cwd + sys_id + 'changer.py ' + cwd + ' ' + sys_id + ' ' + school_folder_name + ' ' + xml_good + ' ' + xml_bad)
        
        #Usunięcie zbędnego pliku xml
        os.remove(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + xml_bad + '.xml')

        #Zwijamy plik tymczasowy (temp) do archiwum .zip z nową nazwą (new_docx_name)
        shutil.make_archive(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + document_name, 'zip', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp')
        #Kopiujemy nowe archiwum .zip i zmieniamy format archiwum z .zip na .docx
        shutil.copy(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + document_name + '.zip', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + document_name + '.docx')
        #Usuwamy zbędne już archiwum .zip
        os.remove(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + document_name + '.zip')
        #Usunięcie całego wypakowanego folderu tymczasowego (temp/*) oraz archiwum tymczasowego (temp.zip)
        shutil.rmtree(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp')
        os.remove(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp.zip')

print('\nEnd, danke schón!')