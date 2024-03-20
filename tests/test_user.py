#!/usr/bin/python3

import unittest
from models.user import User, db


# Unit test class for testing User model
class UserTest(unittest.TestCase):
    # Test case for creating a user
    def test_create_user(self):
        # Create a new user object
        user = User(email='test@example.com', password='password')

        # Add the user object to the database session
        db.session.add(user)

        # Commit the changes to the database
        db.session.commit()

        # Retrieve the user from the database
        retrieved_user = User.query.filter_by(email='test@example.com').first()

        # Check if the retrieved user is not None
        self.assertIsNotNone(retrieved_user)

        # Check if the retrieved user's email matches the expected value
        self.assertEqual(retrieved_user.email, 'test@example.com')
