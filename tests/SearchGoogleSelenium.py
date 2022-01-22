import time

from selenium import webdriver

class ChromeDriverWindows():

    def SearchGoogle(self):
        driver = webdriver.Chrome(executable_path="D:\\Automation\\chromedriver.exe")
        driver.get("https://www.google.com/")

        element = driver.find_element_by_id("L2AGLb")
        element.click()

        element_search = driver.find_element_by_name("q")
        element_search.send_keys("selenium")
        element_search.submit()

        #name="q"

        time.sleep(10)

#L2AGLb


search = ChromeDriverWindows()
search.SearchGoogle()