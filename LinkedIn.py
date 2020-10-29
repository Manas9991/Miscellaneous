from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('path\chromedriver') 

driver.get("https://linkedin.com/")

us = "Your Username here"
 
pw = "Your Password here"
#enter username
x_us = '/html/body/main/section[1]/div[2]/form/div[2]/div[1]/input'
usbar = driver.find_element_by_xpath(x_us) 
usbar.send_keys(us);
#enter password
x_pw = '/html/body/main/section[1]/div[2]/form/div[2]/div[2]/input'
pwbar = driver.find_element_by_xpath(x_pw) 
pwbar.send_keys(pw);
#click login
x_log = '/html/body/main/section[1]/div[2]/form/button'
log = driver.find_element_by_xpath(x_log)
log.click()
print("Logged In")
#click mynetwork
driver.implicitly_wait(15)
x_n = '/html/body/div[8]/header/div[2]/nav/ul/li[2]/a/span'
n = driver.find_element_by_xpath(x_n)
n.click()
print("Opened requests page")
#check credentials:
x_cred = '/html/body/div[8]/div[3]/div/div/div/div/div/div/ul/li[1]/ul/li[1]/div/section/div[1]/a/span[4]'
cred = driver.find_element_by_xpath(x_cred)
credentials = cred.text
if ("Your desired credential" in credentials):
    #click accept
    driver.implicitly_wait(10)
    a = driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div/div/div/div/div/div[1]/section/div/ul/li/div/div[2]/button[2]')
    a.click()
    print("Found correct and Accepted")
else:
    print("Incorrect Credentials, please review manually")