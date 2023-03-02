from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("")
ele=driver.find_element(By.XPATH)
act=ActionChains(driver)
act.double_click()

act.click()
act.pause()