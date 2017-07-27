# -*- coding: utf-8 -*-
import  urllib.request
import json

apiUrl = "http://www.nhtsa.gov/webapi/api/SafetyRatings"
apiParam = "/modelyear/2013/make/audi/model/a4"
#apiParam = "/VehicleId/7045" uzyc tego do wybranego modelu
outputFormat = "?format=json"


#Combine all three variables to make up the complete request URL
response = urllib.request.urlopen(apiUrl + apiParam + outputFormat)
s= response.read()
print (response.read())


#code below is only to handle JSON response object/format
#use equivalent sets of commands to handle xml response object/format
json_obj = json.loads(s)

#Load the Result (vehicle collection) from the JSON response
print ('------------------------------')

for objectCollection in json_obj['Results']:
	# Loop each vehicle in the vehicles collection
    for safetyRatingAttribute, safetyRatingValue in objectCollection.items():
        print (safetyRatingAttribute, ": ", safetyRatingValue)

# After running this example, feel free to explore the results below