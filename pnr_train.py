#Python program to find live train
#status sing RAILWAY API

#import required modules
import requests, json

#enter the api key
api_key = "m6vhuffq8k"

#base_url variable to store url
base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"

#enter the pnr number
pnr_number = raw_input("Enter your PNR number: ")



#complete url variable to
#store complete url address
complete_url = base_url + pnr_number + "/apikey/" + api_key + "/"

#get method of request module
#return response object
response_ob = requests.get(complete_url)

#json method of response object convert
#json format data to python format data
result = response_ob.json()


#now result contains list of nested dictionaries
# check the value of "response_code" key is equal
# to "200" or not if equal that means record is found
# otherwise record is not found
if result["response_code"] == 200:

    #the train name is extracting from
    # the result variable data
    train_name = result["train"]["name"]

    #the train nmber is extracting from
    #the result variable data
    train_number = result["train"]["number"]

    #from station name is exracting from
    #the result variable data
    from_station = result["from_station"]["name"]

    #to station name is extracting from
    #the result variable data
    to_station = result["to_station"]["name"]

    #boarding point is extracting from
    #the result variable data
    boarding_point = result["boarding_point"]["name"]

    #reservation upto is extracting from
    #the result variable data
    reservation_upto = result["reservation_upto"]["name"]

    #pnr number is extracting from
    #the result variable data
    pnr_number = result["pnr"]

    #date of journey is extracting from
    #the result variable data
    date_of_journey = result["doj"]

    #total number of passengers is extracting from
    #the result variable data
    total_passengers = result["total_passengers"]

    #passengers list is extracting from
    #the result variable data
    passengers_list = result["passengers"]


    #journey class extracting from
    #result variable data
    journey_class = result["journey_class"]["name"]

    #chart prepared or not
    chart_prepared = result["chart_prepared"]

    
    
    #print following values
    print("train name: " + str(train_name)
    + "\ntrain number: " + str(train_number)
    + "\npnr number: " + str(pnr_number)
    + "\nfrom station: " + str(from_station)
    + "\nto station: " + str(to_station)
    + "\nboarding point: " + str(boarding_point)
    + "\nreservation upto: " + str(reservation_upto)
    + "\ndate of journey: " + str(date_of_journey)
    + "\ntotal passengers: " + str(total_passengers)
    + "\njourney class: " + str(journey_class)
    + "\nchart prepared: " + str(chart_prepared))

    #looping through passengers list
    for passenger in passengers_list:

        #store the value or data
        #of "no" key in variable
        passenger_number = passenger["no"]

        #store the value or data
        #of current status in variable
        current_status = passenger["current_status"]

        #store the value or data
        #of booking status key in variable
        booking_status = passenger["booking_status"]


        #print the following values
        print("passenger number: " + str(passenger_number)
        + "\ncurrent status: " + str(current_status)
        + "\nbooking status:" + str(booking_status))

else:
    print("record is not found for given request")