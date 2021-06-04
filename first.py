import json
import requests


res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Montreal,,CA&appid=b26f884059504c801d371a4834ce4623&mode=json')
print(res)
jres = res.json()

print (jres['coords'])



