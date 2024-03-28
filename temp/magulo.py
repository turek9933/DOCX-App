from googlesearch import search

f_szkoly = open('szkoly.txt', 'r')
f_strony = open('strony.txt', 'w')
f_numery = open('numery.txt', 'w')
f_maile = open('maile.txt', 'w')

for szkola in f_szkoly:
    szkola = szkola[:-1]
    try:
        # Użyj Google do wyszukiwania adresów internetowych szkół
        query = f"strona internetowa {szkola}"
        results = search(query)
        # Wyświetl pierwszy wynik
        for result in results:
            f_strony.write(result + '\n')
            print(f"Nazwa szkoły: {szkola}, Adres strony internetowej: {result}")
            break
    except Exception as e:
        print(f"Błąd dla {szkola}: {str(e)}")

for szkola in f_szkoly:
    szkola = szkola[:-1]
    try:
        # Użyj Google do wyszukiwania numerów telefonów szkół
        query = f"Numer telefonu {szkola}"
        results = search(query)
        # Wyświetl pierwszy wynik
        for result in results:
            f_numery.write(result + '\n')
            print(f"Nazwa szkoły: {szkola}, Numer telefonu: {result}")
            break
    except Exception as e:
        print(f"Błąd dla {szkola}: {str(e)}")

for szkola in f_szkoly:
    szkola = szkola[:-1]
    try:
        # Użyj Google do wyszukiwania e-maili szkół
        query = f"e-mail {szkola}"
        results = search(query)
        # Wyświetl pierwszy wynik
        for result in results:
            f_maile.write(result + '\n')
            print(f"Nazwa szkoły: {szkola}, E-mail: {result}")
            break
    except Exception as e:
        print(f"Błąd dla {szkola}: {str(e)}")