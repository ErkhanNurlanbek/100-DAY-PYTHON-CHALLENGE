import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


USERNAME = input('ENTER_YOUR_INSTAGRAM_USERNAME_OR_EMAIL_OR_PHONENUM:')
PASSWORD = input('YOUR_INSTAGRAM_PASSWORD:')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(chrome_options)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5)
username = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[1]/div/label/input')
password = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div[2]/div/form/div[1]/div[2]/div/label/input')
time.sleep(3.5)
username.send_keys(USERNAME)
time.sleep(4.2)
password.send_keys(PASSWORD)
time.sleep(3.4)
password.send_keys(Keys.ENTER)

time.sleep(15.4)
# notnow = driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div[2]/div/div/div[1]')
# notnow.click()

time.sleep(6.2)

search = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div')
search.click()

time.sleep(5.8)

inp = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
inp.send_keys('chefsteps')

time.sleep(3.2)

click = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div')
click.click()

time.sleep(3.4)
followers_but = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span')
followers_but.click()


time.sleep(5.6)
follow = driver.find_elements(By.CSS_SELECTOR, value='.xyi19xy.x1ccrb07.xtf3nb5.x1pc53ja.x1lliihq.x1iyjqo2.xs83m0k.xz65tgg.x1rife3k.x1n2onr6 .x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3  ._acan._acap._acat._aj1-._ap30')
for foll in follow:
    try:
        foll.click()
        time.sleep(1.5)
    except ElementClickInterceptedException:
        cancel = driver.find_element(By.XPATH, value='/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
        cancel.click()


# search[3].click()


