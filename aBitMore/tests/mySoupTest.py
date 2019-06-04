#this is more of history, dont run this



import bs4 as bs
import urllib.request
import ssl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
#import sys
#from PyQt5.QtGui import QGuiApplication
#from PyQt5.QtCore import QUrl
#from PyQt5.QtWebKit import QWebPage

chrome_path =r'/Applications/Google Chrome.app'
driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
url = "https://www.avoyatravel.com/cruises/search/?lengthList=7-9,10-14,15-999&maxrows=150"
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

driver.get(url)
#closes the popups so that you can access the elements of the main page
WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-modal"]/div/button'))).click()
WebDriverWait(driver,180).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="get-availability-modal"]/div/button'))).click()



#grabs the prices for all the cruises
price_list = []
price = driver.find_elements_by_xpath("//span[contains(@class, 'text-blue') and contains(@class, 'text-2xl')]")
for pri in price:
    price_list.append(pri.text)

#grabs the titles for all the cruises
title_list = []
title = driver.find_elements_by_xpath("//button[contains(@class, 'text-left') and contains(@class, 'text-xl') and contains(@class, 'font-bold') and contains(@class, 'text-blue')]")
for tit in title:
    title_list.append(tit.text)

#grabs the company name of the cruise trip
company_list = []
company = driver.find_elements_by_xpath("//h2[contains(@class, 'text-lg') and contains(@class, 'font-medium')]")
for com in company:
    company_list.append(com.text)

#grabs the list of places the cruise goes through
itinerary_list = []
itinerary = driver.find_elements_by_xpath("//span[contains(@class, 'capitalize')]")
for iti in itinerary:
    itinerary_list.append(iti.text)
print(price_list)
print(len(price_list))

driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[2]/a').click()

for xor in range(2,162):
    #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,  '')))
    if xor == 2 :
        time.sleep(20)
        price = driver.find_elements_by_xpath("//span[contains(@class, 'text-blue') and contains(@class, 'text-2xl')]")
        for pri in price:
            price_list.append(pri.text)
        print(price_list)
        print(len(price_list))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[4]/a').click()
    elif xor == 3 :
        time.sleep(20)
        price = driver.find_elements_by_xpath("//span[contains(@class, 'text-blue') and contains(@class, 'text-2xl')]")
        for pri in price:
            price_list.append(pri.text)
        print(price_list)
        print(len(price_list))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[5]/a').click()
    elif xor > 3 :
        time.sleep(20)
        price = driver.find_elements_by_xpath("//span[contains(@class, 'text-blue') and contains(@class, 'text-2xl')]")
        for pri in price:
            price_list.append(pri.text)
        print(price_list)
        print(len(price_list))
        driver.find_element_by_xpath(
            '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[6]/a').click()

