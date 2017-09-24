from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get("https://www.facebook.com")
user = "simplybava@hotmail.com"
pwd = "Theguru!"

username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("u_0_2")

username.send_keys(user)
password.send_keys(pwd)

submit.click()

wait = WebDriverWait(browser, 5)

# try:
# 	page_load = wait.until_not(lambda browser: browser.current_url == login_page)
# except TimeoutException:
# 	self.fail("Loading tmeout expired")

# self.assertEqual(browser.current_url, correct_page, msg="Successful Login")
