#  used to get real time weather data.
#  requires internet.

import requests

api_key = "f0f7eeabf8c37b30277f88027e4c35ae"
city_name = input("Enter city name:  ")
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
data = response.json()

#  getting data from main
humidity = data['main']['humidity']
pressure = data['main']['pressure']
wind = data['wind']['speed']
description = data['weather'][0]['description']
temp = data['main']['temp']
c = temp - 273.15
#  convert into kelvin into celcius
print('Temperature:', c, '°C')
print('Wind:', wind, 'km/h')
print('Pressure: ', pressure, 'bar')
print('Humidity: ', humidity, '%')
print('Description:', description, 'in', city_name)
