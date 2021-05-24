from selenium import webdriver
def open_baidu(url):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver