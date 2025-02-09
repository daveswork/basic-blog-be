import requests
import pprint
import os
from dotenv import load_dotenv

load_dotenv()

# response = requests.get("https://official-joke-api.appspot.com/random_joke")
#
# print(response)
# print(response.json()['setup'])
# print(response.json()['punchline'])

#
# parameters = {
#     "lat":40.678177,
#     "lng":-73.944160,
#     "formatted":0
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# pprint.pprint(response.json())


apikey = os.environ.get("OWM_API_KEY")
print(apikey)

# paris = {
#     "lat": 48.856613,
#     "long": 2.352222
# }
#
# # https://api.openweathermap.org/data/2.5/weather?q=paris&appid=2faf60adf7504fd840155ff6dc78b7c2
#
api_params = {
    "q" : "Paris",
    "appid": apikey,
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=api_params)
pprint.pprint(response.json())