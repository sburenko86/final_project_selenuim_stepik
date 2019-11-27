from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_buy(self):
        link = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        link.click()
