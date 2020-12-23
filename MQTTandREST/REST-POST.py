import requests
import json
url = 'https://api.thingspeak.com/update?api_key=YMG26ZD34A06YMMT&'
update = {'field1': 25}
response = requests.get(url, data=update).content
print(response)
