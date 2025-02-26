from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)


driver.get('https://www.python.org/')


# search = driver.find_element(By.NAME, value='q')
# print(search.get_attribute('placeholder'))
# button = driver.find_element(By.ID, 'submit')
# print(button.size)
# print(driver.find_element(By.CSS_SELECTOR, value='.documentation-widget a').text)
#
# code = driver.find_element(By.XPATH, value='//*[@id="dive-into-python"]/ul[2]/li[1]/div[1]/pre/code')
# print(code.text)

idk = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul li time')
idk1 = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul li a')
upcoming_events = {}
for i in range(len(idk)):
    time = idk[i].text
    event = idk1[i].text
    upcoming_events[i] = {'time': time, 'event': event}

print(upcoming_events)





# whole = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# print(f'This is the price rn: {whole.text}.{cents.text}')

# driver.close()
# driver.quit()
driver.quit()

