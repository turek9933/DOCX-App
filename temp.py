from pydoc import doc
from tkinter import *
from tkinter.filedialog import askopenfile, askopenfilenames
from typing import Any
import names
import sys

root = Tk()
root.geometry('400x400')
root.bind('<space>', sys.exit)#TODO

#tkinter.Label(text='Magulo!', font=names.font).pack(anchor='center')

lego_image = {}
lego_bg = {}
lego = {}

def destroy_label(text: str):
    canvas.delete(lego[text], lego_bg[text], lego_image[text])

def destroy_all_buttons(butts: dict):
    print('0 -> ' + str(butts[0]))
    for butt in butts:
        print(butt)
        print(butts[butt])
        butts[butt].destroy()

def add_label(text: str):
    lego_image[text] = PhotoImage(file = names.relative_to_assets('button_main.png'))
    lego_bg[text] = canvas.create_image(400.0, 400.0, image = label_1_image)
    lego[text] = canvas.create_text(
        canvas.coords(lego_bg[text])[0],
        canvas.coords(lego_bg[text])[1],
        text = text,
        font = names.font,
        fill = names.color_font
    )

def open_file():
    #file = askopenfile(mode ='r')
    filez = askopenfilenames(filetypes=[('PYTHON', '*py')], title='Paola')
    txt_list = {'q', 'w', 'e', 'r', 'ALA'}
    print(txt_list)
    txt_list.update('r', 't', 'y', 'ALE')
    print(txt_list)
    
    docx_list = []
    print(docx_list)
    docx_list.append('ala')
    docx_list.append('ola')
    docx_list.append('lola')
    print(docx_list)
    docx_list.extend('ala')
    print(docx_list)
    #if file is not None:
    #    content = file.read()
    #    print(content)

canvas = Canvas(
    root,
    background = names.color_background,
    width = 1000,
    height = 600,
    #borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat'
)
canvas.place(x = 0, y = 0)

label_1_image = PhotoImage(file = names.relative_to_assets('button_main.png'))
label_1_bg = canvas.create_image(150.0, 100.0, image = label_1_image)
label_1 = canvas.create_text(
    canvas.coords(label_1_bg)[0],
    canvas.coords(label_1_bg)[1],
    text = 'LABEL 1',
    font = names.font,
    fill = names.color_font
)

buttons_images = {}

buttons_images['O aplikacji'] = PhotoImage(file = names.relative_to_assets('button_help_1.png'))

buttons = {}
buttons['O aplikacji'] = Button(
    root,
    image = buttons_images['O aplikacji'],
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: [print('button_1 - O aplikacji: pressed!'), print(buttons['O aplikacji']), add_label('Paooolaa')],
    background = names.color_background,
    activebackground = names.color_active_background
)
buttons['O aplikacji'].place(x = 10 + buttons_images['O aplikacji'].width() / 2, y = 40 + buttons_images['O aplikacji'].height() / 2)

button_1 = Button(
    image = label_1_image,
    #command = lambda: [destroy_label('Paooolaa')]
    command = open_file
)
button_1.place(x = 0, y = 200)

root.mainloop()