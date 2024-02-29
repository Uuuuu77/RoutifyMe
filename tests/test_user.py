#!/usr/bin/python3

import unittest
from models.user import User, db


class UserTest(unittest.TestCase):
    def test_create_user(self):
        user = User(email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()

        retrieved_user = User.query.filter_by(email='test@example.com').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'test@example.com')
