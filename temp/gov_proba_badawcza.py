from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_in_gov(query_list):
    #We are getting into webside
    browser.get("https://www.gov.pl/web/dostepnosc-cyfrowa/wykaz-stron-internetowych-podmiotow-publicznych")

    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="register-search-input-20052445"]')))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-search-input-20052445"]')))

    #We are typing in search bar and printing results or '???' if no results
    search_bar = browser.find_element(By.XPATH, '//*[@id="register-search-input-20052445"]')
    for query in query_list:
        search_bar.send_keys(query)
        sleep(1)
        try:
            web_address = browser.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/a')
            print(web_address.text)
        except:
            #print('No results for: ' + query)
            print('???')

browser = webdriver.Firefox()

school_names = ['Szkoła Policealna - Medyczne Studium Zawodowe w Biłgoraju', 'Powiatowy Zespół Szkół nr 2 im K. Miarki', 'Zespół Szkół Nr 2 im. Grzegorza z Sanoka w Sanoku', 'Wojewódzki Zakład Doskonalenia Zawodowego', 'Zespół Szkół im. Władyslawa Szybińskiego', 'Zespół Szkół Ponadpodstawowych w Chojnie', 'Zespół Szkół Centrum Kształcenia Rolniczego im. Wincentego Witosa', 'Zespół Szkół Zawodowych im. Gen. Józefa Bema w Węgorzewie', 'Zespół Szkół Ponadpodstawowych im. Władysława Reymonta w Bierutowie', 'Zespół Szkół Ponadgimnazjalnych Nr 3 w Malborku']

search_in_gov(school_names)

browser.close()