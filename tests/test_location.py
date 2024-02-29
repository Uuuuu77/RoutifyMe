#!/usr/bin/python3

import unittest
from models.location import Location, db

class LocationTest(unittest.TestCase):
    def test_create_location(self):
        location = Location(name='Test Location', address='123 Test St')
        db.session.add(location)
        db.session.commit()

        retrieved_location = Location.query.filter_by(name='Test Location').first()
        self.assertIsNotNone(retrieved_location)
        self.assertEqual(retrieved_location.name, 'Test Location')
        self.assertEqual(retrieved_location.address, '123 Test St')
