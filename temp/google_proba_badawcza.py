from time import sleep
from tkinter import W
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googlesearch import search
import os

def szkoly():
    return [
        'Zespół Szkół Ponadgimnazjalnych Nr 3 w Malborku',
        'Zespół Szkół Ponadpodstawowych w Gryfinie',
        'Policealna Szkoła Zawodowa Meritum Sp. z o.o.',
        'Zespół Szkół Zawodowych w Węgierskiej Górce',
        'Zespół Szkół nr 1 w Mławie',
        'Zespół Szkół im Jana Koszczyca Witkiewicza w Kazimierzu Dolnym',
        'Centrum Kształcenia Zawodowego i Ustawicznego w Złotowie',
        'Zespół Szkół Zawodowych nr 2 im. kpt. Władysława Wysockiego w Białymstoku',
        'Zespół Szkół Ekonomiczno- Gastronomicznych w Żywcu',
        'Mazowiecka Wojewódzka Komenda Ochotniczych Hufców Pracy w Warszawie',
        'Zespół Szkół Nr 1 im. Mikołaja Kopernika w Ostrowcu Świętokrzyskim',
        'Zespół Szkół nr 4 im. Obrońców Mlawy z Września 1939r',
        'Centrum Wsparcia Rzemiosła, Kształcenia Dualnego i Zawodowego w Pile',
        'Zespół Szkół "Elektryk"  im. Noblistów Polskich w Słupsku',
        'Zespół Szkół Mechanicznych im. Stefana Czarnieckiego w Łapach',
        'Zespół Szkół w Brusach - Branżowa Szkoła I stopnia im. Kazimierza Sikorskiego',
        'Zespół Szkół Zawodowych Nr 3 im. Kardynała Stefana Wyszyńskiego',
        'Zespół Szkół w Sosnowcu Zakładu Doskonalenia Zawodowego w Katowicach',
        'Centrum Edukacji Ekonomiczno-Handlowej im. Karola Goduli',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Boninie',
        'Zespół Szkół Zawodowych Nr 1 im. 2 Warszawskiej Brygady Saperów i II Liceum Ogólnokształcące im. A. Frycza- Modrzewskiego',
        'Centrum Kształcenia i Wychowania Ochotnicze Hufce Pracy w Pleszewie',
        'STOWARZYSZENIE EDUKACJA-MŁODZIEŻ',
        'Europejskie Centrum Kształcenia i Wychowania OHP w Roskoszy',
        'Centrum Kształcenia i Wychowania OHP',
        'Zespół Szkół Ogólnokształcących i Technicznych w Ustce',
        'Zespół Szkół Ponadpodstawowych nr 3 im. W. S. Reymonta w Łowiczu',
        'Zespół Szkół Ponadpodstawowych im. Adama Mickiewicza w Lubaniu',
        'Centrum Kształcenia Zawodowego i Ustawicznego nr 1 w Raciborzu',
        'Cech Rzemiosł Różnych i Przedsiębiorczości w Katowicach',
        'Zespół Szkół Ponadpodstawowych w Białobrzegach',
        'Zespół Szkół Gastronomiczno-Hotelarskich im. Marii Sklodowskiej-Curie',
        'Zespół Szkół Zawodowych nr 2 im. Powstańców Warszawy w Mińsku Mazowieckim',
        'Zespół Szkół Zawodowych im. Stanisława Staszica w Wysokiem Mazowieckiem',
        'Zespół Szkół im. Marii Sklodowskiej-Curie w Działoszynie',
        'Zespół Szkół Nr 1 im. Marii Skłodowskiej- Curie w Wyszkowie',
        'Zespół Szkół Zawodowych w Jastrzębiu- Zdroju',
        'Fundacja "Mądra Europa"',
        'Zespół Szkół Zawodowych nr 1 im. Komisji Edukacji Narodowej w Białej Podlaskiej',
        'Zs nr 1 im. KEN Szczecinek',
        'Zespół Szkół Nr 2 im. Stanisława Konarskiego w Bochni',
        'Centrum Kształcenia Zawodowego i Ustawicznego nr 1 w Warszawie',
        'Zespól Szkół im. Armii Krajowej Obwodu Głuszec-Grójec w Grójcu',
        'Zespół Szkół Ogólnokształcących i Zawodowych im. Bohaterów Monte Cassino w Lubniu',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Jadwigi Dziubinskiej w Goladkowie',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Hańczowej',
        'Zespół Szkół Centrum Kształcenia Rolniczego im Władysława Stanisława Reymonta w Radomiu',
        'Zespół Szkół Rolniczych im. W. Witosa w Ostrożanach',
        'Zespół Szkół Zawodowych im. sw. Jadwigi Królowej w Bieczu',
        'Zespół Szkół Ekonomicznych im Jana Pawła II w Gorlicach',
        'Fundacja "Rodzice Szkole"',
        'Zgierski Zespół Szkół Ponadpodstawowych im. Jana Pawła II w Zgierzu',
        'Zespół Szkół Centrum Kształcenia Praktycznego w Sochaczewie',
        'Technikum nr 15 im. Marii Skłodowskiej- Curie',
        'Zespół Szkół Zawodowych nr 2 im. Marii Dąbrowskiej w Dęblinie',
        'Zespół Szkół i Placówek im. W. Witosa w Bolkowie',
        'Zespół Szkół nr 2 im. Eugeniusza Kwiatkowskiego w Nowej Dębie',
        'Zespół Szkół im. Władysława Stanisława Reymonta w Brniu',
        'Zespół Szkół Ponadpodstawowych nr 1 w Piotrkowie Trybunalskim',
        'Zespół Szkół Zawodowych nr 2 im. Leona Wyczółkowskiego',
        'Małopolskie Centrum Edukacji Sp. z o. o.',
        'Zespół Szkół  nr 8 im. Stanisława Staszica w Szczecinie',
        'Zespół Szkół  Centrum Kształcenia Rolniczego im. prof. Władysława Szafera w Rzemieniu',
        'Zespół Szkół  Politechnicznych w Głogowie',
        'Zespół Szkół  Ekonomicznych im. Mikołaja Kopernika',
        'Wojewódzki Zakład Doskonalenia Zawodowego w Szczecinie',
        'Zespół Szkół  w Brusach - Branżowa Szkół a I stopnia im. Kazimierza Sikorskiego w Brusach',
        'Zespół Szkół Przemysłu Spożywczego im. J. Rymera - I Wojewody Śląskiego',
        'Zespół Szkół  Centrum Kształcenia Rolniczego w Powierciu',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Jadwigi Dziubińskiej w Zduńskiej Dąbrowie',
        'Zespól Szkół  Rolnicze Centrum Kształcenia Ustawicznego im. Stanisława Staszica w Kościelcu',
        'Zespół Szkół Ponadgimnazjalnych Nr 3 w Malborku',
        'Zespół Szkół  i Placówek Oświatowych w Skale',
        'Zespół Szkół Nr 2 im. Wojciecha Korfantego w Jastrzębiu-Zdroju',
        'Zespół Szkół Ponadgimnazjalnych im. W. Broniewskiego w Krośnie Odrzańskim',
        'Zespół Szkół  nr 6',
        'Zespół Szkół  nr 2 im. Władysława Jagiełły w Mrągowie',
        'Zespół Szkół  Nr 2 im. Tadeusza Kościuszki w Stalowej Woli',
        'Zespół Szkół im. bł. ks. Piotra Dankowskiego w Jordanowie',
        'Zespół Szkół  Ponadpodstawowych im. Jana Pawła II w Krynicy-Zdroju',
        'Zespół Szkół  Centrum Kształcenia Praktycznego w Sochaczewie',
        'Zespół Szkół  im. T. Kościuszki',
        'Zespół Szkół Nr 1 im. Mikołaja Kopernika w Ostrowcu Świętokrzyskim, os. Słoneczne 33',
        'Zespół Szkół  Nr 3 im. Kombatantów RP',
        'Zespół Szkół Rolnicze Centrum Kształcenia Ustawicznego im. Ziemi Kujawskiej',
        'Zespół Szkół Samochodowych i Licealnych Nr 3 im. Ignacego Jana Paderewskiego',
        'Zespół Szkół  Zawodowych im. Stanisława Staszica i Centrum Kształcenia Ustawicznego',
        'Policealna Szkół a Zawodowa Meritum Sp. z o.o.',
        'Specjalny Ośrodek Szkół no-Wychowawczy im. Janusza Korczaka w Mosinie',
        'Zespół Szkół Zawodowych im. ppor. E. Gierczak w Górze Kalwarii',
        'Zespół Szkół  w Świątnikach Górnych',
        'Zespół Szkół Nr 3 im. Walentego Lipińskiego i Mateusza Beksińskiego w Sanoku',
        'Zespół Szkół Spożywczych Chemicznych i Ogólnokształcących w Jarosławiu',
        'Zespół Szkół Zawodowych Towarzystwa Salezjańskiego w Oświęcimiu',
        'Zespół Szkół  im. Stanisława Staszica',
        'Zespół Szkół nr 2 im. L. Skowyry w Przysusze',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Jadwigi Dziubińskiej w Golądkowie',
        'Niepubliczne Technikum im. Wojska Polskiego w Starachowicach Zakladu Doskonalenia Zawodowego w Kielcach',
        'Zespól Szkół  im. Armii Krajowej Obwodu Głuszec- Grójec w Grójcu',
        'Zespół Szkół  Przemysłu Spożywczego',
        'Kłodzka Szkół a Przedsiębiorczości',
        'Zespół Szkół im. Marii Grodzickiej w Lubrańcu Marysinie',
        'Zespół Szkół Politechnicznych Energetyk w Wałbrzychu',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Józefa Piłsudskiego w Okszowie',
        'Zespół Szkół im. Emilii Sukertowej-Biedrawiny w Malinowie',
        'Schools Agricultural Training Centre in Potoczek',
        'Zespół Szkół Ponadgimnazjalnych w Blaszkach',
        'Zespół Szkół Ekonomiczno-Gastronomicznych w Żywcu',
        'Zespół Szkół Ekonomicznych im. Jana Pawła II w Złotowie',
        'Stowarzyszenie EDUKACJA - MŁODZIEŻ',
        'Niepubliczne Technikum Zawodowe w Nowym Mieście nad Pilica Zakładu Doskonalenia Zawodowego w Kielcach',
        'Powiat Świdnicki w Świdniku / Powiatowe Centrum Edukacji Zawodowej im. Zygmunta Puławskiego w Świdniku',
        'Zespół Szkół Nr 1 w Mlawie',
        'Zespół Szkół  nr 4 im. Obrońców Mławy z września 1939r w Mławie',
        'Zespół Szkół  im. Stanisława Staszica w Gąbinie',
        'Zespół Szkół "Elektryk" im. Noblistów Polskich w Słupsku',
        'Zespół Szkół  Ogólnokształcących i Zawodowych im. Bohaterów Monte Cassino w Lubniu',
        'The Centre of Supporting Crafts, Dual and Vocational Education in Pila',
        'Zespół Szkół  Zawodowych nr 2 im. Powstańców Warszawy w Mińsku Mazowieckim',
        'Podlaska Wojewódzka Komenda Ochotniczych Hufców Pracy w Białymstoku',
        'Zespół Szkół Zawodowych nr 2 im. Marii Dąbrowskiej w Dęblinie',
        'Kujawsko-Pomorska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół Ponadgimnazjalnych nr 1 im. Stanisława Staszica w Siedlcach',
        'Zespół Szkół Ekonomicznych im. W. Stysia w Świdnicy',
        'Regionalne Centrum Edukacji Zawodowej w Bilgoraju',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Stanisława Szumca w Bielsku-Białej',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Swarożynie',
        'Zespół Szkół  nr 1 im. K.K. Baczyńskiego w Sokołowie Podlaskim',
        'Zespół Szkół im. Marii Skłodowskiej-Curie w Działoszynie',
        'Fundacja Kształcenia Zawodowego i Międzykulturowego Faveo',
        'Centrum Kształcenia i Wychowania Ochotniczych Hufców Pracy w Oleśnicy',
        'Zespół Szkół im Jana Koszczyca Witkiewicza w Kazimierzu Dolnym',
        'Zespół Szkół Zawodowych w Jastrzębiu-Zdroju',
        'Fundacja "Rodzice Szkół e"',
        'Zespół Szkół  Elektronicznych im. Bohaterów Westerplatte',
        'Związek Młodzieży Wiejskiej',
        'Zespół Szkół Ogólnokształcących i Technicznych w Ustce',
        'Zakład Doskonalenia Zawodowego w Toruniu',
        'Zespół Szkół Technicznych w Płocku',
        'Mazowiecka Wojewódzka Komenda Ochotniczych Hufców Pracy w Warszawie',
        'Zespół Szkół im. bl. ks. Piotra Dankowskiego w Jordanowie',
        'Zespół Szkół nr 8 im. Stanisława Staszica w Szczecinie',
        'Zespół Szkół Zawodowych im. ppor. E. Gierczak w Górze Kalwarii',
        'Zespół Szkół Nr 2 im. Wojciecha Korfantego w Jastrzębiu- Zdroju',
        'Zespół Szkół Gastronomicznych im. Marii Skłodowskiej- Curie w Częstochowie',
        'Zespół Szkół Politechnicznych w Głogowie',
        'Instytut Głuchoniemych im. Jakuba Falkowskiego',
        'Zespół Szkół im ks. dra Jana Zwierza',
        'Centrum Edukacji Ekonomiczno-Handlowej im. Karola Goduli w Tarnowskich Górach',
        'Centrum Kształcenia Zawodowego Nr 1 w Warszawie',
        'Zespół Szkół Ekonomicznych im. Jana Pawła II w Złotowie',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Boninie',
        'Zespół Szkół nr 2 im. Władysława Jagiełły w Mrągowie',
        'Technikum nr 15 im. Marii Skłodowskiej-Curie',
        'Zespół Szkół Politechnicznych Energetyk w Wałbrzychu',
        'Zespół Szkół Ponadpodstawowych w Białobrzegach',
        'Zespół Szkół nr 2 w Golubiu-Dobrzyniu',
        'Zespół Szkół Budowlanych w Rybniku',
        'Zespół Szkół Nr 2 w Żyrardowie',
        'Zespół Szkół Ponadgimnazjalnych nr 2 im. Mikołaja Kopernika w Siedlcach',
        'Zespół Szkół Zawodowych Nr 1 im. mjr. Henryka Dobrzańskiego w Bychawie',
        'Zespół Szkół Ekonomicznych im. Jana Pawła II w Głogowie',
        'Technikum Leśne w Tucholi im. Adama Loreta',
        'Zespół Szkół Rolniczo-Technicznych',
        'Zespół Szkół Zawodowych Towarzystwa Salezjańskiego w Oświęcimiu',
        'Zespół Szkół nr 4 im. Piotra Latoski w Rudzie Śląskiej',
        'ZESPÓŁ SZKÓŁ IM. STANISLAWA STASZICA W GABINIE',
        'DELTA - WIEDZA EDUKACJA ROZWÓJ',
        'Zespół Szkół Technicznych i Ogólnokształcących im. Stefana Żeromskiego w Częstochowie',
        'Policealna Szkoła Zawodowa Meritum Sp. z o.o.',
        'Zakład Doskonalenia Zawodowego',
        'Zespół Szkół Zawodowych Nr 1 im. gen. Franciszka Kleeberga w Dęblinie',
        'Zespół Szkół Łączności W Warszawie',
        'Zespół Szkół Zawodowych Nr 1 im. 2 Warszawskiej Brygady Saperów i II Liceum Ogólnokształcące im. A. Frycza-Modrzewskiego we Włodawie',
        'Zespól Szkół Rolnicze Centrum Kształcenia Ustawicznego im. Stanisława Staszica w Kościelcu',
        'Zespół Szkół Licealnych im. B. Chrobrego w Leżajsku',
        'Wojewódzki Zakład Doskonalenia Zawodowego w Szczecinie',
        'Zespół Szkół Zawodowych Nr 2 im. kpt. Władysława Wysockiego w Białymstoku',
        'ZESPÓŁ SZKÓŁ NR1 W MLAWIE',
        'Zespół Szkół Nr 2 im. Tadeusza Kościuszki w Stalowej Woli',
        'Zs nr1 im. KEN Szczecinek',
        'Zespół Szkół nr4 im. Obrońców Mlawy z września 1939r w Mlawie',
        'Zespól Szkół nr 2 im. Ludwika Skowyry w Przysusze',
        'Zespół Szkół Zawodowych nr 1 im. Komisji Edukacji Narodowej w Białej Podlaskiej',
        'Zespół Szkół Mechanicznych im. Stefana Czarnieckiego w Lapach',
        'Zespół Szkół Rolniczych Centrum Kształcenia Zawodowego w Pszczelej Woli',
        'Zespół Szkół w Brusach - Branżowa Szkoła I stopnia im. Kazimierza Sikorskiego w Brusach',
        'Zespół Szkół Ponadpodstawowych im. Jana Pawła II w Krynicy - Zdroju',
        'Technikum im. Stanisława Konarskiego w Nowym Mieście nad Pilicą Zakładu Doskonalenia Zawodowego w Kielcach',
        'Zespół Szkół Budowlanych im. Jurija Gagarina w Bydgoszczy',
        'Zespół Szkół Zawodowych im. Stanisława Staszica w Wysokiem Mazowieckiem',
        'Zespół Szkół w Stoczku Łukowskim',
        'Zespół Szkół nr 2 w Mlawie',
        'Zespół Szkół Gastronomicznych i Handlowych w Bielsku- Białej',
        'A team of technical schools in Wloclawek',
        'Zespół Szkół Ekonomicznych im. W. Stysia w Świdnicy',
        'Zespół Szkół i Placówek im. W. Witosa w Bolkowie',
        'Europejskie Centrum Kształcenia i Wychowania OHP w Roskoszy',
        'Zespół Szkół im. Władysława Stanisława Reymonta w Brniu',
        'Zespół Szkół Technicznych i Ogólnokształcących nr 3 im. Edwarda Abramowskiego',
        'Zespół Szkół Zawodowych w Węgierskiej Gorce',
        'Powiatowy Zespół Szkół nr 2 im. K. Miarki',
        'Zakład Doskonalenia Zawodowego w Warszawie',
        'Zespół Szkół nr 1 im. K.K. Baczyńskiego w Sokołowie Podlaskim',
        'Centrum Kształcenia Zawodowego i Ustawicznego nr 1 w Raciborzu',
        'Zespół Szkół Nr 2 im. Stanisława Konarskiego w Bochni',
        'Zespół Szkół im. Ks. Kard. Stefana Wyszyńskiego w Karczewie',
        'Centrum Kształcenia Zawodowego i Ustawicznego w Złotowie',
        'Powiatowy Zespół Nr 4 Szkół Ekonomiczno- Gastronomicznych w Oświęcimiu',
        'Zespół Szkół Centrum Kształcenia Rolniczego im Władysława Stanisława Reymonta w Radomiu',
        'Zespół Szkół Centrum Kształcenia Praktycznego w Sochaczewie',
        'ZSP im. Jana Kochanowskiego w Węgrowie',
        'Zespół Szkół Samochodowych',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Wincentego Witosa w Różańcu',
        'Centrum Wsparcia Rzemiosła, Kształcenia Dualnego i Zawodowego',
        'Zespół Szkół Ekonomicznych im. M. Skłodowskiej- Curie w Rzeszowie',
        'Małopolska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół w Świątnikach Górnych',
        'Zespół Szkół im. Emilii Sukertowej - Biedrawiny w Malinowie',
        'Urząd Marszałkowski Województwa Dolnośląskiego',
        'Internationaler Bund Polska',
        'Fundacja Efekt Motyla',
        'Zachodniopomorska Wojewódzka Komenda Ochotniczych Hufców Pracy w Szczecinie',
        'Zespół Szkół Technicznych i Ogólnokształcących im. ks. Edmunda Domańskiego w Iłowie-Osadzie',
        'Zespół Szkół w Sosnowcu Zakładu Doskonalenia Zawodowego w Katowicach',
        'Zespół Szkół Spożywczych i Biznesowych im. Marii Curie - Skłodowskiej w Jarosławiu',
        'Zespół Szkół nr 5 im. Karola Brzostowskiego',
        'Zespół Szkół Ekonomicznych im Jana Pawła II w Gorlicach',
        'Zespół Szkół Budowlanych im Kazimierza Wielkiego w Szczecinie',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Ziemi Sandomierskiej w Sandomierzu-Mokoszynie',
        'Zespół Szkół Nr 3 im. Kombatantów RP',
        'Zespół Szkół Ekonomicznych w Zawierciu',
        'Zespół Szkół "Elektryk" im. Noblistów Polskich w Słupsku',
        'Fundacja Możesz Więcej',
        'Centrum Kształcenia Zawodowego i Ustawicznego Nr 1 w Gdańsku',
        'Zespół Szkół Zawodowych i Ogólnokształcących im 29 Pułku Piechoty 2 Armii Wojska Polskiego',
        'Centrum Kształcenia Zawodowego i Ustawicznego w Sosnowcu ul. Grota Roweckiego 64',
        'Zespół Szkół im. Jarosława Iwaszkiewicza',
        'Zespół Szkół Ponadpodstawowych im. Adama Mickiewicza w Lubaniu',
        'Zespół Szkół Rolnicze Centrum Kształcenia Ustawicznego im. Bohaterów Walk nad Bzurą 1939 r. w Sochaczewie',
        'Zespół Szkół Zawodowych im. Stanisława Staszica i Centrum Kształcenia Ustawicznego w Ostrodzie',
        'Zespół Szkół  nr 3 w Tarnobrzegu',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. prof. Władysława Szafera w Rzemieniu',
        'Zespół Szkół nr 3 w Rudzie Śląskiej',
        'Cech Rzemiosł Różnych i Przedsiębiorczości w Katowicach',
        'Zespół Szkół im. Marii Skłodowskiej-Curie, ul. Kolejowa 2, 58-310 Szczawno-Zdrój',
        'Zespół Szkół Zawodowych i Licealnych w Zgorzelcu',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Hańczowej',
        'Wielkopolska Izba Rzemieślnicza w Poznaniu',
        'Fundacja Regionalne Centrum Kompetencji',
        'Perfect Project Spółka z ograniczona odpowiedzialnością',
        'Centrum Wsparcia Rzemiosła, Kształcenia Dualnego i Zawodowego w Kaliszu',
        'EDU-IT Augustyn, Pieprzycki spółka jawna',
        'Powiatowe Centrum Kształcenia Zawodowego i Ustawicznego w Chodczu',
        'Zespół Szkół Zawodowych nr 2 im. Leona Wyczółkowskiego',
        'Zespół Szkół im. T. Kościuszki',
        'Zespół Szkół Mechanicznych 3',
        'Zespół Szkół Ponadgimnazjalnych nr 2 w Nowej Soli',
        'NIEPUBLICZNE TECHNIKUM IM. WOJSKA POLSKIEGO W STARACHOWICACH ZAKŁADU DOSKONALENIA ZAWODOWEGO W KIELCACH',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Jadwigi Dziubińskiej w Golądkowie',
        'Zespół Szkół Powiatowych w Drzewicy',
        'Zespół Szkół im. Marii Grodzickiej w Lubrańcu Marysinie',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Jadwigi Dziubińskiej w Zduńskiej Dąbrowie',
        'Zespół Szkół Elektronicznych im. Bohaterów Westerplatte',
        'Zespół Szkół Budowlanych im. Kazimierza Wielkiego w Radomiu',
        'ZSZ_Nr6_Poznan',
        'Zespół Szkół Przemysłu Spożywczego im. J. Rymera - I Wojewody Śląskiego',
        'Zespół Szkół Ponadpodstawowych w Gryfinie',
        'Technikum Nr 3 w Malborku',
        'Zespół Szkół Technicznych i Ogólnokształcących im. Kazimierza Gzowskiego w Opolu',
        'Zespół Szkół Mechanicznych',
        'Zespół Szkół Zawodowych nr 2 im. Marii Dąbrowskiej w Dęblinie',
        'Powiat Sokólski',
        'Instytut Inicjatyw Społecznych',
        'Zespół Szkół im. Marii Skłodowskiej-Curie w Działoszynie',
        'Zespół Szkół Zawodowych nr 2 im. Powstańców Warszawy w Mińsku Mazowieckim',
        'Świętokrzyska Wojewódzka Komenda Ochotniczych Hufców Pracy w Kielcach',
        'Niepubliczne Technikum Zawodowe w Końskich Zakładu Doskonalenia Zawodowego w Kielcach',
        'Zespół Szkół Zawodowych im. św. Jadwigi Królowej w Bieczu',
        'Państwowe Szkoły Budownictwa im. prof. Mariana Osińskiego',
        'Centrum Kształcenia i Wychowania Ochotnicze Hufce Pracy w Pleszewie',
        'Powiatowy Zespół Szkół w Blaszkach',
        'Zespół Szkół Technicznych im. E. Kwiatkowskiego',
        'Zespół Szkół nr 1 im. Powstańców Wielkopolskich w Ostrzeszowie',
        'Zespół Szkół Ponadpodstawowych nr 1 w Piotrkowie Trybunalskim',
        'Zespół Szkół Technicznych i Ogólnokształcących im. prof. Z. Strzeleckiego w Sandomierzu',
        'Zespół Szkół Ogólnokształcących i Zawodowych im. Bohaterów Monte Cassino w Lubniu',
        'Zespół Szkół Technicznych w Częstochowie',
        'Centrum Wsparcia Rzemiosła, Kształcenia Dualnego i Zawodowego w Pile',
        'Zespół Szkół Elektrycznych im. prof. Janusza Groszkowskiego w Białymstoku',
        'Podlaska Wojewódzka Komenda Ochotniczych Hufców Pracy w Białymstoku',
        'ZESPÓŁ SZKÓŁ IM. GEN. TADEUSZA KUTRZEBY',
        'Zespół Szkół w Mszczonowie',
        'FUNDACJA PIĘĆ PLUS',
        'Fundacja Zawodowiec',
        'STOWARZYSZENIE EDUKACJA - MLODZIEZ',
        'Zwiazek Młodzieży Wiejskiej',
        'Zespół Szkół Ekonomiczno-Gastronomicznych w Zywcu',
        'Zespół Szkół Ponadpodstawowych Nr 1 im. 10 Pułku Piechoty w Łowiczu',
        'Zespół Szkół nr 1 im. K. Adamieckiego w Sanoku',
        'Zespół Szkół Ponadpodstawowych nr 3 im. W. S. Reymonta w Łowiczu',
        'Polsko-Niemiecka Współpraca Młodzieży',
        'Fundacja Kształcenia Zawodowego i Miedzykulturowego Faveo',
        'Zespół Szkół Nr 3 im. Walentego Lipińskiego i Mateusza Beksińskiego w Sanoku',
        'Zespół Szkół nr 5 im. Tadeusza Tańskiego',
        'Flying Colours Sp. z o.o.',
        'Centrum Kształcenia i Wychowania Ochotniczych Hufców Pracy w Oleśnicy',
        'Zespół Szkół nr 1 w Tarnobrzegu',
        'Zespół Szkół Ponadpodstawowych nr 1 w Zamościu',
        'Zespół Szkół w Dowspudzie',
        'Fundacja Centrum Edukacji i Przedsiębiorczości Obywatelskiej',
        'Lubelska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Krajowy Sekretariat Przemysłu Chemicznego NSZZ "SOLIDARNOŚĆ"',
        'Zgierski Zespół Szkół Ponadpodstawowych im. Jana Pawła II w Zgierzu',
        'Fundacja Ku Pomocy',
        'Zespół Szkół Nr 9 im. dr Mikołaja Witczaka',
        'Zespól Szkół im. Armii Krajowej Obwodu Głuszec-Grojec w Grojcu',
        'Zespół Szkół Techniczno-Branżowych w Jastrzębiu-Zdroju',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Augusta Zamoyskiego w Jabłoniu',
        'Zespół Szkół Ponadpodstawowych im. Wincentego Witosa w Nawojowej',
        'Zespół Szkół Ekonomicznych im. Cyryla Ratajskiego',
        'Zespół Szkół Elektronicznych i Ogólnokształcących',
        'Zespół Szkół Turystyczno-Gastronomicznych w Mińsku Mazowieckim',
        'Zespół Szkół nr 1 im. Bohaterów Westerplatte w Garwolinie',
        'Zespół Szkół Ponadpodstawowych nr 1 w Krotoszynie',
        'Centrum Wsparcia Rzemiosła, Kształcenia Dualnego i Zawodowego w Poznaniu',
        'Zespół Szkół Zawodowych',
        'Zespół Szkół nr 1 im Bartłomieja z Bydgoszczy w Bydgoszczy',
        'Zespól Szkól Ponadpodstawowych nr 2 Centrum Kształcenia Zawodowego im. Tadeusza Kościuszki w Łowiczu',
        'Zespół Szkół w Czchowie',
        'Zespół Szkół Ponadpodstawowych Nr 1 im. 10 Pułku Piechoty w Łowiczu',
        'Technikum nr 1 w Zespole Szkół im. Adama Mickiewicza w Lublińcu',
        'Zespół Szkół nr 1 im. K.K. Baczyńskiego w Sokołowie Podlaskim',
        'Zespół Szkół Nr 2 im. prof. Tadeusza Kotarbińskiego w Dzierżoniowie',
        'Zespół Szkół Technicznych i Branżowych im. Bohaterów Westerplatte w Brzesku',
        'Bronislaw Rutkowski Primary and Secondary Music School',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Osadników Wojskowych w Mieszkowicach',
        'ZESPÓŁ SZKÓŁ POWIATOWYCH W PRZASNYSZU',
        'Dolnośląski Zespół Szkół w Biedrzychowicach',
        'Zespół Szkół im. Hugona Kołłątaja w Jordanowie',
        'Zespół Szkół Gastronomicznych im. prof. Eugeniusza Pijanowskiego',
        'Zespół Szkół w Kowalewie Pomorskim',
        'Branżowa Szkoła I Stopnia w Zarkach Zakładu Doskonalenia Zawodowego w Katowicach',
        'Zespół Szkół Mechanicznych Centrum Kształcenia Praktycznego Nr 2 im. św. Józefa',
        'Zespół Szkół Chemicznych im. Ignacego Łukasiewicza',
        'Zespół Szkół Ponadpodstawowych w Niemcach',
        'Zespół Szkół Budowlanych im. gen. Stefana Grota Roweckiego w Cieszynie',
        'Niepubliczne Technikum Zawodowe w Nowym Mieście nad Pilica Zakładu Doskonalenia Zawodowego w Kielcach',
        'Niepubliczne Technikum im 72 Pułku Piechoty w Radomiu Zakładu Doskonalenia Zawodowego w Kielcach',
        'Zespół Szkół Zawodowych Nr 2',
        'Zespół Szkół Techniczno-Zawodowych im. Macieja Rataja w Tomaszowie Lubelskim',
        'Zespół Szkół Zawodowych i Ogólnokształcących w Sulkowicach',
        'Perfect Project Sp. z o.o.',
        'Zespół Szkół Techniczno-Weterynaryjnych',
        'Zespół Szkół im. Władysława Stanisława Reymonta w Malaszewiczach',
        'Zespół Szkół Rolniczych im. Biskupa Ignacego Błażeja Krasickiego',
        'Zespół Szkół im. gen. Sylwestra Kaliskiego w Górze',
        'Fundacja Centrum Edukacji i Przedsiębiorczości Obywatelskiej',
        'Zespół Szkół nr. 14',
        'Technikum nr 18',
        'Zespół Szkół Nr 1 w Piasecznie',
        'Zespół Szkół Technicznych im. Hipolita Cegielskiego w Śremie',
        'Zespół Szkół nr 1 w Hrubieszowie',
        'Zespół Szkół Nr 2 im. prof. Janusza Groszkowskiego',
        'Zespół Szkół Zawodowych i Ogólnokształcących im. I Brygady Pancernej im. Bohaterów Westerplatte w Kartuzach',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Kamieniu Małym',
        'Zespół Szkół Rolniczych Centrum Kształcenia Zawodowego w Pszczelej Woli',
        'Zespół Szkół im. Macieja Rataja w Reszlu',
        'Zespół Szkół Zawodowych im. Stanisława Staszica w Barlewiczkach',
        'Zespół Szkół im. Stanisława Staszica',
        'Centrum Kształcenia Zawodowego i Ustawicznego w Sosnowcu ul. Grota Roweckiego 64',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. prof. Władysława Szafera w Rzemieniu',
        'Zespół Szkół Gastronomicznych w Częstochowie',
        'Zespół Szkół Ekonomiczno-Handlowych im. Polaków spod Znaku Rodła',
        'Zespół Szkół Zawodowych i Ogólnokształcących im 29 Pułku Piechoty 2 Armii Wojska Polskiego',
        'Zespół Szkół Ekonomiczno-Gastronomicznych',
        'TEB Jelenia Góra',
        'Zespół Szkół im. Krzysztofa Celestyna Mrongowiusza w Olsztynku',
        'Fundacja Kształcenia Zawodowego i Międzykulturowego Faveo',
        'Zespół Szkół Ekonomicznych Nr 2 im. I. Daszyńskiego w Krakowie',
        'Katolickie Stowarzyszenie Oświatowe',
        'Zespół Szkół nr 2 w Koluszkach',
        'Powiatowy Zespół Szkół',
        'Powiatowy Zespol Nr 4 Szkol Ekonomiczno-Gastronomicznych w Oświecimiu',
        'Zespół Szkół nr 2 w Łosicach',
        'Zespół Szkół nr 5 im. Jana Pawła II',
        'Zespół Szkół Rolniczych',
        'Zespół Szkół  Ponadpodstawowych im. Jana Pawła II w Krynicy - Zdroju',
        'CENTRUM KSZTAŁCENIA "NAUKA" SP Z O.O.',
        'Powiatowy Zespół Szkół w Złoczewie',
        'Technikum TEB Edukacja we Wrocławiu',
        'Powiatowy Zespół Szkół nr 2 w Rumi',
        'Zespół Szkół Chemicznych i Ogólnokształcących im. Jędrzeja Śniadeckiego w Olsztynie',
        'Zespół Szkół Zawodowych im. ppor. E. Gierczak w Górze Kalwarii',
        'Centrum Wsparcia Rzemiosła, Kształcenia Dualnego i Zawodowego w Lesznie',
        'ZESPÓŁ SZKÓŁ PONADGIMNAZJALNYCH W ZAGANIU',
        'Zespół Szkół Ponadgimnazjalnych nr 4',
        'Zespół Szkół Zawodowych im. Kazimierza Pułaskiego',
        'Zespół Szkół Rolnicze Centrum Kształcenia Ustawicznego',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Augustyna Suskiego w Nowym Targu',
        'Technikum TEB Edukacja w Gliwicach',
        'Zespół Szkół Ponadpodstawowych nr 6 w Tomaszowie Mazowieckim',
        'Zespół Szkół Elektronicznych im. Bohaterów Westerplatte',
        'Warmińsko-Mazurska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół Technicznych im. płk Gwido Langera Cieszynie',
        'ZESPÓŁ SZKÓŁ PONADGIMNAZJALNYCH NR 1 IM. STANISŁAWA STASZICA W SIEDLCACH',
        'Zespół Szkół Zawodowych im. Kardynała Stefana Wyszyńskiego w Dynowie',
        'Zespół Szkół Nr 3 im. S. Staszica',
        'Powiatowe Centrum Kształcenia Zawodowego i Ustawicznego w Lubieńcu',
        'ZESPÓŁ SZKÓŁ CENTRUM KSZTAŁCENIA ROLNICZEGO W WIDZEWIE',
        'Zespół Szkół nr 17 w Zabrzu',
        'Zespół Szkół Mechaniczno-Elektrycznych',
        'Centrum Kształcenia i Wychowania Ochotniczych Hufców Pracy w Oleśnicy',
        'Zespół Szkół Spożywczych Chemicznych i Ogólnokształcących w Jarosławiu',
        'Zespół Szkół Ponadpodstawowych im. Ks. Janusza St. Pasierba w Żabnie',
        'Zespół Szkół Liczności w Gliwicach',
        'Zespół Szkół im. Bohaterów Września 1939r. w Iławie',
        'Zespół Szkół Technicznych i Ogólnokształcących im. prof. Z. Strzeleckiego w Sandomierzu',
        'Zespół Szkół Ponadpodstawowych w Pszowie',
        'Zespół Szkół w Cieszynie Zakładu Doskonalenia Zawodowego w Katowicach',
        'Urzad Marszalkowski Wojewodztwa Dolnośląskiego',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Wincentego Witosa w Samostrzelu',
        'Fundacja NOVA',
        'Zespół Szkół Zawodowych im. Sandora Petofi w Ostródzie',
        'Zespół Szkół Zawodowych im. Stanisława Staszica i Centrum Kształcenia Ustawicznego',
        'WOLF SECURTY TOMASZ ZEGAN',
        'Zespół Szkół Nr1 w Ostrowi Mazowieckiej',
        'Zespół Szkół Samochodowych i Licealnych Nr 3 im. Ignacego Jana Paderewskiego',
        'Specjalny Ośrodek Szkolno-Wychowawczy im. Janusza Korczaka w Mosinie',
        'Zespół Szkół Mechanicznych nr 4, im. Gen. A.E. Fieldorfa "Nila"',
        'Zespół Szkół Centrum Kształcenia Rolniczego w Szczecinie',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Szkoły Podchorążych Piechoty w Komorowie w Starym Lubiejewie',
        'Zespół Szkół Budowlano-Geodezyjnych im. S.W. Bryły w Białymstoku',
        'Zespół Szkół  im. Marii Skłodowskiej-Curie, ul. Kolejowa 2, 58-310 Szczawno-Zdrój',
        'Zespół Szkół Rzemiosła im. Jana Kilińskiego',
        'Zespół Szkół Gastronomiczno -Usługowych im. M. Dąbrowskiej',
        'Zespół Szkół nr 2 im. Adama Mickiewicza',
        'Zespół Szkół im. Jana Kasprowicza w Sztumie',
        'Zespół Szkół Zawodowych im. Elizy Orzeszkowej',
        'Zespół Szkół im. gen. Władysława Andersa w Częstochowie',
        'Zespół Szkół Skórzano-Odzieżowych, Stylizacji i Usług',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Wincentego Witosa w Suwałkach',
        'Ochotnicze Hufce Pracy Centrum Kształcenia i Wychowania w Gołdapi',
        'Powiatowy Zespół Szkół nr 2 im. Komisji Edukacji Narodowej',
        'Zespół Szkół Samochodowych im. Obrońców Westerplatte',
        'Ludzka Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'TECHNICZNE ZAKLADY NAUKOWE',
        'Zespół Szkół Zawodowych Nr 2 im. dr A. Troczewskiego',
        'SZKOLY EKONOMICZNO-HANDLOWE IM.MACIERZY SZKOLNEJ W GDANSKU',
        'Zespół Szkół Ogólnokształcących i Zawodowych w Siemianowicach Salskich',
        'Podkarpacki Zespół Placówek Wojewódzkich w Rzeszowie - Podkarpackie Centrum Edukacji Nauczycieli',
        'Zespół Szkół Geodezyjno-Technicznych im. Sybiraków w Lodzi',
        'Fundacja Europejskich Inicjatyw Społecznych, Fundacja',
        'Akademicka Szkolą Ponadpodstawowa w Łomży',
        'Lubuska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół Nr 2 im. Przyjaźni Polsko-Norweskiej',
        'Zespół Szkół Ponadgimnazjalnych nr 4 im. Kazimierza Wielkiego w Siedlcach',
        'Zespół Szkół Zawodowych Nr 1 im. mjr. Henryka Dobrzańskiego w Bychawie',
        'Zespół Szkół Ponadpodstawowych nr 4  im Władysława Grabskiego w Łowiczu',
        'Zespół Szkół im. ks. Stanisława Staszica',
        'Zespół Szkół Ekonomicznych im. Eugeniusza Kwiatkowskiego w Sandomierzu',
        'Zespół Szkół im. Jana Wyzykowskiego w Głogowie',
        'ZESPÓŁ SZKÓŁ Ogólnokształcących I ZAWODOWYCH IM. KS. PROF. JOZEFA TISCHNERA W LIMANOWEJ SPOLKA Z OGRANICZONA ODPOWIEDZIALNOSCIA',
        'Zespół Szkół Ponadpodstawowych Nr 2 im. ks. Stanisława Szpetnara w Krośnie',
        'Wieloprofilowy Zespol Szkol',
        'Ochotnicze Hufce Pracy Podkarpacka Wojewódzka Komenda',
        'EDU WAW CONSULTING SPOLKA Z OGRANICZONA ODPOWIEDZIALNOSCIA',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. chor. Jana Szymańskiego  w Marianowie',
        'Zespół Szkół Nr 1 im. Eugeniusza Kwiatkowskiego w Myszkowie',
        'CENTRUM KSZTAŁCENIA ZAWODOWEGO i USTAWICZNEGO W BRODNICY',
        'Zespół Szkół im. I. J. Paderewskiego w Knurowie',
        'Zespół Szkół nr 3 im. Mikołaja Kopernika',
        'Zespół Szkół Ponadpodstawowych im. Jana Pawła II',
        'Fundacja Rozwój i Edukacja',
        'Zespół Szkół nr 2 im. Bartosza Głowackiego w Krasnymstawie',
        'Zespół Szkół Przemysłu Mody i Reklamy im. W.S. Reymonta',
        'Zespół Szkół Technicznych w Ostrowie Wielkopolskim',
        'Ochotnicze Hufce Pracy Wielkopolska Wojewódzka Komenda',
        'Zespół Szkół  im. Batalionów Chłopskich w Zielonej',
        'Zespół Szkół im Króla Władysława Jagiełły w Lidzbarku',
        'Samodzielny Publiczny Zakład Opieki Zdrowotnej "Śródmieście" w Opolu',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. 1000-lecia Państwa Polskiego w Nakle Salskim',
        'Fundacja Wspierania Edukacji AM Consulting and Education',
        'Eturia Spółka z ograniczona odpowiedzialnością',
        'BEAR ANNA ZEGAN',
        'Specjalny Ośrodek Szkolno-Wychowawczy im. Janusza Korczaka w Sokółce',
        'Zespół Szkół nr 1 im. Stanisława Staszica w Płońsku',
        'Zespół Szkół Technicznych im. Wincentego Pola w Gorlicach',
        'Technikum nr 20 w Zespole Szkol nr 11 im. Władysława Grabskiego',
        'Zespół Szkół Ogólnokształcących i Technicznych im. Jana Pawła II w Lipsku',
        'Zespół Szkół nr 1 im. Jana Kilińskiego w Pabianicach',
        'FUNDACJA MODE - MOVE AND DEVELOP FOUNDATION',
        'POWIATOWY ZESPÓŁ SZKÓŁ W SWIEBODZINIE',
        'Oddział Wojewódzki Stowarzyszenia Na Rzecz Aktywizacji Zawodowej i Pomocy Socjalnej Młodzieży',
        'Fundacja Aktywne Społeczeństwo',
        'Salska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        '"Oświata-Lingwista" Nadbałtyckie Centrum Edukacji Spółka z o.o.',
        'Regionalna Organizacja Turystyczna Województwa Świętokrzyskiego',
        'Zespół Szkół Ponadpodstawowych im. gen. Władysława Sikorskiego w Pomiechówku',
        'Centrum Kształcenia Zawodowego Nauka Maria Wasiewicz Galinska',
        'STOWARZYSZENIE EDUKACJI DLA ZRÓWNOWAZONEGO ROZWOJU "EKOS"',
        'ZESPÓŁ SZKÓŁ CENTRUM KSZTAŁCENIA ROLNICZEGO IM. ADOLFA DYGASINSKIEGO W SICHOWIE DUZYM',
        'Zespół Szkół Technicznych Olecko',
        'Fundacja Młodzieży Wiejskiej',
        'Zespół Szkół Technicznych i Ogólnokształcących "MERITUM" im. Piotra Kołodzieja w Siemianowicach Śląskich',
        'Zespół Szkół  nr 1 w Ożarowie Mazowieckim',
        'Świętokrzyskie Centrum Doskonalenia Nauczycieli',
        'Heuresis Sp. z o. o.',
        'Zespół Szkół Ekonomicznych im. Generała Stefana Roweckiego "Grota"',
        'Zespół Szkół nr 40 im. Stefana Starzyńskiego w Warszawie',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Jana Pawła II w Brzostku',
        'Zespół Szkół Ponadpodstawowych im. inż. Jozefa Marka',
        'Fundacja Skarabeusz',
        'Niepubliczna Branżowa Szkoła I Stopnia',
        'Proyecto Iberico',
        'Zespół Szkół Zawodowych Nr 1 im. mjr. Henryka Dobrzańskiego w Bychawie',
        'Zespół Szkół Ponadpodstawowych nr 1 w Łasku',
        'Zespół Szkół nr 2 im. Bartosza Głowackiego w Krasnymstawie',
        'Zespół Szkół Zawodowych w Gołdapi',
        'ZSZ_Nr6_Poznań',
        'Państwowe Szkoły Budownictwa im. prof. Mariana Osińskiego',
        'Zespół Szkół nr 1 im. Stanisława Staszica w Kwidzynie',
        'Zespół Szkół Nr 6 im. St. Staszica',
        'Zespół Szkół Budowlanych im. Kazimierza Wielkiego w Radomiu',
        'Świętokrzyska Wojewódzka Komenda Ochotniczych Hufców Pracy w Kielcach',
        'Specjalny Ośrodek Szkolno- Wychowawczy im. Janusza Korczaka',
        'Zespół Szkół Ekonomicznych i Ogólnokształcących im. Mikołaja Kopernika w Oleśnie',
        'Zespół Szkół im. W. Witosa w Zarzeczu',
        'Krajowy Sekretariat Przemysłu Chemicznego NSZZ "SOLIDARNOŚĆ"',
        'Zespół Szkół Technicznych',
        'Lubelska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Ochotnicze Hufce Pracy Centrum Kształcenia i Wychowania w Gołdapi',
        'Zespół Szkół Ponadgimnazjalnych nr 2 im. Mikołaja Kopernika w Siedlcach',
        'Opolska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Dolnośląska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół Ogólnokształcących i Zawodowych im. Stefana Kardynała Wyszyńskiego',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Zesłańców Sybiru w Bobowicku',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Władysława Grabskiego',
        'Ochotnicze Hufce Pracy Wielkopolska Wojewódzka Komenda',
        'Małopolska Izba Rzemiosła i Przedsiębiorczości',
        'Niepubliczne Technikum im. T. Kościuszki w Ostrowcu Świętokrzyskim Zakładu Doskonalenia Zawodowego w Kielcach',
        'Śląska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół Zawodowych Nr 2 im. dr A. Troczewskiego',
        'Centrum Edukacji Zawodowej i Ustawicznej "Kopernik"',
        'Zespół Szkół nr 2 im. Tadeusza Rejtana',
        'Fundacja Centrum Umiejętności Praktycznych',
        'Zespół Szkół Mechanicznych i Logistycznych im. inż. Tadeusza Tańskiego',
        'Centrum Kształcenia Zawodowego i Ustawicznego w Pionkach',
        'Fundacja Partnerstwo na Rzecz Rozwoju',
        'Zespół Szkół Budowlanych w Bielsku-Białej',
        'Zespół Szkół Centrum Kształcenia Ustawicznego im. Juliusza Poniatowskiego',
        'Zespół Szkół Agro-Technicznych im. Wincentego Witosa',
        'Techniczne Zakłady Naukowe',
        'Zespół Szkół nr 6 im. M. Rataja w Ełku',
        'Zespół Szkół nr 1',
        'Okręgowa Izba Radców Prawnych w Warszawie',
        'Zespół Szkół Zawodowych nr 1 w Brzegu',
        'Zespół Szkół Ponadpodstawowych Nr 2 im. ks. Stanisława Szpetnara w Krośnie',
        'Fundacja Europejskich Inicjatyw Społecznych',
        'Centrum Kształcenia i Wychowania OHP w Szczawnicy-Jablonce',
        'Zespół Szkół Nr 1 im. Legionów Polskich',
        'Zabrzańskie Centrum Kształcenia Ogólnego i Zawodowego w Zabrzu',
        'Zespół Szkół nr 1 im. Mikołaja Kopernika',
        'Zespół Szkół Zawodowych nr 1 im. mjr. H. Dobrzańskiego "Hubala" w Starachowicach',
        'Zespół Szkół Samochodowych i Budowlanych',
        'Zespół Szkół nr1 im. Jana Pawła w Przysusze',
        'Zespół Szkół Ekonomiczno-Usługowych im. F. Chopina',
        'Zespół Szkół Ogólnokształcących im. Jana Pawła II',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Adolfa Dygasińskiego w Sichowie Dużym',
        'Zespół Szkół Ekonomicznych im. Józefa Gniazdowskiego',
        'Zespół Szkół Gastronomiczno-Hotelarskich im. Janka Bytnara "Rudego"',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Michała Drzymały w Brzostowie',
        'Zespół Szkół Zawodowych nr 5 we Wrocławiu',
        'Zespół Szkół imienia Leokadii Bergerowej w Płocku',
        'Zespół Szkół Nr 2 im. Jana Pawła II w Miechowie',
        'Stowarzyszenie EDUQ',
        'Zespół Szkół Ogólnokształcąco-Technicznych w Lublińcu',
        'Technikum Ośrodka Edukacji Sokrates',
        'Medicus Group Spółka z ograniczoną odpowiedzialnością',
        'Zespół Szkół Centrum Kształcenia Rolniczego im. Ziemi Dobrzyńskiej w Nadrożu',
        'Zespół Szkół Leśnych',
        'Zespół Szkół im. Piotra Wysockiego',
        'Zespół Szkół nr 40 im. Stefana Starzyńskiego w Warszawie',
        'Zespół Szkół Przemysłu Spożywczego im. Jana i Jędrzeja Śniadeckich',
        'Zespół Szkół w Staszowie',
        'Towarzystwo Umiejętności Rolniczych TUR',
        'Zespół Szkół Nr 1 w Żyrardowie',
        'Zespół Szkół Ekonomicznych im. Stanisława Staszica w Słupsku',
        'Zespół Szkół Samochodowo-Usługowych im. W."Oseta" Wasilewskiego Technikum Nr 3',
        'Fundacja Awans',
        'Technikum Nr 4 im. inż.. Eugeniusza Kwiatkowskiego Zespołu Szkół Transportowo- Mechatronicznych',
        'Zespół Szkół w Żywcu Zakładu Doskonalenia Zawodowego w Katowicach',
        'Zespół Szkół Nr 1 im. Ignacego Łukasiewicza w Gorlicach',
        'Pomorska Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół Centrum Kształcenia Rolniczego imienia Powstańców Wielkopolskich w Bielicach',
        'SEMPER AVANTI',
        'Niepubliczne Technikum Zawodowe w Kozienicach Zakładu Doskonalenia Zawodowego w Kielcach',
        'Zespół Szkół Zawodowych im. mjr. H. Dobrzańskiego "Hubala" w Radomiu',
        'Zespół Szkół Technicznych im. Wincentego Pola w Gorlicach',
        'Centrum Kształcenia Zawodowego i Ustawicznego nr 2 w Przemyślu',
        'Zespół Szkół Technicznych i Ogólnokształcących "MERITUM" im. Piotra Kołodzieja',
        'Zespół Szkół im. Żołnierzy Armii Krajowej w Makowie Mazowieckim',
        'Zespół Szkół Drzewnych i Leśnych im. Jana Kochanowskiego w Garbatce-Letnisku',
        'Zespół Szkół Ponadpodstawowych im. inż. Józefa Marka',
        'Fundacja Nowe Technologie',
        'Łódzka Wojewódzka Komenda Ochotniczych Hufców Pracy',
        'Zespół Szkół w Kowalu',
        'ZSS nr 2',
        'Centrum Rozwoju Lokalnego',
        'Zespół Szkół Logistycznych',
        'Fundacja na rzecz Wsparcia Współpracy Międzynarodowej „KROKUS”',
        'Regionalna Izba Budownictwa w Łodzi',
        'Szkoła Podstawowa Specjalna z Oddziałami Przedszkolnymi nr 7 w Rybniku',
        'Europejska Fundacja Odnowy i Rozwoju Terytorialnego'
        ]

def simplified_address(address):
    #https://
    if address.find('://')!= -1:
        #https://.....pl/bla_bla
        if address.find('/', address.find('://') + 3)!= -1:
            return address[:address.find('/', address.find('://') + 3)]
    #....pl/bla_bla
    else:
        if address.find('/')!= -1:
            return address[:address.find('/')]
    return address

def search_in_gov(query_list, respond_list):
    #We are getting into webside
    browser.get("https://www.gov.pl/web/dostepnosc-cyfrowa/wykaz-stron-internetowych-podmiotow-publicznych")

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="register-search-input-20052445"]')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-search-input-20052445"]')))

    #We are typing in search bar and printing results or '???' if no results
    search_bar = browser.find_element(By.XPATH, '//*[@id="register-search-input-20052445"]')
    for i, query in enumerate(query_list):
        search_bar.send_keys(query)
        sleep(2)
        try:
            web_address = browser.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/a')
            print(web_address.text)
            respond_list.append(web_address.text)
        except:
            print('???')
            respond_list.append('???')
        search_bar.clear()

def search_in_google_1_list(query_list_1, respond_list):
    for i, query in enumerate(query_list_1):
        results = search(f'"{query_list_1[i]}"')
        #Wyświetl pierwszy wynik
        for result in results:
            print(result)
            respond_list.append(result)
            break
        sleep(30)

def search_in_google_2_lists(query_list_1, query_list_2, respond_list):
    for i, query in enumerate(query_list_1):
        if respond_list[i] == '???':
            results = search(f'Strona internetowa {query_list_1[i]} {query_list_2[i]}')
            #Wyświetl pierwszy wynik
            for result in results:
                print(result)
                respond_list[i] = result
                break
        sleep(2)

def search_in_google_1_list_selenium(query_list, respond_list):
    #We are getting into webside
    browser.get("https://www.google.com/search?q=temp&client=firefox-b-lm&sca_esv=597475757&sxsrf=ACQVn0-18F909MJYKMHGVEbPRRErfuy3rQ%3A1704968446790&ei=_sCfZaruL6Dkxc8PztKUgAc&udm=&ved=0ahUKEwiq5f60jtWDAxUgcvEDHU4pBXAQ4dUDCBA&uact=5&oq=temp&gs_lp=Egxnd3Mtd2l6LXNlcnAiBHRlbXAyCxAAGIAEGLEDGIMBMgsQABiABBiKBRiSAzIOEAAYgAQYsQMYgwEYyQMyCxAAGIAEGLEDGIMBMgsQLhiABBixAxiDATIIEAAYgAQYsQMyCBAuGIAEGLEDMggQABiABBixAzIFEAAYgAQyCBAAGIAEGLEDSLQPULwGWIsLcAJ4AZABAJgBX6ABrgKqAQE0uAEDyAEA-AEBwgIKEAAYRxjWBBiwA8ICDRAAGIAEGIoFGEMYsAPCAhMQLhiABBiKBRhDGMgDGLAD2AEBwgIbEC4YgAQYigUYQxjHARjRAxjIAxiwAxgK2AEBwgIKECMYgAQYigUYJ8ICEBAAGIAEGIoFGEMYsQMYgwHCAgoQABiABBiKBRhDwgIOEC4YgAQYigUYsQMYgwHCAhEQLhiABBixAxjHARivARiOBcICDhAuGIAEGMcBGK8BGI4FwgIOEAAYgAQYigUYsQMYgwHiAwQYACBBiAYBkAYMugYECAEYCA&sclient=gws-wiz-serp")

    sleep(5)

    print("Oki")
    try:
        browser.switch_to.frame(browser.find_element(By.XPATH, '/html/body/div[1]/form/div/div/div/iframe'))
        print('Changed frame')
        
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]')))
        WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]')))

        anty_bot_button = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]')
        anty_bot_button.click()
        
        input('MEEEEEN\nI need to you check the page!\nPress any key if you have done it')
        
        browser.switch_to.default_content()
    except:
        print('No anty-bot frame')
    
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
    search_bar = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_bar.clear()
    search_bar.send_keys('Kwiateeek')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/button')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/button')))
    search_bar_button = browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/button')
    search_bar_button.click()
    
    print('Searching... Kwiatek')
    sleep(5)
    
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
    search_bar = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_bar.clear()
    search_bar.send_keys('Psiak')
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')))
    search_bar_button = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')
    search_bar_button.click()

    print('Searching... Psiak')
    #wynik = browser.find_element(By.XPATH, '/html/body/div[5]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a')
    #print(wynik.get_attribute('href'))

    result_xpath = '//div[@id="search"]//*[contains(@href,"https://")]'
    first_result = browser.find_element(By.XPATH, result_xpath)
    print(first_result.get_attribute('href'))
    
    for i in query_list:
        try:        
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
            search_bar = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
            search_bar.clear()
            search_bar.send_keys(i)
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')))
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')))
            search_bar_button = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')
            search_bar_button.click()
            
            result_xpath = '//div[@id="search"]//*[contains(@href,"https://")]'
            first_result = browser.find_element(By.XPATH, result_xpath)
            print(first_result.get_attribute('href'))
            respond_list.append(first_result.get_attribute('href'))
        except:
            input('MEEEEEN\nI need to you check the page!\nPress any key if you have done it')
            
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]')))
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
            search_bar = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
            search_bar.clear()
            search_bar.send_keys(i)
            WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')))
            WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')))
            search_bar_button = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[1]/div[1]/div[2]/button')
            search_bar_button.click()
            
            result_xpath = '//div[@id="search"]//*[contains(@href,"https://")]'
            first_result = browser.find_element(By.XPATH, result_xpath)
            print(first_result.get_attribute('href'))
            respond_list.append(first_result.get_attribute('href'))
        

    
    return True

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="register-search-input-20052445"]')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-search-input-20052445"]')))

    #We are typing in search bar and printing results or '???' if no results
    search_bar = browser.find_element(By.XPATH, '//*[@id="register-search-input-20052445"]')
    for i, query in enumerate(query_list):
        search_bar.send_keys(query)
        sleep(2)
        try:
            web_address = browser.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/a')
            print(web_address.text)
            respond_list.append(web_address.text)
        except:
            print('???')
            respond_list.append('???')
        search_bar.clear()



#school_names = ['Szkoła Policealna - Medyczne Studium Zawodowe w Biłgoraju', 'Powiatowy Zespół Szkół nr 2 im K. Miarki', 'Zespół Szkół Nr 2 im. Grzegorza z Sanoka w Sanoku', 'Wojewódzki Zakład Doskonalenia Zawodowego', 'Zespół Szkół im. Władyslawa Szybińskiego', 'Zespół Szkół Ponadpodstawowych w Chojnie', 'Zespół Szkół Centrum Kształcenia Rolniczego im. Wincentego Witosa', 'Zespół Szkół Zawodowych im. Gen. Józefa Bema w Węgorzewie', 'Zespół Szkół Ponadpodstawowych im. Władysława Reymonta w Bierutowie', 'Zespół Szkół Ponadgimnazjalnych Nr 3 w Malborku']
#school_address = ['Tadeusza Kościuszki 127 23-400 Biłgoraj', 'SZYMANOWSKIEGO 12 PSZCZYNA PSZCZYNA', 'Stróżowska 15 38-500 Sanok', 'Jana Kilińskiego 70-965 Szczecin', 'Kraszewskiego 11 43-400 Cieszyn', 'Dworcowa 3 74-500 Chojna', 'ul. Bialska 7 21-542 Leśna Podlaska', 'Szpitalna 9 11-600 Węgorzewo', 'Plac Kościelny 2 56-420 Bierutów', 'Al. Wojska Polskiego 502 82-200 Malbork']

#search_in_gov(school_names, school_web_address)

szkoly_600 = szkoly()

szkoly_20 = []
ola = 194
while(ola < len(szkoly_600)):
    szkoly_20.append(szkoly_600[ola])
    ola += 1

school_web_address = []

print(szkoly_20)

print()

#search_in_google_1_list(szkoly_20, school_web_address)
#search_in_gov(szkoly_600, school_web_address)

browser = webdriver.Firefox()
search_in_google_1_list_selenium(szkoly_20, school_web_address)
browser.close()

print(school_web_address)

write_file_name = 'ciasteczko_numer1.txt'

if not os.path.exists(write_file_name):
    with open(write_file_name, "w"):
        pass

with open(write_file_name, 'a') as f:
    for i in school_web_address:
        f.write(i + '\n')

#search_in_google(school_names, school_address, school_web_address)

print(school_web_address)
