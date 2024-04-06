#Tomasz Bonifacy Turek
#31.08.2023
#v1.0
#Ważne!!! Używam wyłącznie ' - pojedyńczego, NIE podwójnego.
#Podwójny występuje wyłącznie w plikach, na których operuje program. 

import sys
import os
import shutil
from pathlib import Path
import zipfile
import fileinput
from time import sleep
import subprocess

#Definicja kolejnych funkcji

#Funkcja zwraca name z końcówką .txt
def check_txt(name):
    temp = name
    if temp.find('.txt') == -1:
        temp += '.txt'
    return temp
#Funkcja zwraca znak systemu plików, tzn. '\' lub '/'
def check_sys():
    if os.name == "nt":
        return "\\"
    else:
        return "/"
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
#f_docx_list - plik, odczyt, lista dokumentów do uzupełnienia
#xml_good - string, nazwa pliku xml, z zastępionymi lukami (najlepsza wersja w danej chwili)
#xml_bad - string, nazwa pomocniczego pliku xml, do usunięcia 
###########

#Pobranie katalogu skryptu
cwd = os.path.dirname(__file__)
sys_id = check_sys()

#Pobranie ścieżek do pliku schematu .docx i pliku z danymi .txt
if len(sys.argv) < 3:
    print("Prawidlowa forma wywolania programu: skrypt.py <schemat.docx> <dane.txt>")
    sys.exit(1)
docx_file_path = os.path.join(sys.argv[1])
txt_file_path = os.path.join(sys.argv[2])
if os.name == "nt":
    docx_file_path = docx_file_path.replace("/", "\\")
    txt_file_path = txt_file_path.replace("/", "\\")

#Stworzenie folderu do zapisu nowych dokumentów .docx
to_save_docx_path = os.path.join(txt_file_path.replace(".txt", ""))
create_dir(to_save_docx_path)

#Będzimy kopiować i edytować dokumenty według kolejnych nazw zapisanch w pliku
#Przepakowywanie kolejnych plików z .docx do .zip i kopia document.xml
shutil.copy(docx_file_path, os.path.join(to_save_docx_path, docx_file_path[docx_file_path.rfind(sys_id) + 1:].replace(".docx", ".zip")))
with zipfile.ZipFile(os.path.join(to_save_docx_path, docx_file_path[docx_file_path.rfind(sys_id) + 1:].replace(".docx", ".zip"))) as zip_var:
    zip_var.extractall(path = os.path.join(to_save_docx_path, "temp"))


#Kopiowanie orginalnego document.xml w celu jego przeszukiwania i zastępowania
#Oba pliki mają też zmienioną nazwę, ponieważ
#szukamy luk w jednym pliku, zastępujemy, zapisujemy do drugiego
#Później szukamy luk w drugim i zapisujemy do pierwszego.
#Szukając ciągle w jednym nadpisywalibyśmy tekstem, który nie miałby zastąpionych poprzednich luk
xml_good = "document.xml"
xml_bad = "xml_bad_temp.xml"
shutil.copy(
    os.path.join(to_save_docx_path, "temp", "word", "document.xml"),
    os.path.join(to_save_docx_path, "temp", "word", xml_bad))
os.rename(
    os.path.join(to_save_docx_path, "temp", "word", "document.xml"),
    os.path.join(to_save_docx_path, "temp", "word", xml_good))

#TODO TO DELETE
#Argumenty po kolei: docx_file_path; txt_file_path; to_save_docx_path; xml_good; xml_bad
subprocess.run(["python", "changer.py", docx_file_path, txt_file_path, to_save_docx_path, xml_good, xml_bad], check=True)

input("Press Enter to continue...")
#os.system('python3 ' + cwd + sys_id + 'changer.py ' + cwd + ' ' + sys_id + ' ' + school_folder_name + ' ' + xml_good + ' ' + xml_bad)

#Usunięcie zbędnego pliku xml
os.remove(os.path.join(to_save_docx_path, "temp", "word", xml_bad))

#Zwijamy plik tymczasowy (temp) do archiwum .zip z nową nazwą (new_docx_name)
shutil.make_archive(
    os.path.join(to_save_docx_path, docx_file_path[docx_file_path.rfind(sys_id) + 1:].replace(".docx", "")),
    "zip",
    os.path.join(to_save_docx_path, "temp"))
#Kopiujemy nowe archiwum .zip i zmieniamy format archiwum z .zip na .docx
shutil.copy(os.path.join(to_save_docx_path, docx_file_path[docx_file_path.rfind(sys_id) + 1:].replace(".docx", ".zip")),
            os.path.join(to_save_docx_path, docx_file_path[docx_file_path.rfind(sys_id) + 1:]))
#Usuwamy zbędne już archiwum .zip
os.remove(os.path.join(to_save_docx_path, docx_file_path[docx_file_path.rfind(sys_id) + 1:].replace(".docx", ".zip")))
#Usunięcie całego wypakowanego folderu tymczasowego (temp/*) oraz archiwum tymczasowego (temp.zip)
shutil.rmtree(os.path.join(to_save_docx_path, "temp"))

#TODO TO DELETE Sprawdzić czy to w ogóle jest/było potrzebne!!!
#os.remove(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp.zip')

print('\nEnd, danke schón!')

print(docx_file_path)
print(docx_file_path[docx_file_path.rfind(sys_id) + 1:])
print(txt_file_path)
print(cwd)
print(sys_id)
print(to_save_docx_path)
sys.exit(1)