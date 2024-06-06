#librairies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
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
	dashboardCard = '/html/body/div[3]/div[5]/div/div[2]/div/section/div/aside/section[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div'
	nbDashboardCard = count_elements(driver, dashboardCard)
	print(nbDashboardCard)
	
	if nbDashboardCard > 0:
		# browse dashboard cards
		for i in range(1, nbDashboardCard+1):
			#click on each dashboard 
			dashboardCardText = driver.find_element(By.XPATH, f'/html/body/div[3]/div[5]/div/div[2]/div/section/div/aside/section[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[{i}]/div[1]/div/div/a/span[3]')
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
					print(f"il y a {nbLiInTabs} li a parcourir dans cette section")

					#browse lis
					if nbLiInTabs > 0:
						for k in range(1, nbLiInTabs+1):
							#open side menu
							menuButton = driver.find_element(By.XPATH, '/html/body/div[3]/div[5]/div/div[1]/div/button')
							menuButton.click()
							time.sleep(2)
							#click on each li content
							print(f'li {k} :')
							
							try :
								liText = driver.find_element(By.XPATH, f'/html/body/div[3]/div[4]/div[2]/nav/div/div/div[{j}]/div[2]/ul/li[{k}]/a')
									
								liText.click()
        
								time.sleep(3)
								# check du cadenas
								if(driver.current_url.startswith("https://learning.devinci.fr/mod/resource/")):
									print(f"li {k} est une ressource")

									#SUITE (créer fonction)
								else:
									print(f"li {k} n'est pas une ressource")
									#cas du CM 5 à gérer en algo

								#back to previous page
								driver.back()
								time.sleep(3)

							except: 
								print("Le clic n'a pas pu se faire, tentative de scroll")

								try:
									# Trouver le conteneur qui contient l'élément que vous voulez faire défiler
									drawerContainer = driver.find_element(By.XPATH, '/html/body/div[3]/div[4]/div[2]')

									# Initialiser les variables pour la boucle de défilement
									elementFound = False
									maxScrollAttempts = 10 
									scrollAttempts = 0

									while not elementFound and scrollAttempts < maxScrollAttempts:
										try:
											# Chercher l'élément cible
											driver.execute_script("arguments[0].scrollTop += 50;", drawerContainer)
											scrollAttempts += 1
											time.sleep(1)
											element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[4]/div[2]/nav/div/div/div[{j}]/div[2]/ul/li[{k}]/a')
											elementFound = True
										except:
											print('Erreur de recherche après scroll')

									# Cliquer sur l'élément
									element.click()
									time.sleep(3)
									if(driver.current_url.startswith("https://learning.devinci.fr/mod/resource/")):
										print(f"li {k} est une ressource")

										#SUITE (créer fonction)
									else:
										print(f"li {k} n'est pas une ressource")
										#cas du CM 5 à gérer en algo

									driver.back()
									time.sleep(3)

								except Exception as e:
									print(f"Une erreur est survenue: {e}")
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