import pytest
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class Test_product_page():
	def test_add_to_basket(self, browser):
		browser.get(link)
		btn = browser.find_elements(By.XPATH, "//form[@id='add_to_basket_form']/button[@type='submit']")
		assert len(btn) > 0, "add to basket button not exist"
