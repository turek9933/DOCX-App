from audioop import lin2adpcm
from curses.ascii import isspace
import sys
import fileinput
from time import sleep
import os

import xml

#TODO dotegować wyjątki/błąd jak w pliku '???'

#is_ok - bool, prawdziwy, jeśli faktycznie plik o nazwie xml_good, jest tym z ostatnio zapisanymi poprawniejszymi danymi

def lets_search(xml_good, xml_bad, word_to_find, word_to_put):    
    #Otwieramy plik .xml do przeszukania (xml_bad) i szukamy kolejnych luk do zastąpienia
    with fileinput.FileInput(files=(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + xml_bad + '.xml')) as f_xml_read:
        #Otwieramy plik .xml w folderze do nadpisania go nowymi danymi 
        with open(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + xml_good + '.xml', 'w') as f_xml_write:
            #Przechodimy przez linie pliku (xml_bad), szukając kolejnych słów do zastąpienia je kolejnymi danymi
            #Tak zastąpionymi liniami nadpisujemy plik w folderze tymczasowym 
            for line in f_xml_read:
                temp_line = str(line)
                #print(school_data_splited)#TODO
                while temp_line.find(word_to_find) != -1:
                    temp_line = temp_line.replace(word_to_find, word_to_put)
                f_xml_write.write(temp_line)

def change_files_names(file_a, file_b):
    os.rename(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + file_a + '.xml', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + file_a + '_temp.xml')
    os.rename(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + file_b + '.xml', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + file_a + '.xml')
    os.rename(cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + file_a + '_temp.xml', cwd + sys_id + school_folder_name + sys_id + school_folder_name + sys_id + 'temp' + sys_id + 'word' + sys_id + file_b + '.xml')
def delete_white_symbol(line):
    if isspace(line[-1]):
        return line[:-1]
    else:
        return line

if len(sys.argv) == 6:
    cwd = sys.argv[1]
    sys_id = sys.argv[2]
    school_folder_name = sys.argv[3]
    xml_good = sys.argv[4]
    xml_bad = sys.argv[5]
    is_ok = True
    with fileinput.input(files = (cwd + sys_id + school_folder_name + sys_id + 'scheme_school_data.txt')) as f_school_data:
        for school_data in f_school_data:
            school_data_splited = school_data.split(';;;')
            if len(school_data_splited) == 2:
                if is_ok:
                    lets_search(xml_good, xml_bad, delete_white_symbol(school_data_splited[0]), delete_white_symbol(school_data_splited[1]))
                else:
                    lets_search(xml_bad, xml_good, delete_white_symbol(school_data_splited[0]), delete_white_symbol(school_data_splited[1]))
                is_ok = not is_ok                
            else:
                sys.exit('Wrong school data (It was: ' + str(school_data_splited) + ' there are ' + str(len(school_data_splited)) + ' arguments')
    if not is_ok:
        change_files_names(xml_bad, xml_good)
else:
    sys.exit('Wrong number of arguments!!!')