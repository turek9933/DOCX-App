# DOCX-App
#### Tomasz Turek

## Opis
DOCX-App to aplikacja służąca do manipulacji dokumentami w formacie .docx według ustalonych funkcjonalności. Aplikacja jest napisana w Pythonie i umożliwia generowanie certyfikatów, tworzenie dokumentów, konwertowanie plików z formatu .docx na .pdf oraz prostą edycję plików tekstowych.

## Funkcjonalności
- **Generowanie certyfikatów:** Tworzenie wielu kopii dokumentu .docx, uzupełnianych danymi z pliku .txt.
- **Generowanie dokumentów:** Tworzenie zbioru różnych dokumentów z uzupełnionymi lukami.
- **Konwertowanie plików:** Konwersja plików .docx na .pdf.
- **Edycja plików tekstowych:** Prosta graficzna edycja plików .txt.
- **Dostosowywanie ustawień:** Personalizowanie separatorów i placeholderów aplikacji.

## Wymagania systemowe
- Python 3.6 lub nowszy. (Pliki do pobrania oraz opis procesu instalacji znajduje się pod adresem: **https://www.python.org**)
- Biblioteki Python: wymienione są w pliku w pliku `requirements.txt`
- Obsługa skryptów bash (opcjonalna dla Windows, np. poprzez Git Bash)


## Instalacja i uruchomienie
1. Sklonuj repozytorium i przejdź do katalogu:\
    Z użyciem Git-a:
    ```bash
    git clone https://github.com/turek9933/DOCX-App
    cd DOCX-App
    ```
    Ręcznie:
    ```
    Pobierz skompresowanego .zip-a z repozytorium: https://github.com/turek9933/DOCX-App -> "Code" -> "Download ZIP"
    Wypakuj repozytorium do wybranego katalogu, np. do "DOCX-App-main"
    Przejdź do wybranego katalogu
    ```
2. Zainstaluj wymagane biblioteki i uruchoma aplikację:\
    Z wykorzystaniem skryptów uruchomieniowych:
    ```bash
    run.sh # Dla Linux
    run.bat # Dla Windows
    ```
    Ręcznie:
    ```bash
    pip install -r requirements.txt
    python3 window_main.py # Dla Linux
    python3 window_main.py # Dla Windows
    ```
3. Korzystaj z aplikacji poprzez interfejs graficzny, wybierając odpowiednie funkcjonalości.

### Skróty klawiszowe
W aplikacji występuje skromna ilość skrótów klawiszowych ułatwiających korzystanie.

- `<space>` - Zamknięcie aktywnego okienka

#### Skróty edytora tekstowego:
- `<Control> + <S>` - Zapis dokumentu
- `<Control> + <Shift> + <S>` - Zapis dokumentu jako
- `<Control> + <plus>` - Zwiększenie rozmiaru fontu
- `<Control> + <minus>` - Zmniejszenie rozmiaru fontu
- `<Control> + <Z>` - Cofnięcie zmiany
- `<Control> + <Y>` - Przywrócenie zmiany

## Przykłady użycia

### Generowanie dokumentów
1. Przygotuj plik .docx z miejscami do uzupełnienia:
    ```
    Nazwa szkoły: {school_name}
    Nazwa projektu: {project_name}
    Współfinansowany ze środków: {co_financing}
    ```
2. Przygotuj plik .txt z danymi:
    ```
    {school_name};;;Akademia Ekonomiczno-Humanistyczna w Warszawie
    {project_name};;;Erasmus+
    {co_financing};;;Unia Europejska
    ```
3. Wybierz odpowiednie funkcjonalości w aplikacji i wygeneruj dokumenty.


### Generowanie certyfikatów
1. Przygotuj plik .docx z miejscami do uzupełnienia:
    ```
    Data wystawienia: 0000000000
    Certyfikowany: 1111111111
    Instytut: 2222222222 potwierdza ukończenie kursu!
    ```
2. Przygotuj plik .txt z danymi:
    ```
    04 marca 2024r.	Adam Nowak	Microsoft
    10 kwietnia 2024r.	Jarosław Kowalski	Nvidia
    ```
3. Wybierz odpowiednie funkcjonalości w aplikacji i wygeneruj certyfikaty.

### Generowanie PDF-ów
1. Przygotuj dokumenty w formacie .docx
2. Wybierz odpowiednią funkcjonalość w aplikacji i wygeneruj PDF-y.

### Edycja tekstowa
1. Wybierz odpowiednią funkcjonalości w aplikacji i otwórz edytor. Zmieniaj font, zapisuj cofaj i przywracaj zmiany.

### Personalizacja ustawień
1. Wybierz opcje w aplikacji.
2. Dostosuj według potrzeb wygląd separatorów dokumentów i certyfikatów, a także wygląd placeholderów według zaproponowanych możliwości.
