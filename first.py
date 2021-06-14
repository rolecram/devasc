import json
import requests

#r = requests.get('<MY_URI>', headers={'Authorization': 'Bearer <MY_TOKEN>'})

res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Montreal,,CA&appid=b26f884059504c801d371a4834ce4623&mode=json')
print(res)
dic = res.json()

print (dic['coords'])



