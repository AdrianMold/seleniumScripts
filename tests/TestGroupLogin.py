import time

from selenium.webdriver.common.by import By
from setup import CHROME_DRIVER as driver

class TestGroupLogin():
    """
    description
    """

    def __init__(self) -> None:
        self.driver = driver.get("http://www.demo.guru99.com/V4/")

    def test_login_should_not_be_ok(self, username, parola, testcase):
        """
        test user login on demoguru99 site
        """
        # setup
        user = driver.find_element(By.XPATH, "//input[@name='uid']")

        # execution
        user.send_keys(username)

        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        time.sleep(5)

        # TODO: try out testing your testcase with `assert`
        # https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN" + testcase + " NOK FAILED")
            else:
                print("TEST CASE LOGIN" + testcase + " NOK PASS")
        except:
            print("TEST CASE LOGIN" + testcase + " NOK PASS")

    def test_login_should_be_ok(self, username, parola):
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

    def teardownTests(self) -> None:
        """
        Cleanup after tests
        """
        driver.quit()
