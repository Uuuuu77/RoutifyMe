#!/usr/bin/python3

import os
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv()


def get_location(address):
    # Check that address is a non-empty string
    if not isinstance(address, str) or not address:
        raise ValueError("address must be a non-empty string")

    api_url = "http://dev.virtualearth.net/REST/v1/Locations"

    params = {
        'query': address,
        'key': os.getenv('Bing_Maps_Key'),
    }

    try:
        # Send a GET request to the API with the address as a parameter
        response = requests.get(api_url, params=params)

        # Check that the request was successful
        response.raise_for_status()

        # If successful, return the data from the response
        return response.json()

    except RequestException as e:
        # If not successful, raise an exception
        raise Exception(f"Request to {api_url} failed: {str(e)}")
