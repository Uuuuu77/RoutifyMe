#!/usr/bin/python3

import unittest
from unittest.mock import patch, Mock
from flask import Flask
from services import route_finder

class TestRouteFinder(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(route_finder.route_finder)
        self.client = self.app.test_client()

    @patch('services.route_finder.requests.get')
    def test_optimize_route_success(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {'resourceSets': [{'resources': [{'routeLegs': [{'endLocation': 'Location A'}]}]}]}
        mock_get.return_value = mock_response

        # Call the function with a valid request
        response = self.client.post('/optimize', json={'locations': ['Location A', 'Location B']})

        # Check that the function returned the correct data
        self.assertEqual(response.get_json(), ['Location A'])

    @patch('services.route_finder.requests.get')
    def test_optimize_route_failure(self, mock_get):
        # Mock the API response to raise an exception
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = route_finder.RequestException
        mock_get.return_value = mock_response

        # Call the function with a valid request and check that it raises an exception
        response = self.client.post('/optimize', json={'locations': ['Location A', 'Location B']})
        self.assertEqual(response.status_code, 500)

    def test_optimize_route_invalid_input(self):
        # Call the function with invalid input and check that it returns a 400 status code
        response = self.client.post('/optimize', json={'locations': ['Location A']})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()