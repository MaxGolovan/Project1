import requests
city = "Moscow,RU"
appid = "833e4aaaaeb7050751f1593238537d59"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
             params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Wind speed", data['wind']['speed'])
print("Visibility", data['visibility'])