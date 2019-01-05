from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from urllib.parse import quote
import pyautogui as gui

def getDriver(is_hide):
    option = webdriver.ChromeOptions()
    if is_hide:
        option.add_argument('headless')
        option.add_argument('log-level=2')
    driver = webdriver.Chrome(options=option)
    return driver

def moneyChanger(currency):
    driver.get('https://www.xe.com/')
    text = driver.find_element_by_css_selector('input.Input-lwa9ow-0.AmountField-qk8iiz-0.jmapix')
    text.send_keys(currency, Keys.TAB, Keys.TAB, Keys.TAB, 'twd', Keys.ENTER, Keys.ENTER)
    return driver.find_element_by_css_selector('span.converterresult-toAmount').text

def searchOnHumbleBundle(driver, game):
    print('\nsearching on Humble Bundle')
    driver.get('https://www.humblebundle.com/store/search')
    search_bar = driver.find_element_by_css_selector('input.js-search-input.search-input')
    search_bar.send_keys(game, Keys.ENTER)
    try:
        element = WebDriverWait(driver, 20).until(EC.title_contains('"'))
    finally:
        results = driver.find_elements_by_css_selector('span.entity-title')
        price = driver.find_elements_by_css_selector('span.price')

        max_len = 0
        for x in results[:10]:
            if len(x.text) > max_len:
                max_len = len(x.text)

        price = [moneyChanger(x.text) for x in price[:10]]

        for x,y in zip(results[:10], price[:10]):
            print('{x:{len}}   NT{y}'.format(len=max_len, x=x.text, y=y))

def searchOnIndieGala(driver, game):
    print('\nsearching on Indie Gala')
    driver.get('https://www.indiegala.com/')
    try:
        driver.find_element_by_id('toggleMenu').click()
    except:
        pass
    driver.find_element_by_id('searchBox').send_keys(game)
    driver.find_element_by_id('iconsearch').click()
    try:
        element = WebDriverWait(driver, 20).until(EC.title_contains(game))
    finally:
        results = driver.find_elements_by_css_selector('h3.left')
        price = driver.find_elements_by_css_selector("div.buttons-cont.right.relative")

        max_len = 0
        for x in results[:10]:
            if len(x.text) > max_len:
                max_len = len(x.text)

        for x, y in zip(results[:10], price[:10]):
            try:
                y = y.find_element_by_css_selector('div.bottom')
            except:
                pass
            print('{x:{len}}   {y}'.format(len=max_len, x=x.text, y=y.text))

def searchOnGreenManGaming(driver, game):
    print('\nsearching on Green Man Gaming')
    driver.get('https://www.greenmangaming.com/')
    driver.find_element_by_css_selector('input.form-control.input-sm.search-input.input-search-header.ng-pristine.ng-untouched.ng-valid.ng-empty.ng-valid-maxlength').send_keys(game, Keys.ENTER)
    try:
        element = WebDriverWait(driver, 20).until(EC.title_contains('Search Results'))
    finally:
        results = driver.find_elements_by_xpath("/html/body/div/div/div/section/div/div/ul/li/div/div/div/div/a/p")
        temp = driver.find_elements_by_css_selector('div.info-int')

        price = []
        for x in temp:
            try:
                x = x.find_element_by_css_selector('span.current-price')
                x = x.find_element_by_css_selector('price.notranslate')
                price.append(x)
            except:
                pass

        max_len = 0
        for x in results[:10]:
            max_len = max(max_len, len(x.text))

        for x, y in zip(results[:10], price[:10]):
            print('{x:{len}}   {y}'.format(len=max_len, x=x.text, y=y.text))

def steamSale(driver):
    driver.get('https://store.steampowered.com/')
    driver.find_element_by_link_text('Games').click()
    driver.find_element_by_id('tab_select_TopSellers').click()

if __name__ == '__main__':
    driver = getDriver(False)
    game = input('the game you want: ')
    searchOnHumbleBundle(driver, game)
    #searchOnIndieGala(driver, game)
    #searchOnGreenManGaming(driver, game)
    driver.close()