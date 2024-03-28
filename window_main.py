from email.mime import image
from tkinter import *
from tkinter.filedialog import askopenfilenames
from turtle import window_height
import names
import sys
import os

def show_files(filez: tuple):
    print(filez)
    txt_list = []
    docx_list = []
    for i in filez:
        if i.find('.txt') != -1:
            if i not in txt_list:
                txt_list.append(i[i.rfind('/') + 1:i.find('.txt')])
        elif i.find('.docx') != -1:
            if i not in docx_list:
                docx_list.append(i[i.rfind('/') + 1:i.find('.docx')])



def open_files():
    return askopenfilenames(filetypes = [('Word i dokumenty tekstowe', '*.docx *.txt')], title='NIE PATRZ NA KONIA!')

def clear_window():
    for i in b:
        if not i == 'help':
            delete_button(i)
    for i in l:
        if not i == 'Erasmus machine':
            delete_label(i)

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

def to_certificates():
    delete_label('Cóż generujemy')
    delete_button('certyfikaty')
    delete_button('dokumenty')
    new_button('back_arrow', 'button_back_arrow.png', 70, 475)
    new_label('certyfikaty', 'label_main.png', 40, 150, 'Certyfikaty')
    new_label('txt', 'label_short_main.png', 40, 220, 'Pliki *.txt:')
    new_label('docx', 'label_short_main.png', 406, 220, 'Pliki *.docx:')
    new_button('choose file', 'button_main_choose.png', 738, 180)
    b['choose file'].config(command = lambda: [print('button choose file: pressed!'), show_files(open_files())])
    new_button('generate', 'button_main_generate_not_active.png', 738, 310)
    b['generate'].config(command = lambda: [print('button generate (not active): pressed!')])
    b['back_arrow'].config(command = lambda: [print('button back arrow: pressed!'), clear_window(), to_main()])

def to_main():
    new_label('Erasmus machine', 'label_main.png', 40, 40, 'Erasmus machine')
    new_label('Cóż generujemy', 'label_main.png', 240, 210, 'Cóż generujemy?')
    new_button('dokumenty', 'button_dokumenty.png', 200, 300)
    b['dokumenty'].config(command = lambda: [print('button dokumenty: pressed!'), to_documents()])
    new_button('certyfikaty', 'button_certyfikaty.png', 600, 300)
    b['certyfikaty'].config(command = lambda: [print('button certyfikaty: pressed!'), to_certificates()])
    new_button('help', 'button_help.png', 868, 468)
    b['help'].config(command = lambda: [print('button help: pressed'), os.system('python3 window_help.py')])
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

def delete_label(object_name: str):
    canvas.delete(l[object_name], l_b[object_name], l_i[object_name])
def delete_button(object_name: str):
    canvas.delete(b_i[object_name])
    b[object_name].destroy()

window_main_width = 1000
window_main_height = 600
l_i = {}#label images
l_b = {}#label backgrounds
l = {}#labels
b_i = {}#button images
b = {}#buttons
o_i = {}#others images
o = {}#others

window_main = Tk()
window_main.geometry(str(window_main_width) + 'x' + str(window_main_height))
window_main.title('Erasmus machine')
window_main.configure(background = names.color_background)
window_main.bind('<space>', sys.exit)#TODO

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