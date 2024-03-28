from tkinter import *
import names
import sys

def first_look():
    o_i['line'] = PhotoImage(file = names.relative_to_assets('line_help.png'))
    o['line'] = canvas.create_image(200, 300, image = o_i['line'])
    new_button('O aplikacji', 'button_help_1.png', 10, 40)
    b['O aplikacji'].config(command = lambda: [print('button O aplikacji: pressed!'), to_about()])
    new_button('Skróty', 'button_help_2.png', 10, 110)
    new_button('Dokumenty', 'button_help_3.png', 10, 180)
    new_button('Certyfikaty', 'button_help_4.png', 10, 250)

def to_about():
    print()    

def change_active_button(active: Button):
    active.config(background = names.color_active_background)

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

window_help_width = 600
window_help_height = 600

l_i = {}#label images
l_b = {}#label backgrounds
l = {}#labels
b_i = {}#button images
b = {}#buttons
o_i = {}#others images
o = {}#others

choosen_button = 0

window_help = Tk()
window_help.title('Informations')
window_help.geometry(str(window_help_width) + 'x' + str(window_help_height))
window_help.bind('<space>', sys.exit)
window_help.configure(background = names.color_background)

canvas = Canvas(
    window_help,
    background = names.color_background,
    width = 600,
    height = 600,
    borderwidth = 0,
    highlightthickness = 0,
    relief = 'flat'
)
canvas.place(x = 0, y = 0)

first_look()

window_help.mainloop()