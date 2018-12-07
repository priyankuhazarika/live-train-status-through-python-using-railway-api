#Python program to check availability of seats of a particular train
#using RAILWAY API

import requests, json

#enter the api key
api_key = "m6vhuffq8k"

#base url variable to store the url
base_url = "https://api.railwayapi.com/v2/check-seat/train/"

#enter the train number
train_number = raw_input("Enter the train number: ")

#enter the source station code
source_station_code = raw_input("Enter the source station code (in block letters): ")

#enter the destination station code
destination_station_code = raw_input("Enter the destination station code (in block letters): ")

#enter he date of journey
journey_date = raw_input("Enter the date in dd-mm-yy format: ")

#enter the class in which you want to travel
journey_class = raw_input("Enter the journey class (CC for Chair Car/ SL for sleeper/ FC for first class/ 1A for AC first class/ 2A for AC 2-tier/ 3A for AC 3-Tier/ 2S for second sitting), enter in block letters: ")

#enter the quota
journey_quota = raw_input("Enter the quota (GN for general/ CK for tatkal quota), please enter in block letters: ")



#complete url variable to store complete url address
complete_url = base_url + train_number + "/source/" + source_station_code + "/dest/" + destination_station_code + "/date/" + journey_date + "/pref/" + journey_class + "/quota/" + journey_quota + "/apikey/" + api_key + "/"

#get method of request module
#return response object
response_ob = requests.get(complete_url)

#json method of response object. Convert
#json format data to python format data
result = response_ob.json()

if result["response_code"] == 200:

    #train name is extracting from
    #the result variable data
    train_name = result["train"]["name"]

    print("Train Name: " + str(train_name))

    #availibility
    seats_available = result["availability"]

    #looping through availibility
    for seats in seats_available:
        date = seats["date"]
        current_status = seats["status"]

        print("Availability:" 
        + "\nDate: " + str(date)
        + "\nStatus: " + str(current_status))
    


else:
    print("Record is not found for given request")

    
