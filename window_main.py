from email.mime import image
from tkinter import *
from tkinter.filedialog import askopenfilenames
from turtle import window_height
import names
import sys
import os
import subprocess


# Function displaying selected files and segregating them into .txt and .docx lists
def show_files(filez: tuple):
    print(filez)
    for i in filez:
        if i.endswith('.txt'):
            txt_list.append(i[i.rfind('/') + 1:i.find('.txt')])
        elif i.endswith('.docx'):
            docx_list.append(i[i.rfind('/') + 1:i.find('.docx')])

# Function opening a dialog window for file selection
def open_files():
    return askopenfilenames(filetypes = [('Word i dokumenty tekstowe', '*.docx *.txt')], title='NIE PATRZ NA KONIA!')

# Function to clear the window of all elements except 'help'
def clear_window():
    for i in b:
        if not i == 'help':
            delete_button(i)
    for i in l:
        if not i == '.DOCX-App':
            delete_label(i)

def make_certificates():
    print("TXT:")
    print(txt_list)
    print("DOCX:")
    print(docx_list)
    subprocess.run(["python", "certificate_maker.py", docx_list[0], txt_list[0]], check=True)


# Function transitioning to the documents section
def to_documents():
    delete_label('Cóż generujemy')
    delete_button('certyfikaty')
    delete_button('dokumenty')
    new_button('back_arrow', 'button_back_arrow.png', 70, 475)
    new_label('dokumenty', 'label_main.png', 40, 150, 'Dokumenty')
    new_label('txt', 'label_short_main.png', 40, 220, 'Pliki .txt:')
    new_label('docx', 'label_short_main.png', 406, 220, 'Pliki *.docx:')
    new_button('choose file', 'button_main_choose.png', 738, 180)
    b['choose file'].config(command = lambda: [print('button choose file: pressed!'), show_files(open_files())])
    new_button('generate', 'button_main_generate_not_active.png', 738, 310)
    b['generate'].config(command = lambda: [print('button generate (not active): pressed!')])
    b['back_arrow'].config(command = lambda: [print('button back arrow: pressed!'), clear_window(), to_main()])

# Function transitioning to the certificates section
def to_certificates():
    delete_label('Cóż generujemy')
    delete_button('certyfikaty')
    delete_button('dokumenty')
    new_button('back_arrow', 'button_back_arrow.png', 70, 475)
    new_label('certyfikaty', 'label_main.png', 40, 150, 'Certyfikaty')
    new_label('txt', 'label_short_main.png', 40, 220, 'Pliki *.txt:')
    new_label('docx', 'label_short_main.png', 406, 220, 'Pliki *.docx:')
    new_button('choose file', 'button_main_choose.png', 738, 180)
    b['choose file'].config(command = lambda: [print('button choose file: pressed!'), show_files(open_files()), make_certificates()])
    new_button('generate', 'button_main_generate_not_active.png', 738, 310)
    b['generate'].config(command = lambda: [print('button generate: pressed!')])
    b['back_arrow'].config(command = lambda: [print('button back arrow: pressed!'), clear_window(), to_main()])

# Function initializing the main view of the application
def to_main():
    new_label('.DOCX-App', 'label_main.png', 40, 40, '.DOCX-App')
    new_label('Cóż generujemy', 'label_main.png', 240, 210, 'Cóż generujemy?')
    new_button('dokumenty', 'button_dokumenty.png', 200, 300)
    b['dokumenty'].config(command = lambda: [print('button dokumenty: pressed!'), to_documents()])
    new_button('certyfikaty', 'button_certyfikaty.png', 600, 300)
    b['certyfikaty'].config(command = lambda: [print('button certyfikaty: pressed!'), to_certificates()])
    new_button('help', 'button_help.png', 868, 468)
    b['help'].config(command = lambda: [print('button help: pressed'), os.system('python window_help.py')])#TODO ('python window_help.py') dla Windowsa, ('python3 window_help.py') dla Linuxa
    o_i['line'] = PhotoImage(file = names.relative_to_assets('line_main.png'))
    o['line'] = canvas.create_image(o_i['line'].width() / 2, 110.0, image = o_i['line'])
    o['author'] = {
    canvas.create_text(
        903,
        40,
        text = 'Tomasz',
        font = names.font_bold,
        fill = names.color_font,
    ),
    canvas.create_text(
        903,
        69,
        text = 'Turek',
        font = names.font_bold,
        fill = names.color_font,
    )}

# Function creating a new label
def new_label(label_name: str, file_name: str, x: float, y: float, label_text: str):
    l_i[label_name] = PhotoImage(file = names.relative_to_assets(file_name))
    #Label Image placement is referenced to the center of the object
    l_b[label_name] = canvas.create_image(x + l_i[label_name].width() / 2, y + l_i[label_name].height() / 2, image = l_i[label_name])
    l[label_name] = canvas.create_text(
        canvas.coords(l_b[label_name])[0],
        canvas.coords(l_b[label_name])[1],
        text = label_text,
        font = names.font,
        fill = names.color_font,
    )

# Function creating a new button
def new_button(button_name: str, file_name: str, x: float, y: float):
    b_i[button_name] = PhotoImage(file = names.relative_to_assets(file_name))
    b[button_name] = Button(
        image = b_i[button_name],
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: [print('button ' + button_name + ': pressed!')],
        background = names.color_background,
        activebackground = names.color_active_background
    )
    #Button placement is referenced to the upper, left corner
    b[button_name].place(x = x, y = y)
    print(button_name + ': ' + str(x + b_i[button_name].width() / 2) + ', ' + str(y + b_i[button_name].height() / 2))

# Function removing a label
def delete_label(object_name: str):
    canvas.delete(l[object_name], l_b[object_name], l_i[object_name])

# Function removing a button
def delete_button(object_name: str):
    canvas.delete(b_i[object_name])
    b[object_name].destroy()

# Size of the app window
window_main_width = 1000
window_main_height = 600

l_i = {}# label images
l_b = {}# label backgrounds
l = {}# labels
b_i = {}# button images
b = {}# buttons
o_i = {}# others images
o = {}# others
txt_list = []# chosen .txt files with data
docx_list = []# chosen .docx files with templates

window_main = Tk()
window_main.geometry(str(window_main_width) + 'x' + str(window_main_height))
window_main.title('.DOCX-App')
window_main.configure(background = names.color_background)# Setting the background color
window_main.bind('<space>', sys.exit)#TODO Space is binded as key to end application 

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