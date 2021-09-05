import time

#from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\Automation\\chromedriver.exe")

class Facebook():

    def Login(self):
        driver.get("https://www.facebook.com/")
        acceptAll = driver.find_element_by_xpath("//button[normalize-space()='Alle akzeptieren']")
        acceptAll.click()

        email = driver.find_element_by_xpath("//input[@id='email']")
        email.send_keys("email@yahoo.com")

        password = driver.find_element_by_xpath("//input[@id='pass']")
        password.send_keys("parola")

        login = driver.find_element_by_xpath("//button[normalize-space()='Anmelden']")
        login.click()

        time.sleep(10)

        #//input[@id='email']
        #//input[@id='pass']
        #//button[normalize-space()='Anmelden']

fb = Facebook()
fb.Login()
driver.quit()