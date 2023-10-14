#!/usr/bin/python3
"""unittests for city.py
    TesClasses:
        test_constructor correct initializing
        test_constructor with arguments
        test _destructor
"""

import models
import unittest
import os
import datetime from datetime
import time from sleep
from models.base_model import BaseModel
from models.city import City

class TestCaseCity(unittest.TestCase):

    def test_constructor(self):
        """Test case that constructor correctly initializes"""

        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_constructor_with_arguments(self):
        """unit Testcases to check if city is initialized correctly with state_id and name"""

        city = City(state_id="+254", name="Mombasa")

        self.assertEqual(city.state_id, "*254")
        self.assertEqual(city.name, "Mombasa")

    def test_destructor_for_the_class(self):
        """unit TestCase to check if it's destroyed appropriately"""

        city = City()

        del city

        """check and make sure that the object is not present anymore in the class"""

        with self.assertRaises(NameError):
            city.state_id

        with self.assertRaises(NameError):
            city.name

if __name__ = "__main__":
    unittest.main()
