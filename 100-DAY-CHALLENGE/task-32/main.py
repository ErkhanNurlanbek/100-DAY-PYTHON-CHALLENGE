import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = 'randomgmail@gmail.com'
MY_PASSWORD = 'qwertyuiop'

MY_LAT = 42.829939
MY_LNG = 74.583855
FORMAT = 0
def in_eyesight():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    data = response.json()

    iss_pos = data['iss_position']
    latitude = float(iss_pos['latitude'])
    longitude = float(iss_pos['longitude'])

    if MY_LNG - 5 <= longitude <= MY_LAT + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True

def is_night():
    paramaters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': FORMAT
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=paramaters)
    response.raise_for_status()
    data = response.json()
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])

    time_now = dt.datetime.now()
    hours_now = time_now.hour
    if hours_now >= sunset or hours_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if in_eyesight() and is_night():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f'Subject:ISS ABOVE YOU!\n\nLook up and you will see an ISS above you!!!')