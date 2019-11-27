from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
from time import sleep

class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        x = alert.text.split(" ")[2]
        print(x)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass
