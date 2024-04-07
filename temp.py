import tkinter as tk
from tkinter import scrolledtext
import sys

# Funkcja do zapisywania zawartości pola tekstowego do pliku
def save_text():
    text_content = text_area.get(1.0, tk.END)
    with open(file_path, 'w') as file:
        file.write(text_content)

# Sprawdzenie, czy ścieżka do pliku została podana jako argument
if len(sys.argv) < 2:
    print("Usage: python text_editor.py <path_to_file>")
    sys.exit(1)

file_path = sys.argv[1]

# Tworzenie głównego okna aplikacji
window = tk.Tk()
window.title("Prosty Edytor Tekstu")

# Dodanie pola tekstowego z przewijaniem
text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD)
text_area.pack(fill=tk.BOTH, expand=True)

# Próba otwarcia i wczytania pliku, jeśli istnieje
try:
    with open(file_path, 'r') as file:
        text_area.insert(tk.INSERT, file.read())
except FileNotFoundError:
    print(f"File not found: {file_path}")

# Dodanie przycisku do zapisywania tekstu
save_button = tk.Button(window, text="Zapisz", command=save_text)
save_button.pack(side=tk.BOTTOM)

window.mainloop()
