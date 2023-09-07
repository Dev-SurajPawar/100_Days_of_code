from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "chrome/chrome.exe"
driver = webdriver.Chrome(exec("chrome_driver_path"))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

search = driver.find_elements_by_css_selector("cdx-text-input__input")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
