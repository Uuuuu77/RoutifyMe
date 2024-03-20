#!/usr/bin/python3

import unittest
from models.location import Location, db


# Unit test class for testing Location model
class LocationTest(unittest.TestCase):
    # Test case for creating a location
    def test_create_location(self):
        # Create a new location object
        location = Location(name='Test Location', address='123 Test St')

        # Add the location object to the database session
        db.session.add(location)

        # Commit the changes to the database
        db.session.commit()

        # Retrieve the location from the database
        retrieved_location = Location.query.filter_by(name='Test Location').first()

        # Check if the retrieved location is not None
        self.assertIsNotNone(retrieved_location)

        # Check if the retrieved location's name and address match the expected values
        self.assertEqual(retrieved_location.name, 'Test Location')
        self.assertEqual(retrieved_location.address, '123 Test St')
