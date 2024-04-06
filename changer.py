#TODO TO DELETE
#TOOOOOOOOOMEEEEEKKKK
# Możliwe, że potrzebujesz dwóch kopii archiwów .zip
# Nie wiem po co i na co, ale w poprzedniej wersji miałeś w main.py usuwanie document_name.zip oraz temp.zip
# Zatem były 2 .zip -y, coś w tym może być
#Chodzi o linijkę 93, 96 stąd: https://github.com/turek9933/DOCX-App/blob/Sciezki_bezposrednie_zamiast_nazw_txt_docx/main.py#L93

import sys
import fileinput
from time import sleep
import os
import xml

#TODO dotegować wyjątki/błąd jak w pliku '???'

#TODO TO DELETE
#Ogarnąć separatory customowe

line_sep = ";;;"

def lets_search(xml_good, xml_bad, word_to_find, word_to_put):    
    #Otwieramy plik .xml do przeszukania (xml_bad) i szukamy kolejnych luk do zastąpienia
    with fileinput.FileInput(files=(os.path.join(to_save_docx_path, "temp", "word", xml_bad))) as f_xml_read:
        #Otwieramy plik .xml w folderze do nadpisania go nowymi danymi 
        with open(os.path.join(to_save_docx_path, "temp", "word", xml_good), 'w') as f_xml_write:
            #Przechodimy przez linie pliku (xml_bad), szukając kolejnych słów do zastąpienia je kolejnymi danymi
            #Tak zastąpionymi liniami nadpisujemy plik w folderze tymczasowym 
            for line in f_xml_read:
                temp_line = str(line)
                #print(school_data_splited)#TODO
                while temp_line.find(word_to_find) != -1:
                    temp_line = temp_line.replace(word_to_find, word_to_put)
                f_xml_write.write(temp_line)

def change_files_names(file_a, file_b):
    os.rename(os.path.join(to_save_docx_path, "temp", "word", file_a),
              os.path.join(to_save_docx_path, "temp", "word", file_a.replace(".xml", "_temp.xml")))

    os.rename(os.path.join(to_save_docx_path, "temp", "word", file_b),
              os.path.join(to_save_docx_path, "temp", "word", file_a))

    os.rename(os.path.join(to_save_docx_path, "temp", "word", file_a.replace(".xml", "_temp.xml")),
              os.path.join(to_save_docx_path, "temp", "word", file_b))
def delete_white_symbol(line):
    if line[-1].isspace():
        return line[:-1]
    else:
        return line

#is_ok - bool, prawdziwy, jeśli faktycznie plik o nazwie xml_good, jest tym z ostatnio zapisanymi poprawniejszymi danymi

#Argumenty po kolei: docx_file_path; txt_file_path; to_save_docx_path; xml_good; xml_bad
if len(sys.argv) == 6:
    docx_file_path = sys.argv[1]
    txt_file_path = sys.argv[2]
    to_save_docx_path = sys.argv[3]
    xml_good = sys.argv[4]
    xml_bad = sys.argv[5]
    is_ok = True

    with fileinput.input(files = (txt_file_path)) as f_data:
        for data_line in f_data:
            data_line_splited = data_line.split(line_sep)
            if len(data_line_splited) == 2:
                if is_ok:
                    lets_search(xml_good, xml_bad, delete_white_symbol(data_line_splited[0]), delete_white_symbol(data_line_splited[1]))
                else:
                    lets_search(xml_bad, xml_good, delete_white_symbol(data_line_splited[0]), delete_white_symbol(data_line_splited[1]))
                is_ok = not is_ok                
            else:
                sys.exit("Wrong school data (It was: " + str(data_line_splited) + ' there are ' + str(len(data_line_splited)) + ' arguments')
        if is_ok:
            change_files_names(xml_bad, xml_good)
else:
    sys.exit('Wrong number of arguments!!!')