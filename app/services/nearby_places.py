#!/usr/bin/python3

import requests

def get_nearby_places(location):
    # This is a placeholder URL - replace with the URL of the actual API you're using
    api_url = "https://api.example.com/nearby-places"

    # Send a GET request to the API with the location as a parameter
    response = requests.get(api_url, params={'location': location})

    # Check that the request was successful
    if response.status_code == 200:
        # If successful, return the data from the response
        return response.json()
    else:
        # If not successful, raise an exception
        raise Exception(f"Request to {api_url} failed with status code {response.status_code}.")