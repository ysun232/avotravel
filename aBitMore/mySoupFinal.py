#working version of website scraping of avoytravel. Run this only
#could not reach the last few tabs because chrome kept crashing

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
#works, but the chrome driver crashes, and I cant extract the data from the website


driver = webdriver.Firefox(executable_path='/Applications/geckodriver')
url = "https://www.avoyatravel.com/cruises/search/?lengthList=7-9,10-14,15-999&maxrows=150"
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

driver.get(url)

price_list = []
title_list = []
company_list = []
itinerary_list = []
time_taken = []


#closes the popups so that you can access the elements of the main page
WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="register-modal"]/div/button'))).click()
WebDriverWait(driver,180).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="get-availability-modal"]/div/button'))).click()

for xor in range(1,10):
    #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,  '')))
    time.sleep(20)
    #using xpath to find all the fields with the desired information since by class name does not accept compound names
    price = driver.find_elements_by_xpath("//span[contains(@class, 'text-blue') and contains(@class, 'text-2xl')]")
    for pri in price:
        price_list.append(pri.text)
        time_taken.append(now)
    title = driver.find_elements_by_xpath(
        "//button[contains(@class, 'text-left') and contains(@class, 'text-xl') and contains(@class, 'font-bold') and contains(@class, 'text-blue')]")
    for tit in title:
        title_list.append(tit.text)
    company = driver.find_elements_by_xpath("//h2[contains(@class, 'text-lg') and contains(@class, 'font-medium')]")
    for com in company:
        company_list.append(com.text)
    itinerary = driver.find_elements_by_xpath("//span[contains(@class, 'capitalize')]")
    for iti in itinerary:
        itinerary_list.append(iti.text)

    #iterates through the entire website
    #each page can display at most 150 results
    #by test, the webdriverwait should be in theory better than driver.find_element_by_xpath
    if xor == 1 :
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[2]/a'))).click()
        #driver.find_element_by_xpath(
        #    '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[2]/a').click()
    elif xor == 2 :
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[4]/a'))).click()
        #driver.find_element_by_xpath(
        #    '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[4]/a').click()
    elif xor == 3 :
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[5]/a'))).click()
        #driver.find_element_by_xpath(
        #    '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[5]/a').click()
    else :
        if xor == 66:
            break
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[6]/a'))).click()
        #driver.find_element_by_xpath(
        #    '//*[@id="__layout"]/div/div[3]/div[2]/section/div/div/div[2]/div[3]/div[2]/nav/div[2]/ol/li[6]/a').click()

list_of_lists =[title_list, price_list, company_list, itinerary_list, time_taken]
oldArr = (list_of_lists)
size = len(oldArr[1])
newArr = []
for i in range(size):
    newArr.append([])
for i,val in enumerate(oldArr):
    for index,value in enumerate(val):
        newArr[index].append(value)

newTuple = tuple(newArr)
print (newTuple)


#for some reason the website displays 160 clickeable pages for cruises, but returns error at 67
#they say they have 23,854 cruises, displaying 150 per page, which would be a total of 160 pages
