#!/usr/bin/python3

import requests
from requests.exceptions import RequestException

def get_my_location():
    # This is a placeholder URL - replace with the URL of the actual API you're using
    api_url = "https://api.example.com/my-location"

    try:
        # Send a GET request to the API
        response = requests.get(api_url)

        # Check that the request was successful
        response.raise_for_status()

        # If successful, return the data from the response
        return response.json()

    except RequestException as e:
        # If not successful, raise an exception
        raise Exception(f"Request to {api_url} failed: {str(e)}")