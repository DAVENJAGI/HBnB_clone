import unittest
import models
import json
import re
from models import storage
from models.user import User
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class testUser(unittest.TestCase):

    """Test class for user class"""
    def setUp(self):
        """sets up test methods"""
        
        pass

    def tearDown(self):
        """Tears down a method"""

        self.resetStorage()
        
        pass

    def resetStorage(self):
        """resets filestorage data to an empty dict"""
        
        FileStorage.__filestorage__objects = {}
        if os.path.isfile(FileStorage.__FileStorage__file_path):
            os.remove(FileStorage.__filestorage__file__path)

    def test_init(self):
        """Test to see whether the set user details are the correct"""

        user = User(email="njagidave@gmail.com", password="passwrd", first_name="Dave", last_name="Njagi")

        self.assertEqual(user.email, "njagidave@gmail.com")
        self.assertEqual(user.password, "passwrd")
        self.assertEqual(user.first_name, "Dave")
        self.assertEqual(user.last_name, "Njagi")

    def test_set_email(self):
        """test to see if the set email is the correct output email"""
        user = User()
        user.set_email("njagidave@gmail.com")
        self.assertEqual(email, "njagidave@gmail.com")

    def test_getmail(self):
        """test to check whether the retrieved mail is the correct one"""
        user = User()
        retrieved_mail = user.get_email()
        self.assertEqual(email, retrieved_mail)

    def test_set_password(self):
        """test to check for the set password"""

        user = User()
        user.set_password("passwrd")
        self.assertEqual(user.password, "passwrd")

    def test_getpassword(sef):
        """Test to check if the retrieved password is true"""

        user = User()
        retrieved_password = user.get_password()
        self.assertEqual(password, retrieved_password)

    def test_set_firstname(self):
        """Test to check whether set first name is true"""

        user = User()
        user.set_first_name("Dave")
        self.assertEqual(user.first_name, "Dave")

    def test_get_first_name(self):
        """test to check whether retrieved first name True"""

        user = User()
        first_name = user.get_first_name()
        self.assertEqual(first_name, "Dave")

    def test_set_last_name(self):
        """Test to check whether set last name True"""

        user = User()
        user.set_last_name("Njagi")
        self.assertEqual(user.last_name, "Njagi")

    def test_get_last_name(self):
        """Test to check whether retrieved last name True"""

        user = User()
        last_name = user.get_last_name()
        self.assertEqual(last_name, "Njagi")

    @mock.patch("models.user.BaseModel.save", return_value=True)
    def test_save(self, mock_save):
        """Test to check whether the info is saved"""
        user = User(email="davenjagi@gmail.com", password="passwrd", first_name="Dave", last_name="Njagi")
        user.save()

        mock_save.assert_called_once()

if __name__ == "__main__":
    unittest.main()
