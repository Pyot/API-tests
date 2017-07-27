import  urllib.parse
import requests
import json

main_api ='http://maps.googleapis.com/maps/api/geocode/json?'

address = 'czestochowa halo'

while True:
    address = input('Address: ')
    url =  main_api + urllib.parse.urlencode({'address': address})
    
    print(urllib.parse.urlencode({'address': address}))
    
    json_data = requests.get(url).json()
    
    #print(json_data)
    
    json_status =  json_data['status']
    
    
    print('API Status: ' + json_status + '\n')
    print(url)
    
    if json_status == 'OK': 
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
            
        
        formatted_address =  json_data['results'][0]['formatted_address']
        print(formatted_address)