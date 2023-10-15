#!/usr/bin/python3

"""testunit or file file_storage.py
    test classes:
            construct instantiation withour args
            destructor
"""

import models
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.amenity import Amenity

class TestCaseFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_storage = FileStorage()

    def teardown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Testcase to ensure it returns the dictionary of objects"""
        
        amenity = Amenity()

        self.file_storage.new(Amenity(name="amenityA"))
        self.file_storage.new(Amenity(name="amenityB"))

        objects = self.file_storage.all()

        self.assertEqual(2, len(obects))
        self.assertIn("amenityB", objects)
        self.assertIn("amenityA", objects)

    def test_new(self):
        """Test that the newset object in the dict with correct key"""

        amenity = Amenity(name="WIFI")
        self.file_storage.new(amenity)

        objects = self.file_storage.all()

        self.assertEqual(1, len(objects))
        self.assertIn("WIFI", objects)
        self.assertEqual(amenity, objets["WIFI"])

    def test_save(self):
        """testcase that save serializes the dict"""
        
        amenity  = Amenity(name="amenity 5")
        self.file_storage.new(amenity)

        self.filestorage.save()

        with open("file.json", "r") as f:
            json_obj = load(f)

        self.assertEqual(1, len(json_obj))
        self.assertIn("amenity.1", json_obj)
        self.assertEqual(amenity.to_dict(), json_obj["amenity.1"])

    def test_reload(self):
        """test that reload deserializes file to dict"""
        
        amenity = Amenity(name="Wifi")
        self.file_storage.new(amenity)

        self.file_storage.save()

        self.file_storage.reload()

        obj = self.file_storage.all()

        self.assertEqual(1, len(obj))
        self.assertIn("Wifi", obj)
        self.assertEqual(amenity, obj["Wifi"])

if __name__ == "__main__":
    unittest.main()
