# DOCX-App
Tomasz Turek
v. 1.0

## Informacje ogólne
Aplikajca traktuje o manipulowaniu dokumentami w formacie .docx według ustalonych funkcjonalności.
Umożliwia ona:
- generowanie certyfikatów, czyli ciągu dokumentów o identycznych lukach uzupełnianych z plików tekstowych;
- generowanie dokumentów, czyli zbioru różnych dokumentów z lukami do uzupełnienia różnymi, ale znanymi danymi z plików tekstowych;
- konwertowanie plików z formatu .docx na format .pdf;
- prostą edycję plików tekstowych.

Składa się z 4 głównych modułów.

## Generowanie dokumentów
Funkcjonalność, która wymaga dwóch plików:
- dokumentu w formacie .docx - A (tych plików może być więcej);
- dokumentu w formacie .txt - B.

Intuicja jest następująca - Plik A jest szablonem, występują w nim luki, które można łatwo, mechanicznie uzupełniać kolejnymi danymi, np. z bazy danych. Niestety zestawów danych do uzupełnienia jest dużo, więcej niż byłoby sensownie je uzupełniać samemu. Dodatkowym utrudnieniem może być, kiedy plików A również jest dużo.\
Funcjonalność odpowiada za wykonywanie tej pracy. Jest ona przydatna np. kiedy potrzebujemy stworzyć zestaw dokumentów, które zawierają podobne luki na dane (jak np. daty wystawienia).\
Przykładem mogą być szablony dokumentów do uzupełnienia w ramach wniosku urzędowego dla kilku osób. Zamiast wpisywać w każdą lukę ręcznie każdego dane, można za pomocą tej funkcjonalności odpowiednio pooznaczać luki, przygotować dane osób, a funkcjonalność wygeneruje uzupełnione dokumenty dla każdego zestawu danych.

Plik A zawiera luki, które są odpowiedno oznaczone.\
Plik B zawiera oznaczenia oraz wartości, które mają się znaleźć w lukach. Oznaczenia i wartości są rozdzielone separatorem, w przykładzie jest to ";;;", który w ramach ustawień można zmienić.

Przykładowe użycie:\
Plik A:
> Dokument wykonano dnia: {Date}\
> Osoba odpowiedzialna: {Person}

Plik B:
> {Date};;;04 marca 2024r.\
> {Person};;;Adam Nowak

Moduł uzupełni dane i wygeneruje nową kopię pliku A. W tym przypadku będzie wyglądała ona tak:
> Dokument wykonano dnia: 04 marca 2024r.\
> Osoba odpowiedzialna: Adam Nowak

## Generowanie certyfikatów
Funkcjonalność, która wymaga dwóch plików:
- dokumentu w formacie .docx - A;
- dokumentu w formacie .txt - B.

Intuicja jest następująca - Plik A jest szablonem, np. certyfikatu, który potrzebuje być wielokrotnie uzupełniony różnymi **danymi, które zawsze są podane w identycznej kolejności.**
Funkcjonalność generuje wiele kopii pliku A według kolejnych zestawów danych z pliku B.\
Przykładem zastosowanie są certyfikaty, które trzeba wygenerować dla grupy osób.\
Funkcja otrzymuje jako argument szablon oraz zbiór danych uczestników odpowiednio rozdzielony.\
Następnie generuje dla każdego uczestnika osobny dokument z uzupełnionymi danymi.\
Różnica względnem pierwszej funkcjonalności jest taka, iż tutaj dla grupy osób/podmiotów tworzymy jeden ustalony dokument, a tam dla jednej osoby/podmiotu grupę dokumentów.

Plik A zawiera luki, które są odpowiedno oznaczone.
W przykładzie jest to string dziesięcio-znakowy, zwierający cyfry, którym w kolejnych lukach wzrasta wartość.\
Plik B zawiera dane do wstawianie w luki w kolejnych dokumentach odpowiedno rozdzielone.
W przykładzie dane do jednego dokumentu są rozdzielone tabulatorem poziomym "	", natomiast dane do kolejnych dokumentów są rozdzielone znakiem załamania wiersza.

Przykładowe użycie:

Plik A:
> Data wystawienia: 0000000000\
> Certyfikowany: 1111111111\
> Instytyt: 2222222222 potwierdza ukończenie kursu!

Plik B:
> 04 marca 2024r.	Adam Nowak	Microsoft\
> 10 kwietnia 2024r.	Jarosław Kowalski	Nivida

Moduł uzupełni dane i wygeneruje 2 kopie (ponieważ są dwa zestawy danych) pliku A. W tym przypadku będzie wyglądała ona tak:

Kopia nr 1:
> Data wystawienia: 04 marca 2024r.\
> Certyfikowany: Adam Nowak\
> Instytyt: Microsoft potwierdza ukończenie kursu!

Kopia nr 2:
> Data wystawienia: 10 kwietnia 2024r.\
> Certyfikowany: Jarosław Kowalski\
> Instytyt: Nivida potwierdza ukończenie kursu!

## Konwersja na pdf-y
Moduł konwertuje otrzymane pliki .docx na wersje .pdf

## Edytor tekstowy
Moduł pozwalający na prostą, graficzną edycje plików .txt.

### Pozostałe możliwości
Program zawiera też okienko - pomoc - z informacjami o działaniu programu oraz odpowiednim formatowaniu plików.
W ustawieniach można również:
- edytować ustalone w programie separatory plików B (separatory w ramach "Generowanie dokumentów" oraz separatory dla jednego dokumentu w ramach "Generowanie certyfikatów");
- zmienić luki plików A w ramach funkcjonalności "Generowanie certyfikatów", tekst występujący w lukach pliku A (do wyboru dzięsięć cyfr, małych lub dużych liter - maksymalnie 10 luk do uzupełnienia).

### Błędy
Błędy lub nieprawidłowo podane dane będą generować okienko dialogowe z wypisanymi informacjami o potencjalnym źródle problemu.