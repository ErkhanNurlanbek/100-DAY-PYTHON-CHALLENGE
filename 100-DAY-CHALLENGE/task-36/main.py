import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'erkhan'
TOKEN = 'MY TOKEN'
GRAPH_ID = 'graph2'

params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Treadmill',
    'unit': 'Km',
    'type': 'float',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime(year=2025, month=1, day=27) #.now()
# https://www.w3schools.com/python/python_datetime.asp
# FORMATING ANY DATA INTO THE ONE YOU WANT LESSON 284

pixel_params = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '8',
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response.text)
update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}'
update_params = {
    'quantity': '2'
}


response = requests.post(url=update_endpoint, json=update_params, headers=headers)
print(response.text)