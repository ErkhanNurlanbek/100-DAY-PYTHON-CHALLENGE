import selenium
from numpy.f2py.rules import options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 600
PROMISED_UP = 300
CHROME_OPTIONS = webdriver.ChromeOptions()
CHROME_OPTIONS.add_experimental_option('detach', True)

class InternetSpeedXBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=CHROME_OPTIONS)
        self.down = 0
        self.up = 0
        self.email = 'YOUR_X_EMAIL'
        self.username = 'YOUR_X_USERNAME' # NOTE: a username is a name in x that has @ in the beginning
        self.password = 'YOUR_PASSWORD'

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/ru')
        time.sleep(3)
        start_but = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_but.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.CLASS_NAME, value='download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, value='upload-speed').text
    def tweet_at_provider(self):
        self.driver.get('https://x.com/home')

        time.sleep(10)
        email = self.driver.find_element(By.CSS_SELECTOR, value='input.r-30o5oe')
        email.send_keys(self.email, Keys.ENTER)

        time.sleep(3)
        itisme = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        itisme.send_keys(self.username, Keys.ENTER)

        time.sleep(5)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.password, Keys.ENTER)

        time.sleep(3)
        post_but = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        post_but.click()

        time.sleep(3)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        publish_text = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        publish_text.send_keys(tweet)


bot = InternetSpeedXBot()
bot.get_internet_speed()
bot.tweet_at_provider()



# number result-data-value upload-speed
