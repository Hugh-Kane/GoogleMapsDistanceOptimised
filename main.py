from GoogleMapsclient import GoogleMapsClient
import os



def main():
    API_key= os.environ['GoogleMapsAPI']

    search_location = 'roppongi hills mori tower'
    search_item = "cafe"
    radius = 200
    output_result = 'Short'

    client = GoogleMapsClient(api_key=API_key,address= search_location)
    search_nearby_results = client.search_nearby(search_item,radius=radius,output_result=output_result)

    client.pretty_json(search_nearby_results)


if __name__ == "__main__":
    main()