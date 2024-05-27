from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def authenticate(driver, username, password):
    # Open connexion page
    driver.get("https://learning.devinci.fr/")
    time.sleep(5)
    
    # Find input fields
    username_field = driver.find_element(By.ID, "userNameInput")
    password_field = driver.find_element(By.ID, "passwordInput")

    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit form
    password_field.send_keys(Keys.RETURN)

    time.sleep(7)