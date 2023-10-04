# GoogleMapsNearbyOptimised

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

| Parameter     | Data Type      | 
|:-------------:|:-------------:|
| Search_location  | STRING | 
| Search_item   | STRING  | 
| radius | INTEGER | 

# Features <a name="Features"></a>
- Search for any term available on Google maps around a specified search location.
- Adjustable radius search parameter for those who are feeling adventurous to increase their walking distance.
- Optimisation of results suggested by Google Maps analysing distance from search location & review.
- Filters out locations with less than 5 reviews.
- Simple console output of location.    

## Acknowledgements <a name="Acknowledgements"></a>
This project was inspired by a video produced by the CodingEntrepeneurs channel. 

## Change Log <a name="Change Log"></a>
V1 - Uploaded to GitHub with main code & README information.
