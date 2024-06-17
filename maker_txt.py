import sys
import os
from tkinter import *
from tkinter import filedialog, messagebox, font


# Generuje okienko do odkliku z danym tytulem i treścią wiadomości
def show_confirmation_window(title: str, message: str):
    messagebox.showinfo(title, message)

# Zwraca odczytany plik
def load_file(file_path):
    with open(file_path, 'r', encoding = 'utf-8') as file:
        return file.read()

# Zapisuje do piku daną zawartość
def save_file(file_path, content):
    with open(file_path, 'w', encoding = 'utf-8') as file:
        file.write(content)

# Otwiera i wczytuje do aplikacji plik tekstowy
def open_file():
    file_path = filedialog.askopenfilename(filetypes = [('Dokumenty tekstowe', '*.txt')])
    if file_path:
        text.delete(1.0, END)
        text.insert(END, load_file(file_path))
        window.title(f"Edytor - {os.path.basename(file_path)}")
        global current_file
        current_file = file_path

def save_current_file(event = None):
    if current_file:
        save_file(current_file, text.get(1.0, END))
        show_confirmation_window("Sukces", f"Zapisano plik: {current_file}")

def save_as_new_file(event = None):
    file_path = filedialog.asksaveasfilename(defaultextension = ".txt", filetypes = [('Dokumenty tekstowe', '*.txt')])
    if file_path:
        save_file(file_path, text.get(1.0, END))
        show_confirmation_window("Sukces", f"Zapisano plik: {file_path}")

# Obsługuje zmianę używanego w oknie fontu
def change_font_family(new_font_family):
    global current_font_family, current_font
    current_font_family = new_font_family
    current_font.config(family = new_font_family)
    text.config(font = current_font)

# Obsługuje zmianę używanego w oknie rozmiaru fontu
def change_font_size(new_font_size):
    global current_font_size, current_font
    current_font_size = new_font_size
    current_font.config(size = new_font_size)
    text.config(font = current_font)

def increase_font_size(event=None):
    global current_font_size, current_font
    current_font_size += 1
    current_font.config(size = current_font_size)
    text.config(font = current_font)

def decrease_font_size(event=None):
    global current_font_size, current_font
    current_font_size -= 1
    current_font.config(size = current_font_size)
    text.config(font = current_font)

# Obsługuje cofnięcie zmian. Pomija błąd w przypadku próby cofnięcia do nieistniejącego stanu
def undo(event = None):
    try:
        text.edit_undo()
    except TclError:
        pass

# Obsługuje przywracanie zmian. Pomija błąd w przypadku próby przywrócenia nieistniejącego stanu
def redo(event = None):
    try:
        text.edit_redo()
    except TclError:
        pass

# Sprawdza poprawną ilość argumentów wywołania skryptu
if len(sys.argv) != 2:
    print("Prawidłowa forma wywołania programu: python script.py <plik.txt>")
    sys.exit(1)

input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print(f"Not found: {input_file}")
    sys.exit(1)

current_file = input_file

window = Tk()
window.title(f"Edytor - {os.path.basename(current_file)}")
window.geometry("800x600")

current_font_family = "Arial"
current_font_size = 12
current_font = font.Font(family = current_font_family, size = current_font_size)

text = Text(window, wrap = 'word', font = current_font, undo = True)
text.pack(expand = 1, fill = 'both')
text.insert(END, load_file(input_file))

menu = Menu(window)
window.config(menu = menu)

file_menu = Menu(menu)
menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save", command = save_current_file)
file_menu.add_command(label = "Save As", command = save_as_new_file)

# Lista dostępnych fontów
font_families = ["Arial", "Courier", "Times New Roman", "Verdana", "Lato"]
font_menu = Menu(menu)
menu.add_cascade(label = "Font", menu = font_menu)
# Dodanie opcji zmiany rodziny fontu
for family in font_families:
    font_menu.add_command(label = family, command = lambda f = family: change_font_family(f))


# Lista dostępnych rozmiarów
font_sizes = [8, 10, 12, 14, 16, 18, 20, 24, 32, 40, 60]
size_menu = Menu(menu)
menu.add_cascade(label = 'Rozmiar', menu = size_menu)
# Dodanie opcji zmiany rozmiaru fontu
for size in font_sizes:
    size_menu.add_command(label = str(size), command = lambda s = size: change_font_size(s))


window.bind('<Control-s>', lambda event: save_current_file())
window.bind('<Control-S>', lambda event: save_as_new_file())
window.bind('<Control-Shift-s>', lambda event: save_as_new_file())
window.bind('<Control-plus>', increase_font_size)
window.bind('<Control-minus>', decrease_font_size)
window.bind('<Control-z>', undo)
window.bind('<Control-y>', redo)

window.mainloop()