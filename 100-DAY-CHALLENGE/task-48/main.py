from types import NoneType
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4167920892&f_AL=true&geoId=92000000&keywords=Python-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R')
but = driver.find_element(By.XPATH, value='//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
but.click()

email = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_key"]')
password = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal_session_password"]')
signin = driver.find_element(By.XPATH, value='//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')



email.send_keys('randomemail@gmail.com')
password.send_keys('password')
signin.click()



time.sleep(30)
send_job = driver.find_elements(By.CSS_SELECTOR, value='div div div div ul li')

b = []

for li in send_job:
    x = li.get_attribute('id')
    if 'ember' in x:
        b.append(x)
    else:
        pass

rand = random.choice(b)

rand_ = driver.find_element(By.ID, value=rand)
rand_.click()
time.sleep(5)
apply = driver.find_element(By.CSS_SELECTOR, value='button.jobs-apply-button')
apply.click()
time.sleep(5)
number = driver.find_element(By.CSS_SELECTOR, value='input.artdeco-text-input--input')
number.send_keys('123456789')
time.sleep(2)
apply_but = driver.find_element(By.CSS_SELECTOR, value='button.artdeco-button--2')
apply_but.click()

# "artdeco-button artdeco-button--2 artdeco-button--primary ember-view"
# 'artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view artdeco-modal__dismiss'
# ids = []
#
# for i, job in enumerate(send_job):
#     attr = job.get_attribute('data-job-id')
#     if type(attr) == NoneType:
#         send_job.pop(i)
#     else:
#         ids.append(attr)
#
#
# rand = random.choice(ids)
# print(rand)
# rand_ = driver.find_element(By.CSS_SELECTOR, value=f'#{rand}')
# rand_.click()


