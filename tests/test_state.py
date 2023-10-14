#!/usr/bin/python3
"""Contains unittests for state.py
Test classes:
    TestState_initiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

state = State()

class TestStateInstantiation(unittest.TestCase):
    """Unittest to test the instantiation of the class State"""

    def test_no_argument_instantiate(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_obj(self):

        self.assertIn(State(), models.storage.all().values())

    def test_id_public(self):
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        self.assertEqual(type(State().created_at), datetime)

    def test_updated_at(self):
        """test to check the created at time"""
       
        self.assertEqual(type(State().updated_at), datetime)

    def test_state_name(self):
        """Check the state name"""

        self.assertEqual(type(State.name), str)
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_state_ids(self):
        """Tests two different stateshave different ids"""

        stateA = State()
        stateB = State()
        self.assertNotEqual(stateA.id, stateB.id)

    def test_states_created_at_different_time(self):
        """Test to check the time created for two states"""

        stateA = State()
        sleep(0.15)
        stateB = State()
        self.assertLess(stateA.created_at, stateB.created_at)

    def test_state_info_updated_at_different_time(self):
        """Test to check time different states info is updated"""

        stateA = State()
        sleep(0.15)
        stateB = State()
        self.asserLess(stateA.updated_at, stateB.updated_at)

    def test_unused_arguments(self):
        """test to check that args passed aren't stored as attr"""

        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_kwargs_instantiation(self):
        """tests to check the instantiation with kwargs"""

        date = datetime.today()
        date_isoformat = date.isoformat()
        state = State(id=789, created_at=date_isoformat, updated_at=date_isoformat)
        self.assertEqual(state.id, "789")
        self.assertEqual(state.created_at, date_isoformat)
        self.assertEqual(state.updated_at, date_isoformat)

    def test_no_kwargs_instantiation(self):
        """Test for instantiation with no kwargs"""
        
        with self.assertRaises(TypeError):
            state(id=None, created_at=None, updated_at=None)

    def test_is_subclass(self):
        """test that state is subclass of basemodel"""

        self.assertIsInstance(self.state.__class__, BaseModel)

    def test_is_a_string(self):
        """test that the output is a string"""

        state.id = "789456"
        date_time = datetime.now()
        date_time_repr = repr(date_time)
        state.created_at = state.updated_at = date_time
        state_string = state.__str__()
        self.assertIn("[state] 789456", state_string)
        self.assertIn("'id': 789456", statestr)


if __name__ == "__main__":
    unittest.main()
