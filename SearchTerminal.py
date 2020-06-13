# Imports
from time import sleep
from selenium import webdriver
from logger import logger

# Options
firefoxOptions = webdriver.FirefoxOptions()
firefoxOptions.headless = False

# Terminal

print("Hello There !")
while True:
    print("You have three choices: ddg, bing or google")
    search_engine = input("Choose one of the search engines above\n:  ")

    # DuckDuckGo
    if search_engine == "ddg":
        search = input("Type your search : ")
        url = "https://www.duckduckgo.com/?q={}".format(search)
        driver = webdriver.Firefox(options=firefoxOptions)
        driver.get(url)
        logger.info("Starting browser...")
        break
    # Google

    if search_engine == "google":
        search = input("Type your search : ")
        url = "https://www.google.com/search?q={}".format(search)
        driver = webdriver.Firefox(options=firefoxOptions)
        driver.get(url)
        logger.info("Starting browser...")
        break
    # Bing

    if search_engine == "bing":
        search = input("Type your search : ")
        url = "https://www.bing.com/search?q={}".format(search)
        driver = webdriver.Firefox(options=firefoxOptions)
        driver.get(url)
        logger.info("Starting browser...")
        break
    # Others
    if search_engine != "ddg" or "google" or "bing":
        while True:
            print("Incorrect search engine !\n Type ddg, google or bing !")
            search_engine = input(" : ")
            # Bing
            if search_engine == "bing":
                search = input("Type your search : ")
                url = "https://www.bing.com/search?q={}".format(search)
                driver = webdriver.Firefox(options=firefoxOptions)
                driver.get(url)
                logger.info("Starting browser...")
                break
            # Google
            if search_engine == "google":
                search = input("Type your search : ")
                url = "https://www.google.com/search?q={}".format(search)
                driver = webdriver.Firefox(options=firefoxOptions)
                driver.get(url)
                logger.info("Starting browser...")
                break
            # DuckDuckGo
            if search_engine == "ddg":
                search = input("Type your search : ")
                url = "https://www.duckduckgo.com/?q={}".format(search)
                driver = webdriver.Firefox(options=firefoxOptions)
                driver.get(url)
                logger.info("Starting browser...")
                break
