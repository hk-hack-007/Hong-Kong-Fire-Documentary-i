import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc

import unittest, time, re, random
from selenium import webdriver
import sys
from datetime import datetime as dt
import asyncio
import subprocess

my_datetime = dt.now().strftime('%Y-%m-%d')



if __name__ == "__main__":

    driver = uc.Chrome(headless=False,use_subprocess=False)
    actions = ActionChains(driver)
    
    
    driver.get("https://www.inmediahk.net/taxonomy/term/541575/530434")
    time.sleep(10)
    
    num = 0
    start_date = "2025-12-12"
    while num >= 0:
        links = driver.find_elements(By.XPATH, "/html/body/div[4]/section/section/div[2]/div[2]/section/div")
        count = len(links)

        for j in range(count):
            try:
                i = count-j
                p_elm = driver.find_element(By.XPATH, "/html/body/div[4]/section/section/div[2]/div[2]/section/div["+str(i)+"]/div[2]/p")
                a_elm = driver.find_element(By.XPATH, "/html/body/div[4]/section/section/div[2]/div[2]/section/div["+str(i)+"]/div[2]/a[2]")
                h3_elm = driver.find_element(By.XPATH, "/html/body/div[4]/section/section/div[2]/div[2]/section/div["+str(i)+"]/div[2]/a[2]/h3")
                address = a_elm.get_attribute("href")
                article_date = p_elm.text
                article_title = h3_elm.text
                if article_date != start_date:
                    start_date = article_date
                    print("")
                    print("## "+start_date)
                    print("")
                print("- ["+article_title+"]("+address+")")
            except Exception:
                pass            
        
        driver.get("https://www.inmediahk.net/taxonomy/term/541575/530434?page="+str(num))
        time.sleep(5)
        num = num - 1