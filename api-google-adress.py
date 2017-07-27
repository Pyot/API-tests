import  urllib.parse
import requests
import json

main_api ='http://maps.googleapis.com/maps/api/geocode/json?'

address = 'czestochowa'
url =  main_api + urllib.parse.urlencode({'address': address})

json_data = requests.get(url).json()

print(json_data)

json_status =  json_data['long_name']


print('API Status: ' + json_status)