#!/usr/bin/python3

import requests
from requests.exceptions import RequestException


def get_nearby_places(location):
    # Check that location is a non-empty string
    if not isinstance(location, str) or not location:
        raise ValueError("location must be a non-empty string")

    api_url = "https://api.example.com/nearby-places"

    try:
        # Send a GET request to the API with the location as a parameter
        response = requests.get(api_url, params={'location': location})

        # Check that the request was successful
        response.raise_for_status()

        # If successful, return the data from the response
        return response.json()

    except RequestException as e:
        # If not successful, raise an exception
        raise Exception(f"Request to {api_url} failed: {str(e)}")
