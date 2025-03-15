import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup
import requests
import time

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
instant_pot = response.text
# print(instant_pot)
soup = BeautifulSoup(instant_pot, 'html.parser')

k = soup.select('.StyledPropertyCardDataWrapper a')
u_list = [tag.get('href') for tag in k]

b = list(soup.find_all(class_='PropertyCardWrapper__StyledPriceLine'))
p_list = [x.getText().split()[0].strip() for x in b]

l = list(soup.select('ul li address'))
a_list = [x.getText().strip() for x in l]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
for i in range(len(u_list)):
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScAaUGdcbPD5ERsPnqNkAiH1NY7g_oNT3yUEYeQwNuF8QNYUg/viewform?usp=dialog')
    time.sleep(2)

    address = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(a_list[i])

    price = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(p_list[i])

    link = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(u_list[i])

    submit_but = driver.find_element(By.XPATH, value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_but.click()