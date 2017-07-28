import  urllib.parse
import requests
import json


base_url = r'https://api.waqi.info/map/bounds/?latlng=49.0020252,14.1228641,54.9054761,24.1458932&token=17e0fbc5712fd203efceed403b9c1102a4648e79'

json_data = requests.get(base_url).json()

#wyciagamy numery baz meteorologicznych
base_number = []

for base_num in json_data['data']:
    #print(base_num['uid'])
    base_number.append(base_num['uid'])
    


#tworzymy adres dla poszczegolnych miast
url_main = r'https://api.waqi.info/feed/@'
url_city_uid = '8122'
url_token = r'/?token=17e0fbc5712fd203efceed403b9c1102a4648e79'

url_city = url_main + url_city_uid + url_token

json_data_city = requests.get(url_city).json()

city_data = json_data_city['data']
base_name = json_data_city['data']['city']['name']

#baza miast zidentyfikowanych po numerze z base_number
city_base = []

for i, id_number in enumerate (base_number):
    city = []
    url_city = url_main + str(id_number) + url_token
    json_data_city = requests.get(url_city).json()
    city.append(base_number[i])
    city.append(json_data_city['data']['city']['name'])
    city_base.append(city)
    
    
