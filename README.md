# GoogleMapsDistanceOptimised

## Table of Contents
- [Introduction](#introduction)
- [Example](#example)
- [Installation](#Installation)
- [Usage](#Usage)
- [Features](#Features)
- [Acknowledgements](#Acknowledgements)
- [Change Log](#subsection-2)

# Introduction <a name="introduction"></a>
🌍✨ Explore Your Ideal Destination with Pinpoint Precision! 📍🚀

Introducing our cutting-edge Python-powered Google Maps API that goes beyond ordinary location searches. 🌟 Discover top-rated places tailored just for you, whether you're a foodie 🍔, an adventurer 🌄, or a culture connoisseur 🏛️.

Our simple API prioritizes proximity, ensuring you're never too far from your next adventure. ⏳ So for those who prefer to take it easy on foot, our API ensures you reach your destination with convenience and ease!



## Example <a name="example"></a>
As one can see, the first cafe listed when searching for cafes nearby the search area - Ark Hills Cafe appears. While this does seem like a nice cafe, it is a 20 minute walk away from the desired location. A similar observation can be made with the top 4 cafes which are recommended - they are too far. 

<img src="https://i.imgur.com/O25fHAN.png" alt="GoogleMaps" style="width: 80%; height: auto;">

With the updated Distance Optimised search, we can see that the top cafes suggested are significantly closer to the search location - requiring substantially less walking & effort to get to these. These cafes are, however, not in a random order & still prioritises rating - hence, providing meaningful cafe suggestions, within walking distance.

<img src="https://i.imgur.com/LniqPNX.png" alt="DistanceOptimizedAPI" style="width: 80%; height: auto;">


## Installation <a name="Installation"></a>
This code utilises two types of API calls to Google Maps Services 
- [Geocoding request and response](https://developers.google.com/maps/documentation/geocoding/requests-geocoding)
- [Nearby Search](https://developers.google.com/maps/documentation/places/web-service/search-nearby)

In order for these API integrations to work, a Google Cloud project & API set-up is required. 
[More information can be found here](https://developers.google.com/maps/documentation/geocoding/cloud-setup)

## Usage <a name="Usage"></a>
Within the main.py document - adjust the following parameters. 

| Parameter     | Data Type      | Description   |
|:-------------:|:-------------:|:-------------:|
| Search_location  | *STRING* |  The point around which to retrieve place information. |
| Search_item   | *STRING*  | The text string on which to search, for example: "restaurant" or "123 Main Street". This must be a place name, address, or category of establishments. Any other types of input can generate errors and are not guaranteed to return valid results. The Google Places service will return candidate matches based on this string and order the results based on their perceived relevance.|
| radius | *INTEGER* | Defines the distance (in meters) within which to return place results. |
| output_result | *STRING* | Please enter Short or Long. Short will output only place name & overall score. Whereas Long will provide extra information. |

### Output
Results are printed out in the console. 
Example of a Short Output:

```
{
    'ANTICO CAFFÈ AL AVIS - Roppongi Hills': 0.041935483870967745,
    'Hills Cafe / Space': 0.03457943925233645,
    'マックカフェ バイ バリスタ': 0.021621621621621623,
    '自家焙煎珈琲 カフェ・タピロス': 0.00898661567877629
}
```

Example of a Long Output: 

```
{
ANTICO CAFFÈ AL AVIS - Roppongi Hills
         place_id:  ChIJL7waDXeLGGARO42nvUJfpaY
         rating:  3.9
         Review Count:  307
         distance:  93
         Overall score:  0.041935483870967745
Hills Cafe / Space
         place_id:  ChIJh8bEDHeLGGARMa5PSjCLM7Q
         rating:  3.7
         Review Count:  362
         distance:  107
         Overall score:  0.03457943925233645
マックカフェ バイ バリスタ
         place_id:  ChIJq8DGnLGLGGAR1MVYCbaOnpE
         rating:  4
         Review Count:  45
         distance:  185
         Overall score:  0.021621621621621623
自家焙煎珈琲 カフェ・タピロス
         place_id:  ChIJgZygiZ2LGGARkaDee5_BaqE
         rating:  4.7
         Review Count:  97
         distance:  523
         Overall score:  0.00898661567877629
}
```


# Features <a name="Features"></a>
- Search for any term available on Google maps around a specified search location.
- Adjustable radius search parameter for those who are feeling adventurous to increase their walking distance.
- Optimisation of results suggested by Google Maps analysing distance from search location & review.
- Filters out locations with less than 5 reviews.
- Simple console output of location.    
- Selection of short & long output depending on if the user would like additional information.

## Acknowledgements <a name="Acknowledgements"></a>
This project was inspired by a video produced by the CodingEntrepeneurs channel. 

## Change Log <a name="Change Log"></a>
V1 - Uploaded to GitHub with main code & README information.
