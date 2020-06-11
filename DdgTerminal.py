#Imports
from time import sleep
from selenium import webdriver
from logger import logger
import pytest
#Just Some Test
str_test = "lol"
#Options
firefoxOptions = webdriver.FirefoxOptions()
firefoxOptions.headless = False

#Terminal
print("Hi Welcome to DuckDuckGo Terminal")
sleep(1)
search = input("Type your search : ")
if search == "":
    while search == "":
        search = input("Try again : ")



url = "https://www.duckduckgo.com/?q={}".format(search)

try:
    driver = webdriver.Firefox(options=firefoxOptions)
    driver.get(url)
    logger.info("Success ! ")
    sleep(1)
except:
    logger.critical("Failed to launch the browser")
