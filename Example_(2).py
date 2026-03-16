Example (5)from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://the-internet.herokuapp.com/login"


# Test Case 1 : Login Success
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(url)

wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
assert "secure area" in message
print("Login Success")

wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
assert "logged out" in message
print("Test Case 1 Passed: Logout Success")

driver.quit()


# Test Case 2 : Password Incorrect
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(url)

wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("Password!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
assert "password is invalid" in message
print("Test Case 2 Passed: Password Incorrect")

driver.quit()


# Test Case 3 : Username Not Found
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get(url)

wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("tomholland")
driver.find_element(By.ID, "password").send_keys("Password!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

message = wait.until(EC.presence_of_element_located((By.ID, "flash"))).text
assert "username is invalid" in message
print("Test Case 3 Passed: Username Not Found")

driver.quit()
