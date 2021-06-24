# For more information, visit https://developers.google.com/maps/gmp-get-started.

import os
import sys
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv


def load_environment_variables():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        print("The file '.env' was not found. Create it based on '.env.example'.")
        sys.exit()


def make_request(endpoint, params):
    response = requests.get(endpoint + urlencode(params)).json()

    status = response.get("status")
    if status == "OK":
        return response
    if status == "ZERO_RESULTS":
        return {}

    raise Exception(response)


def get_geocode(target):
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json?"
    params = {"address": target, "key": os.environ["API_KEY"]}

    geocode = make_request(endpoint, params)
    if not geocode:
        return {}

    formatted_address = geocode["results"][0]["formatted_address"]
    location = geocode["results"][0]["geometry"]["location"]
    return {"formatted_address": formatted_address, "location": location}


def get_nearby_place_ids(location, keyword, radius):
    endpoint = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    params = {
        "key": os.environ["API_KEY"],
        "location": location,
        "radius": radius,
        "keyword": keyword,
        "opennow": "true",
    }

    places = make_request(endpoint, params)
    if not places:
        return []

    return [place["place_id"] for place in places["results"]]


def get_place_details(place_id):
    endpoint = "https://maps.googleapis.com/maps/api/place/details/json?"
    params = {
        "key": os.environ["API_KEY"],
        "place_id": place_id,
        "fields": "name,formatted_address,formatted_phone_number,url",
    }

    details = make_request(endpoint, params)
    if not details:
        return {}

    for param in params["fields"].split(","):
        details["result"][param] = details["result"].get(param, "Not available.")

    return details["result"]


def main():
    load_environment_variables()

    target = input("Enter the search target (address or place name): ")
    if not target:
        target = "Университет ИТМО"
        print(f"Using the default: '{target}'.")

    geocode = get_geocode(target)
    if not geocode:
        print("\nThe specified address was not found.")
        return
    print(f'\nFound place: {geocode["formatted_address"]}')
    print("Coordinates: {lat:.6f}, {lng:.6f}".format(**geocode["location"]))

    keyword = input("\nEnter the keyword(s) (place name, type, etc.): ")
    if not keyword:
        keyword = "Евразия"
        print(f"Using the default: '{keyword}'.")

    radius = input("\nEnter the search radius (in meters): ")
    if not radius:
        radius = "1500"
        print(f"Using the default: '{radius}'.")
    elif not radius.isdecimal() or int(radius) <= 0:
        print("\nWrong radius. Enter a positive number.")
        return

    location = f'{geocode["location"]["lat"]},{geocode["location"]["lng"]}'
    place_ids = get_nearby_place_ids(location, keyword, radius)
    if not place_ids:
        print("\nNo nearby places were found.")
        return

    dashes = "-" * 80
    for place_id in place_ids:
        details = get_place_details(place_id)
        print("\n" + dashes)
        if details:
            print("Name:   ", details["name"])
            print("Address:", details["formatted_address"])
            print("Phone:  ", details["formatted_phone_number"])
            print("Maps:   ", details["url"])
        else:
            print(f"Skipping {place_id}. It no longer refers to a valid result.")
        print(dashes)


if __name__ == "__main__":
    main()
