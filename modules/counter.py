from selenium.webdriver.common.by import By

def count_elements(driver, selector):
    elements = driver.find_elements(By.XPATH, selector)
    count = len(elements)
    return count
