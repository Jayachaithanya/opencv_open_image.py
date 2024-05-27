#  used to get real time weather data.
#  requires internet.

import requests

api_key = "f0f7eeabf8c37b30277f88027e4c35ae"
city_name = input("Enter city name:  ")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
data = response.json()

humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']
c = temp - 273.15
print('Temperature:', c, '°C')
print('Wind:', wind)
print('Pressure: ', pressure)
print('Humidity: ', humidity)
print('Description:', description)
