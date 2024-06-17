#Tomasz Bonifacy Turek
#01.02.2023
#v1.0

import os
import shutil
from pathlib import Path
import zipfile
import fileinput
import sys
import names

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
def check_sys():
    if os.name == "nt":
        return "\\"
    else:
        return "/"
#Funkcja zwraca 10 znakowy wyraz składający się z jednakowej, danej cyfry
def digit_word(n):
    i = 0
    ret = ""
    while i < names.get_placeholder_certificates_amount():
        ret += chr(n)
        i += 1
    return ret
#Funkcja zwraca ilość linii z pliku w miejscu f_dir_and_name
def how_much_numbers_file(f_dir_and_name):
    with open(f_dir_and_name, encoding = names.detect_encoding(f_dir_and_name)) as f:
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
# Funkcja sprzątająca użyte zasowby
def cleanup(temp_path, original_xml_path, temp_zip_path):
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    if os.path.exists(original_xml_path):
        os.remove(original_xml_path)
    if os.path.exists(temp_zip_path):
        os.remove(temp_zip_path)


if len(sys.argv) != 3:
    print("Prawidlowa forma wywolania programu: skrypt.py <schemat.docx> <dane.txt>")
    sys.exit(1)

certificate_name = os.path.join(sys.argv[1])
data_name = os.path.join(sys.argv[2])

data_line_separator = names.get_separator_certificates()

if os.name == "nt":
    certificate_name = certificate_name.replace("/", "\\")
    data_name = data_name.replace("/", "\\")

#Pobranie katalogu, nazwy certyfikatu, nazwy pliku z danymi i ustalenie ilości danych
cwd = os.path.dirname(__file__)
sys_id = check_sys()

# Nazwy ścieżek do plików tymczasowych
temp_zip_path = os.path.join(certificate_name.replace(".docx", "temp.zip"))
temp_dir = os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), "temp")
original_xml_path = os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), "document_original.xml")
output_dir = data_name.replace(".txt", "")

data_lines_count = how_much_numbers_file(data_name)

#Tworzymy folder, gdzie zapiszemy wszytkie nowe programy
create_dir(output_dir)

try:
    #Przepakowanie z .docx do .zip i kopia document.xml
    shutil.copy(certificate_name, temp_zip_path)

    #Wypakowanie z .zip do folderu o nazwie temp, który znajduje się w katalogu dokumentu .docx
    with zipfile.ZipFile(temp_zip_path) as zip_var:
        zip_var.extractall(temp_dir)

    #Kopiowanie orginalnego document.xml w celu jego przeszukiwania i zastępowania
    shutil.copy(os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), "temp", "word", "document.xml"),
            original_xml_path)

    #Klucz całego programu:
    #Bierzemy plik z danymi (data_name) i działamy z kolejnymi członami w liniach (oddzielonymi tabulatorem).
    #Bierzemy plik document_original.xml (tzn. kopię) i analizujemy.
    #Szukamy kolejnych zaznaczonych tam luk (zaznaczonych poprzez 10 cyfrowy wyraz złożony z samych 0, 1, itd.)
    #Znalezione luki zastępujemy kolejnymi członami z pliku z danymi (data_name)

    #Otwarcie pliku z danymi (dana_name)
    with fileinput.input(files = (data_name), encoding = names.detect_encoding(data_name)) as f_data:
        #Zapisujemy też numer linii, na której działamy
        line_count = 0
        #Idziemy po każdej lini z pliku, będziemy zamieniać wyrazy i tworzyć nowe pliki .docx
        for data_line in f_data:
            #Dzielimy każdą linię na człony rozielone tabulatorem (domyślny podział Excela)
            data_line_splited = data_line.split(data_line_separator)
            #Zapamiętujemy pierwszy człon, gdyż posłuży on jako nazwa nowego pliku .docx
            new_docx_name = data_line_splited[0]
            #Pilnujemy również indeksów członów linii
            index = 0

            #Otwieramy orginalny plik .xml (document_original.xml) i szukamy kolejnych luk do zastąpienia
            with fileinput.FileInput(original_xml_path, encoding = names.detect_encoding(original_xml_path)) as f_docx_read:
                #Otwieramy plik .xml w folderze do nadpisania go nowymi danymi 
                with open(os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), "temp", "word", "document.xml"), "w", encoding = 'utf-8') as f_docx_write:
                    #Przechodimy przez linie pliku orginalnego (document_original.xml), szukając kolejnych luk (10 cyfr), zastępując je kolejnymi danymi (data_line_splited[index])
                    #Tak zastąpionymi liniami nadpisujemy plik w folderze tymczasowym 
                    for line in f_docx_read:
                        temp_line = str(line)
                        char_code_numer = names.get_placeholder_certificates_code()
                        while temp_line.find(digit_word(char_code_numer)) != -1 and index < len(data_line_splited):
                            temp_line = temp_line.replace(digit_word(char_code_numer), data_line_splited[index])
                            char_code_numer += 1
                            index += 1
                        f_docx_write.write(temp_line)
            #Wyswietlamy obecny proces przez chwilę
            os.system('cls')
            show_process(line_count + 1, data_lines_count)
            #Iterujemy ilość linii, które przeszliśmy
            line_count += 1

            #Zwijamy plik tymczasowy (temp) do archiwum .zip z nową nazwą (new_docx_name)
            shutil.make_archive(os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), new_docx_name),
                                "zip", 
                                temp_dir)
            #Kopiujemy nowe archiwum .zip do folderu, gdzie gromadzimy wszystkie zastąpione pliki (data_name) oraz zmieniamy format archiwum z .zip na .docx
            shutil.copy(os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), new_docx_name + ".zip"),
                        os.path.join(output_dir, new_docx_name + ".docx"))
            #Usuwamy zbędne już archiwum .zip
            os.remove(os.path.join(certificate_name.replace(certificate_name[certificate_name.rfind(sys_id):], ""), new_docx_name + ".zip"))

# Sprzątanie na wypadek błędu
except Exception as e:
    cleanup(temp_dir, original_xml_path, temp_zip_path)
    sys.exit(e)

# Sprzątanie po zakończeniu programu
cleanup(temp_dir, original_xml_path, temp_zip_path)

#Komunikat końcowy
os.system('cls')
print("Gotowe, wszystkie pliki znajdują się w folderze: " + output_dir)