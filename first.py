import json
import requests

#r = requests.get('<MY_URI>', headers={'Authorization': 'Bearer <MY_TOKEN>'})
#res = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Montreal,,CA&appid=b26f884059504c801d371a4834ce4623&mode=json')

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'your_access_token'
httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
queryParams = { 'sortBy': 'lastactivity', 'max': '2' }
response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )
print( response.status_code )
print( response.text )

dic = response.json()

print (dic['?'])



