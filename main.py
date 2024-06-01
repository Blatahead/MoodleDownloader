#librairies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
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

	# Count number of dashboard card by path
	dashboardCard = '/html/body/div[3]/div[5]/div/div[2]/div/section/div/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div'
	nbDashboardCard = count_elements(driver, dashboardCard)
	
	if nbDashboardCard > 0:
		# browse dashboard cards
		for i in range(1, nbDashboardCard+1):
			#click on each dashboard 
			dashboardCardText = driver.find_element(By.XPATH, f'/html/body/div[3]/div[5]/div/div[2]/div/section/div/aside/section[1]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[{i}]/div[1]/div/div/a/span[3]')
			dashboardCardText.click()
			time.sleep(3)

			#count number of course section by path
			courseSection = '/html/body/div[3]/div[4]/div[2]/nav/div/div/div'
			nbCourseSection = count_elements(driver, courseSection)
			print(f'Nombre de section : {nbCourseSection}')

			# browse course sections
			if nbCourseSection > 0:
				for j in range(1, nbCourseSection+1):
					#count number of li by path
					liInTabs = f'/html/body/div[3]/div[4]/div[2]/nav/div/div/div[{j}]/div[2]/ul/li'
					nbLiInTabs = count_elements(driver, liInTabs)
					print(nbLiInTabs)

					#browse lis
					if nbLiInTabs > 0:
						for k in range(1, nbLiInTabs+1):
							#open side menu
							menuButton = driver.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/div[1]/div/button')
							menuButton.click()
							time.sleep(2)

							#click on each li content
							print(f'li {k} :')
							liText = driver.find_element(By.XPATH, f'/html/body/div[3]/div[4]/div[2]/nav/div/div/div[{j}]/div[2]/ul/li[{k}]/a')
							liText.click()
							time.sleep(3)

							#back to previous page
							driver.back()
							time.sleep(3)
					else:
						print("Aucun élément dans ce li")
			else:
				print("Aucun élément dans cette matière")
    
			time.sleep(4)
			driver.back()
			time.sleep(3)
	else:
		print("Aucun élément trouvé.")

finally:
    driver.quit()