from urllib.parse import urlencode
import requests
import json
import os

API_key= os.environ['GoogleMapsAPI']

def save_json_to_file(json_data, file_path):
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

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

def pretty_json(json_data):
    pretty_json = json.dumps(json_data, indent=2)
    print(pretty_json)

def extrac_lat_lng(address_or_postalcode,data_type = 'json'):

    endpoint=f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address":address_or_postalcode,"key" : API_key}
    url_params = urlencode(params)
    #print(url_params)

    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200,299):
        return {}
    
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
    except:
        pass
    return latlng.get("lat"),latlng.get("lng")

#print(extrac_lat_lng("1600 Amphitheatre+Parkway, Mountain View, CA"))
print(extrac_lat_lng("MSQ office London"))

def find_place(lat,lng):

    radius = 1000
    endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    parameters = {"input":"corner shop",
                "inputtype": "textquery",
                "fields":"formatted_address,name,geometry,price_level,rating",
                #"locationbias":f"point:{radius}@{lat},{lng}",
                "locationbias":f"circle:{radius}@{lat},{lng}",
                "key" : API_key}
    url_params = urlencode(parameters)

    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200,299):
        {}
    print(pretty_json(r.json()))

def nearby_search(lat,lng):
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    parameters = {
        "keyword": "japanese restaurant",
        "location" : f"{lat},{lng}",
        "radius": 50,
        "key" : API_key,
        "rankby":"prominence"
    }
    url_params = urlencode(parameters)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200,299):
        return {}
    output = r.json()
    save_json_to_file(output, "output.json")


#lat,lng = 51.5132325, -0.1216635 ### MSQ office
#lat,lng = 35.652832, 139.839478 ### Tokyo

#find_place(lat,lng)
#nearby_search(lat,lng)

"""
file_path= 'output.json'
data = read_json_from_file(file_path)
pretty_json(data)
"""

data = read_json_from_file('output.json')
#pretty_json(data)
search_data = []
for dictionary in data['results']:
    location_data = {}
    location_data['name'] = dictionary['name']
    location_data['latlng'] = dictionary['geometry']['location']
    location_data['rating'] = dictionary['rating']
    #dict_keys(['business_status', 'geometry', 'icon', 'icon_background_color', 'icon_mask_base_uri', 'name', 'opening_hours', 'photos', 'place_id', 'plus_code', 'rating', 'reference', 'scope', 'types', 'user_ratings_total', 'vicinity'])
    search_data.append(location_data)

print(search_data)
