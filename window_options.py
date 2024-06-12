import json
from tkinter import *
import names

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


    Label(options_window, text = f'Separator dokumentów: "{options.get("separator_documents")}"').pack()
    Entry(options_window, textvariable = separator_documents_var).pack()

    Label(options_window, text = f'Separator certyfikatów: "{options.get("separator_certificates")}"').pack()
    Entry(options_window, textvariable = separator_certificates_var).pack()

    Label(options_window, text = "Placeholder (certyfikaty):").pack()
    OptionMenu(options_window, placeholder_certificates_code_var, *placeholder_options.keys()).pack()


    Label(options_window, text = "Ilość placeholderów (certyfikaty):").pack()
    placeholder_amounts = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    OptionMenu(options_window, placeholder_certificates_amount_var, *placeholder_amounts).pack()
    Label(options_window, text = f'Pierwszy placeholder: "{get_certificate_placeholder(options.get("placeholder_certificates_code"), options.get("placeholder_certificates_amount"))}"').pack()

    Button(options_window, text = "Zapisz", command = lambda: [save_vars_to_settings(separator_documents_var, separator_certificates_var, placeholder_options[placeholder_certificates_code_var.get()], placeholder_certificates_amount_var), refresh_window()]).pack()
    Button(options_window, text = "Przywróć domyślne", command = lambda: [reset_defaults(), refresh_window()]).pack()

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

    icon_image = PhotoImage(file = "button_help.png")
    options_window.iconphoto(True, icon_image, icon_image)
    
    build_options_window()

    options_window.mainloop()

# Pierwsze wczytanie opcji oraz zainicjowanie okna
options = load_options()
create_options_window()