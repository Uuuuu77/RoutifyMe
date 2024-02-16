#!/usr/bin/python3

import unittest
from unittest.mock import patch, Mock
from services import nearby_places

class TestNearbyPlaces(unittest.TestCase):
    @patch('services.nearby_places.requests.get')
    def test_get_nearby_places_success(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {'some': 'data'}
        mock_get.return_value = mock_response

        # Call the function with a valid location and queries
        result = nearby_places.get_nearby_places('123 Main St', ['coffee', 'pizza'])

        # Check that the function returned the correct data
        self.assertEqual(result, {'coffee': {'some': 'data'}, 'pizza': {'some': 'data'}})

    @patch('services.nearby_places.requests.get')
    def test_get_nearby_places_failure(self, mock_get):
        # Mock the API response to raise an exception
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = nearby_places.RequestException
        mock_get.return_value = mock_response

        # Call the function with a valid location and queries and check that it raises an exception
        with self.assertRaises(Exception):
            nearby_places.get_nearby_places('123 Main St', ['coffee', 'pizza'])

    def test_get_nearby_places_invalid_input(self):
        # Call the function with invalid input and check that it raises a ValueError
        with self.assertRaises(ValueError):
            nearby_places.get_nearby_places('', ['coffee', 'pizza'])
        with self.assertRaises(ValueError):
            nearby_places.get_nearby_places('123 Main St', ['coffee', 123])

if __name__ == '__main__':
    unittest.main()