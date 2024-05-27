#librairies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#personnal
from modules.authentication import authenticate
from modules.counter import count_elements
from config.config import MOODLE_EMAIL, MOODLE_PASSWORD

# Use Chrome
options = Options()
# options.add_argument("--headless") 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
	authenticate(driver, MOODLE_EMAIL, MOODLE_PASSWORD)

	# Count number of element by path
	selector = '/html/body/div[3]/div[5]/div/div[2]/div/section/div/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div'
	count = count_elements(driver, selector)
	
	if count > 0:
		# browse all dashboard cards
		for i in range(1, count+1):
			dashboardCardText = driver.find_element(By.XPATH, f'/html/body/div[3]/div[5]/div/div[2]/div/section/div/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[{i}]/div[1]/div/div/a/span[3]')
			dashboardCardText.click()
			time.sleep(4)
			driver.back()
			time.sleep(3)
	else:
		print("Aucun élément trouvé.")

finally:
    driver.quit()