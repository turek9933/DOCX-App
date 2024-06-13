import json
from tkinter import *
from tkinter import ttk
import names
import sys

options_file = names.options_file

# Zwraca bibliotekę z wczytanami opcjami
def load_options():
    try:
        with open(options_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "separator_documents": ";;;",
            "separator_certificates": "\t",
            "placeholder_certificates_code": 48,
            "placeholder_certificates_amount": 10
        }

# Zapisuje bibliotekę options do pliku JSON options_file oraz odświeża widok okienka 
def save_options(options):
    with open(options_file, 'w') as f:
        json.dump(options, f)
    refresh_window()

# Aktualizuje bibliotekę options i wywołuje zapisanie jej do pliku JSON
def save_vars_to_settings(separator_documents_var, separator_certificates_var, placeholder_certificates_code_fixed, placeholder_certificates_amount_var):
    separator_documents = separator_documents_var.get() if separator_documents_var.get() else ";;;"
    separator_certificates = separator_certificates_var.get() if separator_certificates_var.get() else "\t"
    placeholder_certificates_code = placeholder_certificates_code_fixed if placeholder_certificates_code_fixed else 48
    try:
        placeholder_certificates_amount = int(placeholder_certificates_amount_var.get()) if placeholder_certificates_amount_var.get() else 10
    except ValueError:
        placeholder_certificates_amount = 10
    options['separator_documents'] = separator_documents
    options['separator_certificates'] = separator_certificates
    options['placeholder_certificates_code'] = placeholder_certificates_code
    options['placeholder_certificates_amount'] = placeholder_certificates_amount
    save_options(options)

# Przywraca domyślne wartości biblioteki options oraz wywołuje jej zapisanie do pliku JSON
def reset_defaults():
    options = {
        "separator_documents": ";;;",
        "separator_certificates": "\t",
        "placeholder_certificates_code": 48,
        "placeholder_certificates_amount": 10
    }
    save_options(options)

# Generuje ciąg znaków, który odpowiada pierwszemu oczekiwanemu placeholderowi w ramach generowania certyfikatów
def get_certificate_placeholder(char_code: int, amount: int):
    c = chr(char_code)
    result = ''
    for _ in range(amount):
        result += c
    return result

def new_label(window, image_file_name: str, label_text: str, pad_x = 0, pad_y = 0, side_name = 'top', anchor_var = 'center',):
    label_image = PhotoImage(file = names.relative_to_assets(image_file_name))
    label_bg = Canvas(window, width = label_image.width(), bg = names.color_background, height = label_image.height(), highlightthickness = 0)
    label_bg.create_image(0, 0, image = label_image, anchor = 'nw')
    label_bg.create_text(
        label_image.width() / 2,
        label_image.height() / 2,
        text = label_text,
        font = names.font,
        fill = names.color_font
    )
    label_bg.image = label_image
    label_bg.pack(padx = pad_x, pady = pad_y, side = side_name, anchor = anchor_var)
    return label_bg

def new_button(window, image_file_name: str, pad_x = 0, pad_y = 0, side_name = 'top'):
    button_image = PhotoImage(file = names.relative_to_assets(image_file_name))
    button = Button(
        window,
        image = button_image,
        borderwidth = 0,
        highlightthickness = 0,
        background = names.color_background,
        activebackground = names.color_active_background
    )
    button.image = button_image
    button.pack(padx = pad_x, pady = pad_y, side = side_name)
    return button
 

# Wczytuje opcje, generuje: etykiety z ustawieniami aplikacji; pola do wpisania nowych danych; przyciski do zapisania nowych danych lub przywrócenia domyślnych  
def build_options_window():
    global options
    options = load_options()
    separator_documents_var = StringVar(value = options.get('separator_documents', ';;;'))
    separator_certificates_var = StringVar(value = options.get('separator_certificates', '\t'))
    
    placeholder_options = {
        "cyfry": 48,
        "duże litery": 65,
        "małe litery": 97
    }
    placeholder_certificates_code_value = options.get('placeholder_certificates_code', 48)
    placeholder_certificates_code_var = StringVar(value = next(key for key, value in placeholder_options.items() if value == placeholder_certificates_code_value))

    placeholder_certificates_amount_var = IntVar(value = options.get('placeholder_certificates_amount', 10))


    new_label(options_window, 'label_main.png', f'Separator dokumentów: "{options.get("separator_documents")}"', pad_y = 4)
    Entry(options_window, textvariable = separator_documents_var, font = names.font, bg = "white", fg = "black", cursor = 'X_cursor', selectbackground = 'green').pack(pady = (0, 20))
    # Entry(options_window, textvariable=separator_documents_var, font=names.font, bg="white", fg="black", insertbackground="black").pack(pady=(0, 20))

    new_label(options_window, 'label_main.png', f'Separator certyfikatów: "{options.get("separator_certificates")}"', pad_y = 4)
    Entry(options_window, textvariable = separator_certificates_var, font = names.font, bg = "white", fg = "black", cursor = 'X_cursor', selectbackground = 'green').pack(pady = (0, 40))

    new_label(options_window, 'label_main.png', "Placeholder (certyfikaty):", pad_y = 4)
    
    option_menu_code = OptionMenu(options_window, placeholder_certificates_code_var, *placeholder_options.keys())
    option_menu_code.pack(pady = (0, 20))
    option_menu_code.config(font = names.font, background = '#96BE7C', activebackground = '#123A16', cursor = 'X_cursor')
    option_menu_code['menu'].config(font = names.font, background = '#96BE7C', activebackground = '#123A16')

    # option_menu_code = OptionMenu(options_window, placeholder_certificates_code_var, *placeholder_options.keys()).pack(pady = (0, 20))
    # option_menu_code.config(font = names.font)

    new_label(options_window, 'label_main.png', "Ilość placeholderów (certyfikaty):", pad_y = 4)
    placeholder_amounts = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    option_menu_amount = OptionMenu(options_window, placeholder_certificates_amount_var, *placeholder_amounts)
    option_menu_amount.pack(pady = (0, 10))
    option_menu_amount.config(font = names.font, background = '#96BE7C', activebackground = '#123A16', cursor = 'X_cursor')
    option_menu_amount['menu'].config(font = names.font, background = '#96BE7C', activebackground = '#123A16')
    
    new_label(options_window, 'label_average_main.png', 'Pierwszy placeholder:', pad_y = (0, 4))
    new_label(options_window, 'label_main.png', f'"{get_certificate_placeholder(options.get("placeholder_certificates_code"), options.get("placeholder_certificates_amount"))}"', pad_y = (0, 40))


    button_save = new_button(options_window, 'button_zapisz.png', 0, 20)
    button_save.config(cursor = 'X_cursor', command = lambda: [save_vars_to_settings(separator_documents_var, separator_certificates_var, placeholder_options[placeholder_certificates_code_var.get()], placeholder_certificates_amount_var), print('button save: pressed')])
    
    button_reset = new_button(options_window, 'button_przywroc_domyslne.png', 0, 20)
    button_reset.config(cursor = 'X_cursor', command = lambda: [reset_defaults(), print('button reset: pressed')])

# Usuwa wszystkie elementy okna i wywołuje jego ponowne wygenerowanie
def refresh_window():
    for widget in options_window.winfo_children():
        widget.destroy()
    build_options_window()

# Tworzy płótno okna oraz inicjuje wygenerowanie jego widoku
def create_options_window():
    global options_window
        
    options_window = Tk()
    options_window.title("Ustawienia")
    options_window.geometry("600x700")
    options_window.configure(background = names.color_background)
    options_window.bind('<space>', sys.exit)# Spacja jest przypisana jako klawisz wyłączający okienko


    icon_image = PhotoImage(file = "button_help.png")
    options_window.iconphoto(True, icon_image, icon_image)
    
    build_options_window()

    options_window.mainloop()

# Pierwsze wczytanie opcji oraz zainicjowanie okna
options = load_options()
create_options_window()