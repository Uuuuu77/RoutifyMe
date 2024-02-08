#!/usr/bin/python3

import requests

def get_my_location():
    # This is a placeholder URL - replace with the URL of the actual API you're using
    api_url = "https://api.example.com/my-location"

    # Send a GET request to the API
    response = requests.get(api_url)

    # Check that the request was successful
    if response.status_code == 200:
        # If successful, return the data from the response
        return response.json()
    else:
        # If not successful, raise an exception
        raise Exception(f"Request to {api_url} failed with status code {response.status_code}.")