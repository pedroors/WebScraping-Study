import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument('window-size=400,800')

driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

url = 'https://www.airbnb.com.br/'

driver.get(url)

codigoFonte = driver.page_source

site = BeautifulSoup(codigoFonte, 'html.parser')

print(site)


# print(site.prettify())