from selenium import webdriver

chrome_driver_path = "chrome/chrome.exe"
driver = webdriver.Chrome(exec("chrome_driver_path"))

driver.get("https://www.google.com")


# driver.close()
driver.quit()