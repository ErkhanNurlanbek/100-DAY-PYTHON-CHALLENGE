from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/experiments/cookie/')




cookie = driver.find_element(By.ID, value='cookie')


items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
every_item = []
for item in items:
    every_item.append(item.get_attribute('id').strip())



timeout = time.time() + 5
fiv_min = time.time() + 60 * 5
while True:
    cookie.click()
    cps = driver.find_element(By.ID, value='cps').text
    if time.time() > fiv_min:
        print(cps)
        break

    if time.time() > timeout:
        money = int(driver.find_element(By.ID, value='money').text)
        prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        prices.pop(len(prices) - 1)
        costs = [int(price.text.split()[-1].replace(',', '')) for price in prices]
        for i, price in enumerate(costs):
            if money >= price:
                item = driver.find_element(By.ID, value=every_item[i])
                item.click()








