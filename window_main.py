from logging import config
from tkinter import *
import tkinter
from tkinter import filedialog, messagebox
from tkinter.filedialog import askopenfilenames, askopenfilename
import names
import sys
import os
import subprocess

def foo_to_print(to_print):
    print(to_print)

# Generuje okienko do odkliku z danym tytulem i treścią wiadomości
def show_confirmation_window(title: str, message: str):
    messagebox.showinfo(title, message)

# Wyświetla w okienku listy plików z tablic docx_list oraz txt_list
# which decyduje, co jest do wyświetlenia: 0 - tylko docx, 1 - tylko txt, 2 - obie listy
def show_lists(which: int):
    # *.docx
    if which == 0:
        if len(docx_list) != 0:
            delete_labels(docx_list)
            y_offset = 0.42# Początkowy offset dla etykiet z nazwami plików
            for i, docx_file in enumerate(docx_list):
                new_label(os.path.basename(docx_file), 'label_average_main.png', 0.04, y_offset, os.path.basename(docx_file))
                y_offset += 0.08# Przesunięcie dla każdej kolejnej etykiety
    # *.txt
    if which == 1:
        if len(txt_list) != 0:
            delete_labels(txt_list)
            y_offset = 0.42# Początkowy offset dla etykiet z nazwami plików
            for i, txt_file in enumerate(txt_list):
                new_label(os.path.basename(docx_file), 'label_average_main.png', 0.04, y_offset, os.path.basename(txt_file))
                y_offset += 0.08# Przesunięcie dla każdej kolejnej etykiety
    # *.docx oraz *.txt
    if which == 2:
        if len(docx_list) != 0 or len(txt_list) != 0:
            delete_labels(docx_list)
            delete_labels(txt_list)
            y_offset = 0.42# Początkowy offset dla etykiet z nazwami plików
            for i, txt_file in enumerate(txt_list):
                new_label(os.path.basename(txt_file), 'label_average_main.png', 0.04, y_offset, os.path.basename(txt_file))
                y_offset += 0.08# Przesunięcie dla każdej kolejnej etykiety
            y_offset = 0.42# Początkowy offset dla etykiet z nazwami plików
            for i, docx_file in enumerate(docx_list):
                new_label(os.path.basename(docx_file), 'label_average_main.png', 0.4, y_offset, os.path.basename(docx_file))
                y_offset += 0.08# Przesunięcie dla każdej kolejnej etykiety

# Odpowiada za zamianę przycisku 'generate' na jego aktywną wersję, jeśli są spełnione odpowiednie opcje dostosowane do funkcjonalności
def generate_button_to_active(option: int):
    if option == 0:
        delete_button('generate')
        new_button('generate', 'button_main_generate.png', 0.738, 0.517)
        b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!'), make_documents()])#TODO Ma być dla robienia dokumentów make_documents()
        show_lists(2)
    elif option == 1:
        if len(txt_list) != 0 and len(docx_list) != 0:
            delete_button('generate')
            new_button('generate', 'button_main_generate.png', 0.738, 0.517)
            b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!'), make_certificates()])
            show_lists(2)
    elif option == 2:
        if len(docx_list) != 0:
            delete_button('generate')
            new_button('generate', 'button_main_generate.png', 0.738, 0.517)
            b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!'), make_pdfs()])
            show_lists(0)
    elif option == 3:
        delete_button('generate')
        new_button('generate', 'button_main_generate.png', 0.738, 0.517)
        b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!'), make_pdfs()])#TODO Ma być do otwierania i edycji plików .txt make_txt()

# Wyświetla wybrane pliki oraz segreguje je na listy plików .txt i .docx
def add_docx_and_txt(filez: tuple, which: int):
    for i in filez:
        if i.endswith('.txt') and not i in txt_list:
            txt_list.append(i)
        elif i.endswith('.docx') and not i in docx_list:
            docx_list.append(i)
    b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!'), generate_button_to_active(which)])
    generate_button_to_active(which)

# Dodaje wybrane pliki .docx do listy i aktywuje przycisk
def add_docx_for_pdf(filez: tuple):
    for i in filez:
        if i.endswith('.docx') and not i in docx_list:
            docx_list.append(i)
    b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!'), generate_button_to_active(2)])
    generate_button_to_active(2)

# Otwiera okno dialogowe do wybierania dokumentów
def open_files():
    return askopenfilenames(filetypes = [('Word i dokumenty tekstowe', '*.docx *.txt')], title = 'NIE PATRZ NA KONIA!')

# Otwiera okno dialogowe do wybierania plików .docx
def open_docx():
    return askopenfilenames(filetypes = [('Word i dokumenty tekstowe', '*.docx')], title = 'NIE PATRZ NA KONIA!')

def open_txt():
    return askopenfilenames(filetypes = [('Dokumenty tekstowe', '*.txt')], title = 'NIE PATRZ NA KONIA!')

# Czyści okno ze wszystkich elementów poza 'help' i '.DOCX-App'
def clear_window():
    for i in list(b.keys()):
        if not i in ['help', 'options']:
            delete_button(i)
    for i in list(l.keys()):
        if not i == '.DOCX-App':
            delete_label(i)

def reset_lists():
    global txt_list, docx_list
    txt_list = []
    docx_list = []

def make_documents():
    try:
        count = 0
        for docx_file in docx_list:
            subprocess.run([names.os_python_command, "maker_documents.py", docx_file, txt_list[0]], check=True)
            count += 1
        show_confirmation_window("Dokumenty OK", f"Zapisano {count} z {len(docx_list)} dokumentów")
    except subprocess.CalledProcessError as e:
        print(f'Błąd tworzenia dokumentów: {e.returncode}, {e.output}')
    except Exception as e:
        print('Błąd tworzenia dokumentów: ', e)

# Uruchamia podproces certificate_maker.py, który generuje certyfikaty
def make_certificates():
    try:
        subprocess.run([names.os_python_command, "maker_certificates.py", docx_list[0], txt_list[0]], check=True)
        show_confirmation_window("Certyfikaty OK", "Zapisano wszystkie certyfikaty")
    except subprocess.CalledProcessError as e:
        print(f'Błąd tworzenia certyfikatów: {e.returncode}, {e.output}')
    except Exception as e:
        print('Błąd tworzenia certyfikatów: ', e)

# Uruchamia podproces maker_pdfs.py, który generuje pliki .pdf z zapisanych w tablicy plików .docx
def make_pdfs():
    try:
        subprocess.run([names.os_python_command, "maker_pdfs.py", *docx_list], check=True)
        show_confirmation_window("PDFs OK", "Zapisano wszystkie pliki .pdf")
    except subprocess.CalledProcessError as e:
        print(f'Błąd tworzenia plików PDF: {e.returncode}, {e.output}')
    except Exception as e:
        print('Błąd tworzenia plików PDF: ', e)

# Przeprowadza do widoku odpowiedzialnego za generowanie dokumentów
def to_documents():
    clear_window()
    new_button('back_arrow', 'button_back_arrow.png', 0.07, 0.8)
    new_label('dokumenty', 'label_main.png', 0.04, 0.25, 'Dokumenty')
    new_label('txt', 'label_short_main.png', 0.04, 0.35, 'Pliki .txt:')
    new_label('docx', 'label_short_main.png', 0.406, 0.35, 'Pliki *.docx:')
    new_button('choose file', 'button_main_choose.png', 0.738, 0.3)
    b['choose file'].config(command = lambda: [foo_to_print('button choose file: pressed!'), add_docx_and_txt(open_files(), 0)])
    new_button('generate', 'button_main_generate_not_active.png', 0.738, 0.5)
    b['generate'].config(command = lambda: [foo_to_print('button generate (not active): pressed!')])
    b['back_arrow'].config(command = lambda: [foo_to_print('button back arrow: pressed!'), clear_window(), to_main()])

# Przeprowadza do widoku odpowiedzialnego za generowanie certyfikatów
def to_certificates():
    clear_window()
    new_button('back_arrow', 'button_back_arrow.png', 0.07, 0.8)
    new_label('certyfikaty', 'label_main.png', 0.04, 0.25, 'Certyfikaty')
    new_label('txt', 'label_short_main.png', 0.04, 0.35, 'Pliki *.txt:')
    new_label('docx', 'label_short_main.png', 0.406, 0.35, 'Pliki *.docx:')
    new_button('choose file', 'button_main_choose.png', 0.738, 0.3)
    b['choose file'].config(command = lambda: [foo_to_print('button choose file: pressed!'), add_docx_and_txt(open_files(), 1)])
    new_button('generate', 'button_main_generate_not_active.png', 0.738, 0.5)
    b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!')])
    b['back_arrow'].config(command = lambda: [foo_to_print('button back arrow: pressed!'), clear_window(), to_main()])

def to_pdf():
    clear_window()
    new_button('back_arrow', 'button_back_arrow.png', 0.07, 0.8)
    b['back_arrow'].config(command = lambda: [foo_to_print('button back arrow: pressed!'), clear_window(), to_main()])
    new_label('pdf', 'label_main.png', 0.04, 0.25, 'PDF')
    new_label('docx', 'label_short_main.png', 0.04, 0.35, 'Pliki *.docx:')
    new_button('choose file', 'button_main_choose.png', 0.738, 0.3)
    b['choose file'].config(command = lambda: [foo_to_print('button choose file: pressed!'), add_docx_for_pdf(open_docx())])
    new_button('generate', 'button_main_generate_not_active.png', 0.738, 0.5)
    b['generate'].config(command = lambda: [foo_to_print('button generate: pressed!')])

# Otwiera okienko z wyborem pliku .txt oraz edytor tesktowy do tego pliku
def to_txt():
    try:
        file_path = askopenfilename(filetypes = [('Dokumenty tekstowe', '*.txt')], title = 'NIE PATRZ NA KONIA!')
        if file_path:
            subprocess.Popen([names.os_python_command, "maker_txt.py", file_path])
    except Exception as e:
        print(f'Błąd przy edycji plików txt: {e.returncode}, {e.output}')

# Inicjuje główny widok aplikacji
def to_main():
    clear_window()
    reset_lists()
    new_label('.DOCX-App', 'label_main.png', 0.04, 0.06, '.DOCX-App')
    new_label('Cóż generujemy', 'label_main.png', 0.24, 0.35, 'Cóż generujemy?')
    new_button('dokumenty', 'button_dokumenty.png', 0.2, 0.5)
    b['dokumenty'].config(command = lambda: [foo_to_print('button dokumenty: pressed!'), to_documents()])
    new_button('certyfikaty', 'button_certyfikaty.png', 0.6, 0.5)
    b['certyfikaty'].config(command = lambda: [foo_to_print('button certyfikaty: pressed!'), to_certificates()])
    new_button('pdf', 'button_pdf.png', 0.2, 0.65)
    b['pdf'].config(command = lambda: [foo_to_print('button pdf: pressed!'), to_pdf()])#TODO
    new_button('edytor_txt', 'button_edytor_txt.png', 0.6, 0.65)
    b['edytor_txt'].config(command = lambda: [foo_to_print('button edytor_txt: pressed!'), to_txt()])#TODO
    
    
    new_button('help', 'button_help.png', 0.868, 0.8)
    b['help'].config(command = lambda: [foo_to_print('button help: pressed'), subprocess.Popen([names.os_python_command, "window_help.py"])])#TODO ('python window_help.py') dla Windowsa, ('python3 window_help.py') dla Linuxa
    new_button('options', 'button_options.png', 0.78, 0.8)
    b['options'].config(command = lambda: [foo_to_print('button_options: pressed'), print(l)])#TODO
    o['line'] = canvas.create_line(0 * window_main_width, 0.18 * window_main_height, 1 * window_main_width, 0.18 * window_main_height, fill = names.color_line, width = window_main_width / 100)
    o['author_tomasz'] = canvas.create_text(
        0.903 * window_main_width,
        0.07 * window_main_height,
        text = 'Tomasz',
        font = names.font_bold,
        fill = names.color_font
    )
    o['author_turek'] = canvas.create_text(
        0.903 * window_main_width,
        0.12 * window_main_height,
        text = 'Turek',
        font = names.font_bold,
        fill = names.color_font
    )


# Tworzy nową etykietę na ekranie
def new_label(label_name: str, file_name: str, x: float, y: float, label_text: str):
    l_i[label_name] = PhotoImage(file = names.relative_to_assets(file_name))
    l_b[label_name] = canvas.create_image(x * window_main_width, y * window_main_height, image = l_i[label_name], anchor = 'nw')
    l[label_name] = canvas.create_text(
        (x * window_main_width) + (l_i[label_name].width() / 2),
        (y * window_main_height) + (l_i[label_name].height() / 2),
        text = label_text,
        font = names.font,
        fill = names.color_font
    )

# Tworzy nowy przycisk na ekranie
def new_button(button_name: str, file_name: str, x: float, y: float):
    b_i[button_name] = PhotoImage(file = names.relative_to_assets(file_name))
    b[button_name] = Button(
        image = b_i[button_name],
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [foo_to_print('button ' + button_name + ': pressed!')],
        background = names.color_background,
        activebackground = names.color_active_background
    )
    #Button placement is referenced to the upper, left corner
    b[button_name].place(relx = x, rely = y)
    foo_to_print(button_name + ': ' + str(x + b_i[button_name].width() / 2) + ', ' + str(y + b_i[button_name].height() / 2))

def delete_labels(files_list: list):
    for file_name in files_list:
        base_name = os.path.basename(file_name)
        if base_name in l:
            delete_label(base_name)

def delete_label(object_name: str):
    canvas.delete(l[object_name])
    canvas.delete(l_b[object_name])
    canvas.delete(l_i[object_name])
    del l[object_name]
    del l_b[object_name]
    del l_i[object_name]

def delete_button(object_name: str):
    canvas.delete(b_i[object_name])
    b[object_name].destroy()
    del b[object_name]
    del b_i[object_name]

window_main_width = 1000
window_main_height = 600

# Biblioteki z elementami graficznymi oraz plikami niezbędnymi do działania
l_i = {}# label images
l_b = {}# label backgrounds
l = {}# labels
b_i = {}# button images
b = {}# buttons
o_i = {}# others images
o = {}# others
txt_list = []# .txt files
docx_list = []# .docx files

# Inicjacja okienka
window_main = Tk()
window_main.geometry(f'{window_main_width}x{window_main_height}')
window_main.title('.DOCX-App')
window_main.configure(background = names.color_background)
window_main.bind('<space>', sys.exit)#TODO Spacja jest przypisana jako guzik wyłączający aplikację

# Stworzenie 'nadpudełka' aplikacji
canvas = Canvas(
    window_main,
    background = names.color_background,
    width = window_main_width,
    height = window_main_height,
    borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat'
)
canvas.place(x = 0, y = 0)

to_main()
window_main.mainloop()