import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.Settings import *

driver = webdriver.Chrome(executable_path=CHROME_PATH)

class TestingLogin():



    def LoginNOK(self, username, parola, testcase):

        driver.get("http://www.demo.guru99.com/V4/")

        #user = driver.find_element_by_xpath(By.XPATH, USERNAME_XPATH)
        user = driver.find_element(By.XPATH, "//input[@name='uid']")

        user.send_keys(username)

        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        time.sleep(5)


        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN" + testcase + " NOK FAILED")
            else:
                print("TEST CASE LOGIN" + testcase + " NOK PASS")
        except:
            print("TEST CASE LOGIN" + testcase + " NOK PASS")






    def LoginOK(self, username, parola):

        driver.get("http://www.demo.guru99.com/V4/")

        #user = driver.find_element_by_name("uid")
        #user = driver.find_element_by_xpath(By.XPATH, USERNAME_XPATH)
        user = driver.find_element(By.XPATH, "//input[@name='uid']")
        user.send_keys(username)

        #password = driver.find_element_by_name("password")
        #password = driver.find_element_by_xpath("//input[@name='password']")
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN PASS")
            else:
                print("TEST CASE LOGIN FAILED")

        except:
             print("TEST CASE LOGIN FAILED")



#username = "mngr327236"
#parola = "parolaNOK"


test = TestingLogin()
test.LoginOK("mngr327236", "rehavAs")

#test.LoginNOK(USERNAME, PASSWORD)

test.LoginNOK("mngr327236", "parolaNOK", " user ok, password nok")
test.LoginNOK("userNOK", "rehavAs", " user nok, password ok")
test.LoginNOK("userNOK", "parolaNOK", " user nok, password nok")
test.LoginNOK("", "rehavAs", " user <empty>, password ok")
test.LoginNOK("mngr327236", "", " user ok, password <empty>")


#user ok, parola nok
#user NOK, parola OK
#user nok, parola nok
driver.quit()

