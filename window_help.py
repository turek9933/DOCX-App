from tkinter import *
import names
import sys
import os

def foo_to_print(to_print):
    print(to_print)

def clear_window():
    for i in list(b.keys()):
        if not i in ['O aplikacji', 'Skróty', 'Dokumenty', 'Certyfikaty', 'PDF-y', 'Edytor txt']:
            delete_button(i)
    for i in list(l.keys()):
        if not i in []:
            delete_label(i)

def first_look():
    # o_i['line'] = PhotoImage(file = names.relative_to_assets('line_help.png'))
    # o['line'] = canvas.create_image(200, 300, image = o_i['line'])
    
    o['line'] = canvas.create_line(0.33 * window_help_width, 0 * window_help_height, 0.33 * window_help_width, 1 * window_help_height, fill = names.color_line, width = window_help_width / 100)

    new_button('O aplikacji', 'button_help_about.png', 0.015, 0.065)
    b['O aplikacji'].config(command = lambda: [print('button O aplikacji: pressed!'), to_about()])
    new_button('Skróty', 'button_help_shortcuts.png', 0.015, 0.18)
    new_button('Dokumenty', 'button_help_documents.png', 0.015, 0.295)
    new_button('Certyfikaty', 'button_help_certificates.png', 0.015, 0.41)
    new_button('PDF-y', 'button_help_pdfs.png', 0.015, 0.525)
    new_button('Edytor txt', 'button_help_text_editor.png', 0.015, 0.64)
    
    b['Edytor txt'].config(command = lambda: [print('button Edytor txt: pressed!'), new_text(f'''
wyimaginowane zwierze w czasie suszy lubi
asdsadsadadsadaa
trzecia linia
i czwarta najdłuższaaaaaaaaaaaaaaaaaaaaaaaaa liniaa________
''')])
    
    to_about()

def to_about():
    new_title('O aplikacji')


def change_active_button(active: Button):
    active.config(background = names.color_active_background)

# def new_label(label_name: str, file_name: str, x: float, y: float, label_text: str):
#     l_i[label_name] = PhotoImage(file = names.relative_to_assets(file_name))
#     #Label Image placement is referenced to the center of the object
#     l_b[label_name] = canvas.create_image(x + l_i[label_name].width() / 2, y + l_i[label_name].height() / 2, image = l_i[label_name])
#     l[label_name] = canvas.create_text(
#         canvas.coords(l_b[label_name])[0],
#         canvas.coords(l_b[label_name])[1],
#         text = label_text,
#         font = names.font,
#         fill = names.color_font,
#     )

# def new_button(button_name: str, file_name: str, x: float, y: float):
#     b_i[button_name] = PhotoImage(file = names.relative_to_assets(file_name))
#     b[button_name] = Button(
#         image = b_i[button_name],
#         borderwidth = 0,
#         highlightthickness = 0,
#         command = lambda: [print('button ' + button_name + ': pressed!')],
#         background = names.color_background,
#         activebackground = names.color_active_background
#     )
#     #Button placement is referenced to the upper, left corner
#     b[button_name].place(x = x, y = y)
#     print(button_name + ': ' + str(x + b_i[button_name].width() / 2) + ', ' + str(y + b_i[button_name].height() / 2))

# def delete_label(object_name: str):
#     canvas.delete(l[object_name], l_b[object_name], l_i[object_name])
# def delete_button(object_name: str):
#     canvas.delete(b_i[object_name])
#     b[object_name].destroy()

# Tworzy nową etykietę na ekranie
def new_label(label_name: str, file_name: str, x: float, y: float, label_text: str):
    l_i[label_name] = PhotoImage(file = names.relative_to_assets(file_name))
    l_b[label_name] = canvas.create_image(x * window_help_width, y * window_help_height, image = l_i[label_name], anchor = 'nw')
    l[label_name] = canvas.create_text(
        (x * window_help_width) + (l_i[label_name].width() / 2),
        (y * window_help_height) + (l_i[label_name].height() / 2),
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

def new_title(text: str):
    if 'title' in l.keys():
        delete_label('title')
    new_label('title', 'label_average_main.png', 0.45, 0.03, text)

def new_text(text_var: str):
    global current_text
    try:
        canvas.delete(current_text)
    finally:
        current_text = canvas.create_text(
            (0.5 * window_help_width),
            (0.5 * window_help_height),
            text = text_var,
            font = names.font,
            fill = names.color_font,
            anchor = 'center',
            justify = 'center'
        )


window_help_width = 600
window_help_height = 600

l_i = {}#label images
l_b = {}#label backgrounds
l = {}#labels
b_i = {}#button images
b = {}#buttons
o_i = {}#others images
o = {}#others


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

current_text = canvas.create_text(0,0)

first_look()

window_help.mainloop()