import  urllib.parse
import requests
import json

main_api ='http://maps.googleapis.com/maps/api/geocode/json?'

address = 'czestochowa'
url =  main_api + urllib.parse.urlencode({'address': address})

json_data = requests.get(url).json()

json_status =  json_data['status']
print('API Status: ' + json_status)