import time
from selenium import webdriver

#This part of code it is for use on MS Edge WebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
# edge_service = EdgeService(EdgeChromiumDriverManager().install())
# driver = webdriver.Edge(service=edge_service)

#And this is for use on Google Chrome WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = Options()
# Add any additional options if needed
# chrome_options.add_argument("--headless")  # Example of adding a headless argument

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://github.com/pedroors')

paginaPrincipal = driver.find_element("xpath", "/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]")

paginaPrincipal.click()

time.sleep(1.0)

menuRepositorios = driver.find_element("xpath", "//*[@id='user-repositories-list']/ul/li[1]/div[1]/div[1]/h3/a")

menuRepositorios.click()

time.sleep(1.0)

paginaPrincipalRepositorio = driver.find_element("xpath", "//*[@id='folder-row-5']/td[2]/div/div/h3/div/a")

paginaPrincipalRepositorio.click()

time.sleep(1.0)

paginaCodigo = driver.find_element("xpath", "//*[@id='folder-row-1']/td[2]/div/div/h3/div/a")

paginaCodigo.click()

time.sleep(2.0)

driver.quit()
