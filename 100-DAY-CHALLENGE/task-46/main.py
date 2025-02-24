from bs4 import BeautifulSoup
import requests
import smtplib

headers = {
  'headers': {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru,en-US;q=0.9,en;q=0.8,de;q=0.7,ky;q=0.6",
    "Host": "httpbin.org",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-67bc9c96-2fb0b58738c668e37b66b19a"
  }
}
response = requests.get('https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1')

instant_pot = response.text
soup = BeautifulSoup(instant_pot, 'html.parser')
price_or = soup.find( class_='a-offscreen').getText()

print(price_or)
#

price = float(price_or.split('$')[1])
print(type(price))
title = soup.find(id="productTitle").get_text().strip()
print(title)

# From what price and below would you like to get a notification from?
# ↓ ↓ ↓ ↓ ↓
BUY_PRICE = 100

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP('MY_SMTP-ADDRESS', port=587) as connection:
        connection.starttls()
        result = connection.login('randomemail@gmail.com', 'Password')
        connection.sendmail(
            from_addr='randomemail@gmail.com',
            to_addrs='randomemail@gmail.com',
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{'https://appbrewery.github.io/instant_pot/'}".encode("utf-8")
        )