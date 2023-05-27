from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

inputUsername = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
inputUsername.send_keys("standard_user")

inputPassword = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
inputPassword.send_keys("secret_sauce")

driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]").click()

inputFirstName = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
inputFirstName.send_keys("Adam")
inputLastName = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
inputLastName.send_keys("Rafif")
inputPostalCode = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")
inputPostalCode.send_keys("177013")

driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div[9]/button[2]").click()

driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/button").click()


driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button").click()
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/nav/a[3]").click()


while True:
    continue