
import requests


City = raw_input ('Enter Your City :')
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=53432764958a35b06711b552687a535e'.format(City)
response = requests.get(url)
data = response.json()

Temperature = data['main']['temp']
Wind_Speed = data['wind']['speed']
Latitude = data['coord']['lat']
Longitude = data['coord']['lon']
Description = data['weather'][0]['description']


print('Temperature :{} degree C'.format(Temperature))
print('Wind Speed :{} m/s'.format(Wind_Speed))
print('Latitude :{} degree'.format(Latitude))
print('Longitude :{} degree'.format(Longitude))
print('Description :{}'.format(Description))