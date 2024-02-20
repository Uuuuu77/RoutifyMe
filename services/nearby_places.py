#!/usr/bin/python3

import os
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv

load_dotenv()


def get_nearby_places(location, queries):
    if not isinstance(location, str) or not location:
        raise ValueError("location must be a non-empty string")
    if not isinstance(queries, list) or not all(
           isinstance(query, str) for query in queries):
        raise ValueError("queries must be a list of non-empty strings")

    api_url = "http://dev.virtualearth.net/REST/v1/LocalSearch"
    results = {}

    for query in queries:
        params = {
            'query': query,
            'userLocation': location,
            'key': os.getenv('Bing_Maps_Key'),
        }

        try:
            response = requests.get(api_url, params=params)
            response.raise_for_status()
            results[query] = response.json()
        except RequestException as e:
            raise Exception(f"Request to {api_url} failed: {str(e)}")

    return results
