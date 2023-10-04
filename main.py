from GoogleMapsclient import GoogleMapsClient
import os



def main():
    API_key= os.environ['GoogleMapsAPI']

    client = GoogleMapsClient(api_key=API_key,address= 'roppongi hills mori tower')
    search_nearby_results = client.search_nearby("cafe",radius=200)

    client.pretty_json(search_nearby_results)


if __name__ == "__main__":
    main()