#!/usr/bin/python3

import unittest
from unittest.mock import patch, Mock
from services import my_location

class TestMyLocation(unittest.TestCase):
    @patch('services.my_location.requests.get')
    def test_get_location_success(self, mock_get):
        # Mock the API response
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {'some': 'data'}
        mock_get.return_value = mock_response

        # Call the function with a valid address
        result = my_location.get_location('123 Main St')

        # Check that the function returned the correct data
        self.assertEqual(result, {'some': 'data'})

    @patch('services.my_location.requests.get')
    def test_get_location_failure(self, mock_get):
        # Mock the API response to raise an exception
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = my_location.RequestException
        mock_get.return_value = mock_response

        # Call the function with a valid address and check that it raises an exception
        with self.assertRaises(Exception):
            my_location.get_location('123 Main St')

    def test_get_location_invalid_input(self):
        # Call the function with invalid input and check that it raises a ValueError
        with self.assertRaises(ValueError):
            my_location.get_location('')

if __name__ == '__main__':
    unittest.main()