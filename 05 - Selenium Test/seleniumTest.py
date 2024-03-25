import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

edge_service = EdgeService(EdgeChromiumDriverManager().install())

driver = webdriver.Edge(service=edge_service)

driver.get('https://github.com/pedroors')

paginaPrincipal = driver.find_element("xpath", "/html/body/div[1]/div[4]/main/div[1]/div/div/div[2]/div/nav/a[2]")

paginaPrincipal.click()

time.sleep(5.0)

# menuRepositorios = driver.find_element("link text ", "WebScraping-Study")

# menuRepositorios.click()

# paginaPrincipalRepositorio = driver.find_element("xpath", "//*[@id='folder-row-5']/td[2]/div/div/h3/div/a")

# paginaPrincipalRepositorio.click()


driver.quit()
