#Tomasz Bonifacy Turek
#01.02.2023
#v1.0

import os
import shutil
from pathlib import Path
import zipfile
import fileinput
from time import sleep

#Definicja kolejnych funkcji

#Funkcja zwraca name z końcówką .docx
def check_docx(name):
    temp = name
    if temp.find('.docx') == -1:
        temp += '.docx'
    return temp
#Funkcja zwraca name z końcówką .txt
def check_txt(name):
    temp = name
    if temp.find('.txt') == -1:
        temp += '.txt'
    return temp
#Funkcja zwraca znak systemu plików, tzn. "\" lub "/"
def check_sys(cwd):
    temp = str(cwd)
    if temp.find('\\') != -1:
        return '\\'
    elif temp.find('/') != -1:
        return '/'
#Funkcja zwraca 10 znakowy wyraz składający się z jednakowej, danej cyfry
def digit_word(n):
    i = 0
    ret = ""
    while i < 10:
        ret += chr(n)
        i += 1
    return ret
#Funkcja zwraca ilość linii z pliku w miejscu f_dir_and_name
def how_much_numbers_file(f_dir_and_name):
    with open(f_dir_and_name) as f:
        for i, _ in enumerate(f):
            pass
        return i + 1
#Funkcja wyświetla postęp obecnego procesu (ilosciowo, procentowo, graficznie)
def show_process(current, all):
    current_precent = current * 100 / all
    print(f"{current} z {all}")
    print(f"{current_precent}%")
    i = 0
    while i < current_precent:
        print('.', end = "")
        i += 1
    print("")
#Funkcja tworzy folder o danej sciezce, o ile jeszcze nie istnieje
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path) 

#Pobranie katalogu, nazwy certyfikatu, nazwy pliku z danymi i ustalenie ilości danych
cwd = os.path.dirname(__file__)
sys_id = check_sys(cwd)
print("Twoj folder to:")
print(cwd)
certificate_name = input("Podaj nazwę pliku .docx: ")
certificate_name = check_docx(certificate_name)
data_name = input("Podaj nazwę pliku z danymi .txt: ")
data_name = check_txt(data_name)
data_lines_count = how_much_numbers_file(cwd + sys_id + data_name)

#Tworzymy folder, gdzie zapiszemy wszytkie nowe programy
create_dir(cwd + sys_id + data_name.replace(".txt", ""))

#Uśpienie na chwilkę programu i wyczyszczenie ekrany
sleep(1)
os.system('cls')

#Przepakowanie z .docx do .zip i kopia document.xml
shutil.copy(cwd + sys_id + certificate_name, cwd + sys_id + "temp.zip")
with zipfile.ZipFile(cwd + sys_id + "temp.zip") as zip_var:
    zip_var.extractall(path = cwd + sys_id + "temp")    

#Kopiowanie orginalnego document.xml w celu jego przeszukiwania i zastępowania
shutil.copy(cwd + sys_id + "temp" + sys_id + "word" + sys_id + "document.xml", cwd + sys_id + "document_original.xml")

#Klucz całego programu:
#Bierzemy plik z danymi (data_name) i działamy z kolejnymi członami w liniach (oddzielonymi tabulatorem).
#Bierzemy plik document_original.xml (tzn. kopię) i analizujemy.
#Szukamy kolejnych zaznaczonych tam luk (zaznaczonych poprzez 10 cyfrowy wyraz złożony z samych 0, 1, itd.)
#Znalezione luki zastępujemy kolejnymi członami z pliku z danymi (data_name)

#Otwarcie pliku z danymi (dana_name)
with fileinput.input(files = (cwd + sys_id + data_name)) as f_data:
    #Zapisujemy też numer linii, na której działamy
    line_count = 0
    #Idziemy po każdej lini z pliku, będziemy zamieniać wyrazy i tworzyć nowe pliki .docx
    for data_line in f_data:
        #Dzielimy każdą linię na człony rozielone tabulatorem (domyślny podział Excela)
        data_line_splited = data_line.split(chr(9))
        #Zapamiętujemy pierwszy człon, gdyż posłuży on jako nazwa nowego pliku .docx
        new_docx_name = data_line_splited[0]
        #Pilnujemy również indeksów członów linii
        index = 0

        #Otwieramy orginalny plik .xml (document_original.xml) i szukamy kolejnych luk do zastąpienia
        with fileinput.FileInput(files=(cwd + sys_id + "document_original.xml")) as f_docx_read:
            #Otwieramy plik .xml w folderze do nadpisania go nowymi danymi 
            with open(cwd + sys_id + "temp" + sys_id + "word" + sys_id + "document.xml", 'w') as f_docx_write:
                #Przechodimy przez linie pliku orginalnego (document_original.xml), szukając kolejnych luk (10 cyfr), zastępując je kolejnymi danymi (data_line_splited[index])
                #Tak zastąpionymi liniami nadpisujemy plik w folderze tymczasowym 
                for line in f_docx_read:
                    temp_line = str(line)
                    char_code_numer = 48
                    while temp_line.find(digit_word(char_code_numer)) != -1 and index < len(data_line_splited):
                        temp_line = temp_line.replace(digit_word(char_code_numer), data_line_splited[index])
                        char_code_numer += 1
                        index += 1
                    f_docx_write.write(temp_line)
        
        #Wyswietlamy obecny proces przez chwilę
        os.system('cls')
        show_process(line_count + 1, data_lines_count)
        #sleep(1) TO DO
        #Iterujemy ilość linii, które przeszliśmy
        line_count += 1

        #Zwijamy plik tymczasowy (temp) do archiwum .zip z nową nazwą (new_docx_name)
        shutil.make_archive(cwd + sys_id + new_docx_name, 'zip', cwd + sys_id + "temp")
        #Kopiujemy nowe archiwum .zip do folderu, gdzie gromadzimy wszystkie zastąpione pliki (data_name) oraz zmieniamy format archiwum z .zip na .docx
        shutil.copy(cwd + sys_id + new_docx_name + ".zip", cwd + sys_id + data_name.replace(".txt", "") + sys_id + new_docx_name + ".docx")
        #Usuwamy zbędne już archiwum .zip
        os.remove(cwd + sys_id + new_docx_name + ".zip")

#Usunięcie wypakowanego orginalego pliku .xml (document_original.xml), całego wypakowanego folderu tymczasowego (temp/*) oraz archiwum tymczasowego (temp.zip)
os.remove(cwd + sys_id + "document_original.xml")
shutil.rmtree(cwd + sys_id + "temp")
os.remove(cwd + sys_id + "temp.zip")

#Komunikat końcowy
os.system('cls')
print("Gotowe, wszystkie pliki znajdują się w folderze: " + data_name.replace(".txt", ""))
sleep(3)