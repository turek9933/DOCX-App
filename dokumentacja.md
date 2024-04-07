# DOCX-App
Tomasz Turek
v. 1.0

## Informacje ogólne
Aplikajca traktuje o manipulowaniu dokumentami w formacie .docx według ustalonych funkcjonalności.
Składa się z 4 głównych modułów.

## Generowanie dokumentów
Funkcjonalność, która wymaga dwóch plików:\
- dokumentu w formacie .docx - A (tych plików może być więcej);\
- dokumentu w formacie .txt - B.\
Intuicja jest następująca - Plik A jest szablonem, występują w nim luki, które można łatwo, mechanicznie uzupełniać kolejnymi danymi.\
Niestety zstawów danych do uzupełnienia jest dużo, więcej niż byłoby sensownie je uzupełniać samemu.
Funcjonalność odpowiada za wykonywanie tego. Jest ona przydatna np. kiedy potrzebujemy stworzyć zestawy podobnych dokumentów, które zawierają poniekąd podobne dane (jak np. daty wystawienia).
Plik A zawiera luki, które są odpowiedno oznaczone. Plik B zawiera oznaczenia oraz wartości, które mają się znaleźć w lukach.

Przykładowe użycie:\
Plik A:\
> Dokument wykonano dnia: {Date}\
> Osoba odpowiedzialna: {Person}\
Plik B:\
> {Date};;;04 marca 2024r.\
> {Person};;;Adam Nowak\
Moduł uzupełni dane i wygeneruje nową kopię pliku A. W tym przypadku będzie wyglądała ona tak:\
> Dokument wykonano dnia: 04 marca 2024r.\
> Osoba odpowiedzialna: Adam Nowak\

## Generowanie certyfikatów
Funkcjonalność, która wymaga dwóch plików:
- dokumentu w formacie .docx - A;
- dokumentu w formacie .txt - B.
Intuicja jest następująca - Plik A jest szablonem, np. certyfikatu, który potrzebuje być wielokrotnie uzupełniony różnymi danymi, które zawsze są podane w identycznej kolejności.
Funkcjonalność generuje wiele kopii pliku A według kolejnych zestawów danych z pliku B. Moduł jest przydatny np. przy wysisywaniu certyfikatów dla wielu kursantów według jednego szablonu.

Przykładowe użycie:
Plik A:
> Data wystawienia: 0000000000
> Certyfikowany: 1111111111
> Instytyt: 2222222222 potwierdza ukończenie kursu!
Plik B:
> 04 marca 2024r.   Adam Nowak  Microsoft
> 10 kwietnia 2024r.   Jarosław Kowalski  Nivida
Moduł uzupełni dane i wygeneruje 2 kopie (ponieważ są dwa zestawy danych) pliku A. W tym przypadku będzie wyglądała ona tak:
Kopia nr 1:
> Data wystawienia: 04 marca 2024r.
> Certyfikowany: Adam Nowak
> Instytyt: Microsoft potwierdza ukończenie kursu!
Kopia nr 2:
> Data wystawienia: 10 kwietnia 2024r.
> Certyfikowany: Jarosław Kowalski
> Instytyt: Nivida potwierdza ukończenie kursu!

## Konwersja na pdf-y
Moduł konwertuje otrzymane pliki .docx na wersje .pdf

## Edytor tekstowy
Moduł pozwalający na prostą, graficzną edycje plików .txt.

### Pozostałe możliwości
Program zawiera też okienko - pomoc - z informacjami o działaniu programu oraz odpowiednim formatowaniu plików.
W ustawieniach można również:
- edytować ustalone w programie separatory plików B;
- zmienić luki plików A w ramach funkcjonalności "Generowanie certyfikatów", tekst występujący w lukach pliku A (do wyboru dzięsięć cyfr, małych lub dużych liter).

### Błędy
Błędy lub nieprawidłowo podane dane będą generować okienko dialogowe z wypisanymi informacjami.

