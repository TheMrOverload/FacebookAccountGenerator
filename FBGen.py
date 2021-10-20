#Imports
import uuid
import time
import os
from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Python39\geckodriver.exe')
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Input your username
firstname = "firstname"
lastname = "lastname"
#Input what accept cookies is in your language, look up at https://facebook.com/reg/
acceptCookiesText = "Alle Cookies gestatten"

rand = str(uuid.uuid4())

#Generate Email
emailLength = 18
email = rand[:emailLength] + '@fyii.de'

#Generate Password
passwdLength = 9
password = rand[:passwdLength]

        #fileNameEmails = "./users.txt"

        #f = open(fileNameEmails, "w+")
        #f.write(email + " " + password + "\n")
        #f.close()

#Get Browser
browser = webdriver.Firefox()
browser.get("https://facebook.com/reg/")

#Accept Cookies
time.sleep(2)
browser.find_element(By.XPATH, "//button[text()='" + acceptCookiesText + "']").click()

#Input Data
firstname = browser.find_element(By.NAME, "firstname").send_keys(firstname)
browser.find_element(By.NAME, "lastname").send_keys(lastname)
browser.find_element(By.NAME, "reg_email__").send_keys(email)
browser.find_element(By.NAME, "reg_email_confirmation__").send_keys(email)
browser.find_element(By.NAME, "reg_passwd__").send_keys(password)
        
#Set birthday
selDate = Select(browser.find_element(By.ID, "day"))
time.sleep(0.1)
selDate.select_by_visible_text("21")

#Set birthmonth
selMonth = Select(browser.find_element(By.ID, "month"))
time.sleep(0.1)
selMonth.select_by_visible_text("Jun.")

#Set birthyear
selYear = Select(browser.find_element(By.ID, "year"))
time.sleep(0.1)
selYear.select_by_visible_text("1989")
        
#select gender and create account
browser.find_element(By.NAME, "sex").click()
browser.find_element(By.NAME, "websubmit").click()