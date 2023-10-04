from urllib.parse import urlencode
import requests
import json
import os 
import heapq
import pandas as pd


"""
Google API code:

Geo code - insert address & google maps will spit out the lat, lng of the location. 
more info here: https://developers.google.com/maps/documentation/geocoding/requests-geocoding

Places API - Nearby Search will search the given keyword based on the lat lng extracted from above. 
Find Place is also available, but this only pulls data on the closest matching item, where as Nearby search provides a few options.
"""




class GoogleMapsClient:
    lat = None
    lng = None
    api_key = None
    location_query = None
    data_type= 'json'
    origin_place_id = None
    output_result = 'Short'


    def __init__(self,api_key=None,address=None):
        print("initialising")
        if api_key == None:
            raise Exception("API key is required")
        self.api_key = api_key
        if self.location_query == None:
            self.extract_lat_lng(address)

    def extract_lat_lng(self,location = None):
        loc_query = self.location_query
        if location != None:
            loc_query = location
        endpoint=f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"address":loc_query,"key" : self.api_key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
            origin_place_id = r.json()['results'][0]['place_id']
        except:
            pass
        lat,lng=latlng.get("lat"),latlng.get("lng")
        self.lat = lat
        self.lng = lng
        self.origin_place_id = origin_place_id
        return lat,lng
    
    def search_nearby(self,keyword="corner shop",radius=500,location=None,output_result = None):
        lat = self.lat
        lng = self.lng
        if location != None:
            lat,lng = self.extract_lat_lng(location)
        if output_result:
            self.output_result = output_result
        endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        parameters = {
            "keyword": keyword,
            "location" : f"{lat},{lng}",
            "radius": radius,
            "key" : self.api_key,
            "rankby":"prominence"
        }
        url_params = urlencode(parameters)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        
        output = r.json()
        self.save_json_to_file(output, "output.json")

        location_data = self.extract_key_info_helper()
        location_data = self.append_distance_to_dictionary(location_data)
        self.sort_through_list(location_data)
        return None
    
    def append_distance_to_dictionary(self,search_nearby_results):
        for result,values in search_nearby_results.items():
        # finding distance between origin & the search_nearby result
            distance = self.distance_calculator(self.origin_place_id,values['place_id'])
            search_nearby_results[result]['distance'] = distance
            search_nearby_results[result]['Overall score'] =search_nearby_results[result]['rating']*(1/distance)
        return search_nearby_results
    
    def sort_through_list(self,search_nearby_results):
        # Convert the data into a list of tuples (park name, Overall score)
        scores = [(-search_data["Overall score"],location_name) for location_name, search_data in search_nearby_results.items()]

        # Convert the list into a min-heap
        heapq.heapify(scores)

        # Now, scores contains the locations sorted by Overall score in ascending order (min-heap)
        # To get the locations in order, you can pop elements from the heap.

        while scores:
            overall_score,location_name = heapq.heappop(scores)
            if self.output_result == "Long":
                #print(f"{location_name}: {search_nearby_results[location_name]}")
                print(f"{location_name}")
                for key,value in search_nearby_results[location_name].items():
                    print(f"         {key}:  {value}")
                
            elif self.output_result == "Short":
                print(f"{location_name}: {search_nearby_results[location_name]['Overall score']}")
            else:
                raise Exception("Please input a correct output_result \n either 'short' or 'long'")

    
    def extract_key_info_helper(self):
        with open('output.json', 'r') as json_file:
            data = json.load(json_file)
            output_data = {}
            for result in data["results"]:
                if result["user_ratings_total"]>5:
                    output_data[result["name"]] = {"place_id":result["place_id"],"rating":result["rating"],"Review Count":result["user_ratings_total"]}
            return output_data
        
    def save_json_to_file(self,json_data, file_path):
        # Convert the JSON data to a formatted string
        if isinstance(json_data, dict):
            json_string = json.dumps(json_data, indent=2)
        elif isinstance(json_data, str):
            # If the input is already a JSON string, assume it's formatted correctly
            json_string = json_data
        else:
            raise ValueError("Input must be a JSON string or a dictionary.")
        # Open the file in write mode and save the JSON data to it
        with open(file_path, 'w') as file:
            file.write(json_string)

    def pretty_json(self,json_data):
        pretty_json = json.dumps(json_data, indent=2)
        print(pretty_json)

    def distance_calculator(self,origin_placeID,destination_placeID):
        # Example Place_id's
        MSQ = 'ChIJ4d0-OikbdkgRa82KHUBGAsY'
        Brewdog = 'ChIJz2raGbUddkgR1EBfTLADLtI'
        HeathrowT3 = 'ChIJka-kLi1ydkgR_2C4JIT5f44'
        E15_2GR = 'ChIJM6AXmkQddkgRbQwaupFm1h0'

        outputformat = 'json'
        endpoint = f'https://maps.googleapis.com/maps/api/distancematrix/{outputformat}'


        params = {
            'key' : self.api_key,
            'origins': f"place_id:{origin_placeID}",
            #'destinations': f"place_id:{E15_2GR}|place_id:{MSQ}",
            'destinations': f"place_id:{destination_placeID}",
            'mode': "walking"
        }
        url_params = urlencode(params)

        url = f"{endpoint}?{url_params}"
        #print(url_params)
        try:
            r = requests.get(url)
            #self.pretty_json(r.json())
            duration = r.json()['rows'][0]['elements'][0]['distance']['value']
        except KeyError:
            print("Error: 'duration' key not found in JSON response")
            duration = None  # Set duration to None or handle it as needed
        return duration
    