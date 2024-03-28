from calendar import c
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()

def search_in_kwejk(query):
    #We are getting into webside
    browser.get("https://www.kwejk.pl")

    #We are switching to iframe
    browser.switch_to.frame(browser.find_element(By.XPATH, '//*[@id="cmp-iframe"]'))

    #Wait for cookies iframe
    #WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/div/div[3]/div[2]/button")))

    #We are finding cookies button and clicking on it
    ciastko = browser.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div[3]/div[2]/button")
    ciastko.click()
    print('I have handled cookies!')

    #We are switching back to default content
    browser.switch_to.default_content()

    #We are clicking on search button
    search_button = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div/a")
    search_button.click()
    print('I have clicked on search bar!')

    #We are typing in search bar
    search_bar = browser.find_element(By.XPATH, "/html/body/header/section/div/div[1]/div/div/form/div/input")
    search_bar.send_keys(query)
    print('I have typed in search bar!')

    #We are clicking on search submit button
    search_submit = browser.find_element(By.XPATH, "/html/body/header/section/div/div[1]/div/div/form/div/button")
    search_submit.click()
    print('I have clicked on search submit!')


search_in_kwejk('psiak')

sleep(7)
browser.close()