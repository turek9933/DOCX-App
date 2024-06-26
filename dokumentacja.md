# DOCX-App
Tomasz Turek
v. 1.0

## Spis treści

1. [Informacje ogólne](#informacje-ogólne)
2. [Generowanie dokumentów](#generowanie-dokumentów)
3. [Generowanie certyfikatów](#generowanie-certyfikatów)
4. [Konwersja na pdf-y](#konwersja-na-pdf-y)
5. [Edytor tekstowy](#edytor-tekstowy)
6. [Pozostałe możliwości](#pozostałe-możliwości)
7. [Czasochłonność projektu](#czasochłonność-projektu)
8. [Plan realizacji projektu](#plan-realizacji-projektu)
9. [Przypadki użycia](#Przypadki-użycia)
10. [Strategia bezpieczeństwa](#strategia-bezpieczeństwa)
11. [Harmonogram testów](#harmonogram-testów)
11. [Zabezpieczenia projektu](#zabezpieczenia-projektu)

## Informacje ogólne
Aplikacja traktuje o manipulowaniu dokumentami w formacie .docx według ustalonych funkcjonalności. Zostanie stworzona w języku Python, dostępna będzie na platformę Windows. (W przyszłości, przy łatwej portacji, zostanie opracowana również wersja na Linux-a.)
Aplikacja umożliwia:
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

## Czasochłonność projektu

Szacowany czas wykonania projektu od początku do końca wynosi od 4 do 8 tygodni. Rozstrzał wynika z jednoosobowego wykonania, potrzeby lepszego poznania technologii do zastosowania, a także z podejścia polegającego na dozowaniu pracy w celu utrzymania zainteresowania projektem.\
Projekt zatem powinien trwać od 4 do 8 tygodnii, przy pracy jednej osoby, w nakładzie 4-5 dni w tygodniu przez 3-5 h dziennie.

### Wymagane zasoby

Zasoby wymagane do realizacji projektu można podzielić na dwa rodzaje: sprzętowe i ludzie.

Zasoby sprzętowe niezbędne do realizacji projektu to przede wszystkim komputery:
- obsługujące środowiska programistyczne w języku Python, z uwzględnieniem biblioteki Tkinter;
- mające dostęp do systemu kontroli wersji (Git i GitHub).

Dodatkowo niezbędne do pracy w zespole są ścieżki komunikacji oraz przekazywania informacji. (Aczkolwiek nie w przypadku tego jednoosobowego projektu.)

Zasoby ludzkie niezbędne do realizacji projektu to osoby mające wiedzę i/lub praktykę w:
- obsłudze języka Python w kontekście działania na plikach;
- obsłudze biblioteki Tkinter, na której bazuje frontend aplikacji;
- integracji elementów back- oraz front-end-owych;
- przeprowadzaniu testów aplikacji oraz ocenianiu odczuć użytkownika.

Wobec powyższych wymagań optymalny wydaje się podział na zespół 2 lub 3 osobowy, gdzie występują podziały obowiązków.

Wariant 3 osobowy:
- programista obsługujący pracę modułów w backend-zie oraz przeprowadzający testy modularne;
- programista projektujący wygląd, obsługę aplikacji dla użytkownika, przeprowadzający wstępne testy użytkownicze;
- koordynator pracy, odpowiedzialny za intergację modułów z wyglądem aplikacji.

W wariancie 2 osobowym funkcja koordynator mógłby zostać podzielona na dwóch programistów, którzy symultanicznie konsultowaliby stan projektu, nakreślali cele i poświęcali czas na sprawdzanie dotyczasowej integracji modułów.

W przypadku tego projektu sam łącze owe funkcje.

## Plan realizacji projektu

![Plan realizacji projektu](./Plan.png)

Powyższy plan obrazuje schematycznie założenia realizacji kolejnych etapów. Został on rozpisany na 6 tygodni, a "wyblakłe" elementy wskazują na elementy realizacji, które powinny być prostsze od pozostałych. Faktyczne wykonanie projektu może się różnić od schematu, a także ulec rozciągnięciu lub skróceniu w czasie.


#### Omówienie etapów realizacji

- Planowanie, projektowanie i dokumentacja:\
    Zakłada: przeznaczenie 1. tygodnia na zaplanowanie wyglądu i funkcjonalności; kolejnych 4. na dokumentacje wykonywaną na bieżąco, która będzie dotyczyć wykonywanych działań; ostatniego tygodnia na uzupełnienie finalne dokumentacji oraz stworzenie instrukcji instalacji aplikacji.
- Nauka technologi:\
    Etap zakłada poznanie biblioteki Python - Tkinter, która odpowiada za graficzny interfejs użytkowanej aplikacji. Z pewnością, dokonywana będzie również pomniejsza nauka w trakcie działań, w odpowiedzi na spotykane trudności.
- Testy:\
    Poświęcone zostaną głównie sprawdzaniu odporności aplikacj na podwawanie niewłaściwych danych, infromowanie o tym użytkownika oraz obsłudze wyjątków. Na koniec projektu przetestowane zostanie również proces instalacji programu zgodnie ze stworzoną dokumentacją.
- Prace nad modułami:\
    Prace backend-owe, które skupiać się będą nad opracowaniem metodyki obsługi dokumentów oraz ich interpretacją w ramach aplikacji. Na tym etapie zostaną stworzone najpierw moduły generujące pliki .docx, a następnie .pdf-y oraz zostanie opracowana prosta edycja plików .txt, zgodnie z założeniami funkcjonalności.
- Prace nad interfejsem:\
    Interfej graficzny w opraciu o bibliotekę Tkinter zostanie wstępnie zaprojektowany i rozpoczęty na początku projektu. Po opracowaniu modułów zostanie z nimi zintegrowany, a także zostaną dostowowane okienka, aby użytkownik mógł intuicyjnie podawać odpowienie dane.
- Implementacja i wdrożenie:\
    Zostanie zintegrowane moduły do interfejsu graficznego, a także aplikacja zostanie "spakowana" do instalacji dla użytkownika w przystępny sposób.


## Ryzyka związane z projektem

- Opóźnienia związane z technologią\
Praca nad nową biblioteką (Tkinter), może przynieść niespodziewane przesunięcia w czasie. Istnieje zatem ryzyko, że zakładany czas na naukę oraz wdrożenie może okazać sięn iewystarczający.

- Problemy z integracją modułów\
Integracja modułów back-end-owych z front-endem również może być źródłem błędów i komplikacji. Możliwe, że integracja będzie wymagała więcej czasu, innego - nowego podejścia lub obsługi niewłaściwych danych.

- Testy\
Pomimo pozornego nieskomplikowania aplikacji, testy mogą ukazać niedopracowanie, błędy, obsługiwanie danych w niewłaściwy sposób, niepoprawną implementacje lub integrację modułów. Mogą spowodować kolejne opóźnienia lub przestoje.

- Zmiany projektowe\
Projekt może napotkać zmiany w zakresie planowanych funkcjonalności - chodźby ze względów na potrzebę dodanie niezbędnych elementów, które jeszcze nie zostały wykryte. Mogą wynikać z ponownej definicji założeń lub planów, czym mogą wpłynąć na czas i rozmiar prac.

## Kosztorys

#### Koszty osobowe

Zakładmy, że projekt zostanie wykonany przez jedną osobę:\
Stawka godzinowa: 50 PLN/h\
Czas pracy jest zadeklarowany w widełkach: 4-8 tygodni, 4-5 dni w tygodniu, 3-5 godzin dziennie - zatem szacowane koszty to:\
Minimalny koszt: 50 PLN/h * 3 h/dzień * 4 dni/tydzień * 4 tygodnie = 2 400 PLN\
Maksymalny koszt: 50 PLN/h * 5 h/dzień * 5 dni/tydzień * 8 tygodni = 10 000 PLN

#### Koszty sprzętowe
Zakup lub wynajem komputera spełniającego wymagania projektu:

Zakup nowego komputera: 1 500 - 2 000 PLN\
Wynajem komputera: 150 - 200 PLN/tydzień

#### Koszty wdrożenia
Zakładamy, że aplikacja zostanie wdrożona na platformie Windows, bez dodatkowych kosztów wdrożenia (brak potrzeby serwerów, czy dodatkowych usług).

Wszelakie koszty należy regularnie kontrolować i analizować postępy projektu względem zainwestowanych pieniędzy.

### Suma kosztów

Minimalna suma kosztów: 3 000 PLN\
Maksymalny suma kosztów: 12 000 PLN

## Przypadki użycia

Aktorem we wszystkich przypadkach użycia jest Użytkownik, który korzysta z aplikacji. Inicjuje on generowanie dokumentów, certyfikatów, konwersję do pdf-ów, edycję .txt i zmiany w ustawieniach.

1. Generowanie dokumentów:
    - Opis: Aktor wybiera szablony dokumentów oraz dane wejściwe. Aplikacja weryfikuje dane, wypełnia luki i eksportuje nowe pliki.
    - Zawiera: Wczytanie plików; Weryfikacja plików.
    - Rozszerza: Zapis nowych plików.

2. Generowanie certyfikatów:
    - Opis: Aktor wybiera szablon dokumentu oraz dane wejściwe. Aplikacja weryfikuje dane, wypełnia luki i eksportuje serie plików.
    - Zawiera: Wczytanie plików; Weryfikacja plików.
    - Rozszerza: Zapis nowych plików.

3. Konwersja na pdf:
    - Opis: Aktor wybiera dokumenty do konwersji. Aplikacja weryfikuje format, konwertuje i zapisuje nowe pliki.
    - Zawiera: Wczytanie plików; Weryfikacja formatu plików.
    - Rozszerza: Zapis nowych plików.

4. Edycja tekstowa:
    - Opis: Aktor otwiera plik tekstowy, dokonuje w nim zmian, a następnie zapisuje te zmiany.
    - Zawiera: Wczytanie pliku; Aktualizacje zawartości.

5. Zarządzanie ustawieniami aplikacji:
    - Opis: Aktor, poprzez panel ustawień aplikacji, dostosowuje  parametry działania programu, aby lepiej dopasować aplikację do swoich potrzeb.
    - Rozszerza: Modyfikację separatorów; Wybór rodzaju luk w plikach.

### Diagram przypadków użycia

![Diagram przypadków użycia](./Diagram.png)

## Strategia bezpieczeństwa

### Zasoby do ochrony

Elementy projektu, które należy chronić to:
- dane użytkowników. Obejmuje to ochronę plików szablonów, jak i danych osobowych używanych do ich uzupełnienia - szczególnie na etapie przetwarzania ich przez program; 
- integralność aplikacji. Aplikacja musi funkcjonować zgodnie z oczekiwaniami. Błędy nie mogą doprowadzać do nieporządanych ingerecji systemowych;
- dostępność. Wyłącznie użytkownicy uprawnieni powinni mieć dostęp do aplikacji.

### Potencjalne zagrożenia

Niewłaściwie opracowana aplikacja może generować następujące zagrożenia:
- udostępnianie przetwarzanych danych. Z racji dostępu do informacji niezbędych do pracy, istnieje ryzyko "wycieku" informacji poufnych.
- ingerencja z systemem użytkownika. Może następować szczególnie w momencie wystąpienia nieprzewidzianych i nieobsługiwanych błędów, co może powodować np. generowanie "śmieci".
- opóźnienia w dostępie do funkcjonalności. Nadmierne wykorzystywanie lub w sposób niezgodny z zaleceniami aplikacji może prowadzić do dłuższego oczekiwania na rezultaty.

### Koszty zabezpieczeń

Koszty związane są z: przeprowadzaniem testów bezpieczeństwa; poszukiwaniem luk i niedociągnieć w programie; wdrożeniem zabezpieczeń; utrzymywaniem oraz aktualizowaniem zabezpieczeń.

### Zyski z ochrony

Zyski to przede wszystkim zgodność z regulacjami o ochornie danych osobowych oraz zapewnienie sprawnego działanie aplikacji, co powinno przełożyć się na wzrost reputacji.


## Harmonogram testów

### Sposoby testowania poszczególnych modułów

1. Generowanie dokumentów
- Sprawdzenie pojedynczych funkcji odpowiedzialnych za wczytywanie plików, weryfikację danych, wypełnianie luk oraz zapis nowych plików.
- Upewnienie się, że wszystkie funkcje współpracują poprawnie, wczytując pliki, weryfikując dane, wypełniając luki i zapisując nowe pliki.
- Sprawdzenie poprawności wypełniania luk na różnych zestawach danych, w tym danych poprawnych oraz błędnych.
- Szacowany czas testów: 4 dni

2. Generowanie certyfikatów
- Sprawdzenie funkcji odpowiedzialnych za wczytywanie szablonu, weryfikację danych oraz generowanie wielu dokumentów.
- Upewnienie się, że proces generowania dokumentów działa poprawnie od początku do końca.
- Weryfikacja poprawności generowanych dokumentów przy użyciu różnych zestawów danych, w tym danych poprawnych oraz błędnych.
- Szacowany czas testów: 3 dni

3. Konwersja na pdf-y
- Sprawdzenie funkcji odpowiedzialnych za konwersję plików.
- Upewnienie się, że proces konwersji działa poprawnie, wczytując pliki .docx i zapisując pliki .pdf.
- Weryfikacja poprawności konwersji różnych dokumentów, w tym dokumentów z dużą ilością zawartości.
- Szacowany czas testów: 2 dni

4. Edytor tekstowy
- Sprawdzenie funkcji odpowiedzialnych za wczytywanie, edycję i zapis plików.
- Upewnienie się, że wszystkie funkcje edytora współpracują poprawnie.
- Weryfikacja poprawności edycji i zapisu plików.
- Szacowany czas testów: 2 dni

5. Zarządzanie ustawieniami aplikacji
- Sprawdzenie funkcji odpowiedzialnych za wczytywanie i zapisywanie ustawień.
- Upewnienie się, że zmiany ustawień wpływają na działanie aplikacji zgodnie z oczekiwaniami.
- Weryfikacja poprawności działania panelu ustawień ze zmienonymi konfiguracjami.
- Szacowany czas testów: 3 dni

### Przeprowadzanie testów

Testy będą przeprowadzane głównie przez wykonawce projektu, jako głównego dewelopera.
Harmonogram ich wykonywania będzie pokrywać się z planem realizacji projektu. Moduły będą sprawdzane po kolei oraz w połączeniu z kontrolowaniem wpływu ustawień aplikacji na dany moduł.
Na etapie testów końcowych, do testowania zostaną zaproszeni także użytkownicy, aby zapewnić obiektywność i wykrycie potencjalnych problemów z perspektywy końcowego użytkownika.

## Zabezpieczenia projektu

### Naturalny styk

- Intuicyjny interfejs: Interfejs użytkownika będzie zaprojektowany w sposób intuicyjny, z czytelnymi ikonami i jasnymi instrukcjami, np. okna dialogowe informujące o błędach będą jasno wskazywać, na źródło/obszar problemu.
- Samouczek: Aplikacja będzie zawierać okienko z opisem działania oraz użycia funkcjonalności wbudowanych w program. Dzięki jej pomocy użytkownicy będą mieć ułatwiony proces korzystania z aplikacji.

### Spójność pozioma i pionowa

- Jednolite zasady dostępu: Zasady dotyczące dostępu do wszystkich modułów i uprawnień będą spójne.

### Domyślna odmowa dostępu

- Walidacja danych wejściowych: Aplikacja będzie domyślnie odrzucać wszelkie nieznane lub niepoprawne dane wejściowe, np. użytkownik nie będzie w stanie wczytać plik o nieznanym formacie lub aplikacja odrzuci ten plik i powiadomi o błędzie.
