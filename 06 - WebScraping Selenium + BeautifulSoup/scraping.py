import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_service = ChromeService(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument('window-size=400,800')

driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

url = 'https://www.airbnb.com.br/'

driver.get(url)

cookie_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-application']/div/div/div[1]/div/div[4]/section/div[2]/div[2]/button")))
cookie_input.click()

input_place = driver.find_element(By.XPATH, "//*[@id='react-application']/div/div/div[1]/div/div[3]/div/div/div[3]/div/div[1]/div/div[1]/div/div/div/div[1]/button")
input_place.click()

sleep(1)

second_input_place = driver.find_element(By.XPATH, "//*[@id='accordion-body-/homes-where']/section/div[1]/button")
second_input_place.click()

sleep(1)

third_input_place = driver.find_element(By.XPATH, "//*[@id='/homes-where-input']")
third_input_place.send_keys('São Paulo')
third_input_place.submit()

sleep(1)

next_button = driver.find_element(By.XPATH, "//*[@id='accordion-body-/homes-when']/section/div/footer/button[2]")
next_button.click()

sleep(1)

people_quantity_button = driver.find_element(By.XPATH, "//*[@id='stepper-adults']/button[2]")
people_quantity_button.click()

search_houses_button = driver.find_element(By.XPATH, "//*[@id='vertical-tabs']/div[3]/footer/button[2]/span[1]/span")
search_houses_button.click()
sleep(5)

house_page_url = driver.current_url

print("Url da página: ", house_page_url)

house_page_content = driver.page_source

house_page = BeautifulSoup(house_page_content, 'html.parser')

# print(house_page.prettify())

house_infos = house_page.findAll('div', attrs={'class': 'g1qv1ctd'})

# print("Titulo das casas:\n")
for house_info in house_infos:

    house_title = house_info.find('div', attrs={'class': 't1jojoys'})
    print("\nTitulo das casas:\n")
    print(house_title.text)
