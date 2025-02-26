from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://secure-retreat-92358.herokuapp.com/')
# num = driver.find_elements(By.CSS_SELECTOR, value='#articlecount a')[1]
# num.click()

# portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# portals.click()

search = driver.find_element(By.NAME, value='fName')
search1 = driver.find_element(By.NAME, value='lName')
search2 = driver.find_element(By.NAME, value='email')

search.send_keys('ez', Keys.ENTER)
search1.send_keys('ez', Keys.ENTER)
search2.send_keys('ez@gmail.com', Keys.ENTER)




