from tkinter import *
from tokenize import Name
import names
import sys
import os

def foo_to_print(to_print):
    print(to_print)

# Ciąg funkcji zwracających tekst opisujący dane aspaekty aplikacji dla użytkownika

def text_about():
    return '''Aplikacja traktuje o manipulowaniu dokumentami w formacie .docx według ustalonych funkcjonalności. Zostanie stworzona w języku Python.
Aplikacja umożliwia:
- generowanie certyfikatów, czyli ciągu dokumentów o identycznych lukach uzupełnianych z plików tekstowych;
- generowanie dokumentów, czyli zbioru różnych dokumentów z lukami do uzupełnienia różnymi, ale znanymi danymi z plików tekstowych;
- konwertowanie plików z formatu .docx na format .pdf;
- prostą edycję plików tekstowych.'''

def text_shortcuts():
    return '''Skróty dostępne w aplikacji:
<space> - Zamknięcie aktywnego okienka

Skróty edytora tekstowego:
<Control> + <S> - Zapis danego dokumentu
<Control> + <S> - Zapis dokumentu jako
<Control> + <Shift> + <s> - Zapis dokumentu jako
<Control> + <plus> - Zwiększenie rozmiaru fontu
<Control> + <minus> - Zwiększenie rozmiaru fontu
<Control> + <z> - Cofnięcie zmiany
<Control> + <y> - Przywrócenie zmiany'''

def text_documents():
    return '''Funkcjonalność, która wymaga dwóch plików:
- dokumentu w formacie .docx - A (tych plików może być więcej);
- dokumentu w formacie .txt - B.

Intuicja: Plik A jest szablonem, występują w nim luki, które można łatwo, mechanicznie uzupełniać kolejnymi danymi, np. z bazy danych. Niestety zestawów danych do uzupełnienia jest dużo, więcej niż byłoby sensownie uzupełniać ręcznie. Dodatkowym utrudnieniem może być, kiedy plików A również jest dużo.
Przykładem mogą być szablony dokumentów do uzupełnienia w ramach wniosku urzędowego dla kilku osób. Zamiast wpisywać w każdą lukę ręcznie każdego dane, można za pomocą tej funkcjonalności odpowiednio pooznaczać luki, przygotować dane osób, a funkcjonalność wygeneruje uzupełnione dokumenty dla każdego zestawu danych.

Plik A zawiera luki, które są odpowiedno oznaczone.
Plik B zawiera oznaczenia oraz wartości, które mają się znaleźć w lukach. Oznaczenia i wartości są rozdzielone separatorem (domyślnie jest to ";;;"), który w ramach ustawień można zmienić.

Przykładowe użycie:
Plik A:
> Dokument wykonano dnia: {Date}
> Osoba odpowiedzialna: {Person}

Plik B:
> {Date};;;04 marca 2024r.
> {Person};;;Adam Nowak

Moduł uzupełni dane i wygeneruje nową kopię pliku A. W tym przypadku będzie wyglądała ona tak:
> Dokument wykonano dnia: 04 marca 2024r.
> Osoba odpowiedzialna: Adam Nowak'''

def text_certificates():
    return '''Funkcjonalność, która wymaga dwóch plików:
- dokumentu w formacie *.docx - A;
- dokumentu w formacie *.txt - B.

Intuicja: Plik A jest szablonem, np. certyfikatu, który potrzebuje być wielokrotnie uzupełniony różnymi danymi, które zawsze są podane w identycznej kolejności.
Funkcjonalność generuje wiele kopii pliku A według kolejnych zestawów danych z pliku B.

Plik A zawiera luki, które są odpowiedno oznaczone.
Domyślnie jest to wyraz dziesięcio-znakowy, zwierający cyfry, którym w kolejnych lukach wzrasta wartość.
Plik B zawiera dane do wstawianie w luki w kolejnych dokumentach odpowiedno rozdzielone.
Domyślnie dane do jednego dokumentu są rozdzielone tabulatorem poziomym "	", natomiast dane do kolejnych dokumentów są rozdzielone znakiem załamania wiersza.

Przykładowe użycie:

Plik A:
> Data wystawienia: 0000000000
> Certyfikowany: 1111111111
> Instytyt: 2222222222 potwierdza ukończenie kursu!

Plik B:
> 04 marca 2024r.    Adam Nowak    Microsoft
> 10 kwietnia 2024r.    Jarosław Kowalski    Nivida

Moduł uzupełni dane i wygeneruje 2 kopie (ponieważ są dwa zestawy danych) pliku A. W tym przypadku będzie wyglądała ona tak:

Kopia nr 1:
> Data wystawienia: 04 marca 2024r.
> Certyfikowany: Adam Nowak
> Instytyt: Microsoft potwierdza ukończenie kursu!

Kopia nr 2:
> Data wystawienia: 10 kwietnia 2024r.
> Certyfikowany: Jarosław Kowalski
> Instytyt: Nivida potwierdza ukończenie kursu!'''

def text_pdfs():
    return '''Moduł konwertuje wybrane pliki *.docx na ich wersje *.pdf'''

def text_txt_editor():
    return '''Moduł pozwala na prostą, graficzną edycje plików *.txt.
Umożliwia wczystanie, edycję i zapis dokumentu.
Użytkownik może zmieniać font i jego rozmiar wyświetlanego tekstu'''


# Usuwa wyświetlane obiekty, które nie są podstawowymi elementami okna
def clear_window():
    for i in list(b.keys()):
        if not i in ['O aplikacji', 'Skróty', 'Dokumenty', 'Certyfikaty', 'PDF-y', 'Edytor txt']:
            delete_button(i)
    for i in list(l.keys()):
        if not i in []:
            delete_label(i)

# Generuje podstawowy widok okna aplikacji. Dodaje linię na środku, przyciski do przechodzenia między widokami oraz uruchamia widok 'O aplikacji'
def first_look():    
    o['line'] = canvas.create_line(0.33 * window_help_width, 0 * window_help_height, 0.33 * window_help_width, 1 * window_help_height, fill = names.color_line, width = window_help_width / 100)

    new_button('O aplikacji', 'button_help_about.png', 0.015, 0.065)
    b['O aplikacji'].config(command = lambda: [print('button O aplikacji: pressed!'), to_about()])

    new_button('Skróty', 'button_help_shortcuts.png', 0.015, 0.18)
    b['Skróty'].config(command = lambda: [print('button Skróty: pressed!'), to_shortcuts()])

    new_button('Dokumenty', 'button_help_documents.png', 0.015, 0.295)
    b['Dokumenty'].config(command = lambda: [print('button Dokumenty: pressed!'), to_documents()])

    new_button('Certyfikaty', 'button_help_certificates.png', 0.015, 0.41)
    b['Certyfikaty'].config(command = lambda: [print('button Certyfikaty: pressed!'), to_certificates()])
    
    new_button('PDF-y', 'button_help_pdfs.png', 0.015, 0.525)
    b['PDF-y'].config(command = lambda: [print('button PDF-y: pressed!'), to_pdfs()])


    new_button('Edytor txt', 'button_help_text_editor.png', 0.015, 0.64)
    b['Edytor txt'].config(command = lambda: [print('button Edytor txt: pressed!'), to_text_editor()])
    
    to_about()

# Ciąg funkcji generujących widoki z informacjami o kolejnych aspektach aplikacji
def to_about():
    new_title('O aplikacji')
    new_text(text_about())

def to_shortcuts():
    new_title('Skróty')
    new_text(text_shortcuts())

def to_documents():
    new_title('Dokumenty')
    new_text(text_documents())

def to_certificates():
    new_title('Certyfikaty')
    new_text(text_certificates())

def to_pdfs():
    new_title('PDF-y')
    new_text(text_pdfs())

def to_text_editor():
    new_title('Edytor txt')
    new_text(text_txt_editor())


# Tworzy nową etykietę na ekranie z danym tekstem o danych współrzędnych
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

# Tworzy nowy przycisk na ekranie o danych współrzędnych
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
    # Button placement is referenced to the upper, left corner
    b[button_name].place(relx = x, rely = y)
    foo_to_print(button_name + ': ' + str(x + b_i[button_name].width() / 2) + ', ' + str(y + b_i[button_name].height() / 2))

# Usuwa etykietę o danej nazwie
def delete_label(object_name: str):
    canvas.delete(l[object_name])
    canvas.delete(l_b[object_name])
    canvas.delete(l_i[object_name])
    del l[object_name]
    del l_b[object_name]
    del l_i[object_name]

# Usuwa przycisk o danej nazwie
def delete_button(object_name: str):
    canvas.delete(b_i[object_name])
    b[object_name].destroy()
    del b[object_name]
    del b_i[object_name]

# Generuje etykietę o danym teksie. Etykieta ta jest tytułową dla danego widoku okna.
def new_title(text: str):
    if 'title' in l.keys():
        delete_label('title')
    new_label('title', 'label_average_main.png', 0.45, 0.03, text)

# Generuje dany tekst, który opisuje funkcjonalność. Sprawdza, czy tekst nie występuje w oknie i generuje nowy wraz z możliwością 'scrolowania'. 
def new_text(text_var: str):
    global current_text, current_scrollbar
    try:
        current_text.destroy()
        current_scrollbar.destroy()
    except NameError:
        pass
    finally:
        current_text = Text(
            canvas,
            wrap = 'word',
            font = names.font_small,
            bg = names.color_background,
            fg = names.color_font,
            width = 40,
            borderwidth = 0,
            highlightthickness = 0
        )

        current_scrollbar = Scrollbar(canvas, command = current_text.yview)
        current_text.config(yscrollcommand = current_scrollbar.set)

        current_text.insert('1.0', text_var)
        
        current_text.tag_configure("center", justify = "center")
        current_text.tag_add("center", 1.0, "end")
        
        current_text.config(state = DISABLED)

        text_window  = canvas.create_window(
            (0.665 * window_help_width),
            (0.5 * window_help_height),
            window = current_text,
            anchor = 'center'
        )

        scrollbar_window  = canvas.create_window(
            (0.665 * window_help_width + 200),
            (0.5 * window_help_height),
            window = current_scrollbar,
            anchor = 'center',
            height = 0.8 * window_help_height
        )


# Rozmiary okna
window_help_width = 600
window_help_height = 600

l_i = {}#label images
l_b = {}#label backgrounds
l = {}#labels
b_i = {}#button images
b = {}#buttons
o_i = {}#others images
o = {}#others

# Konfiguracja okienka
window_help = Tk()
window_help.title('Informations')
window_help.geometry(str(window_help_width) + 'x' + str(window_help_height))
window_help.configure(background = names.color_background)
icon_image = PhotoImage(file = "graphic/button_help.png")
window_help.iconphoto(True, icon_image, icon_image)
window_help.bind('<space>', sys.exit)

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

# Przejście do podtawowego widoku okna
first_look()

window_help.mainloop()