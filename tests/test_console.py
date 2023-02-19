#!/usr/bin/python3
""" Module for testing console"""
import unittest
import console
import os
import io
from contextlib import redirect_stdout
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


HBNBComm = console.HBNBCommand()
classes = {"BaseModel": BaseModel, "State": State, "User": User,
           "Place": Place, "City": City, "Amenity": Amenity,
           "Review": Review}


class test_console(unittest.TestCase):
    """ Class to test the console method"""

    def test_console(self):
        """ test that console module exists"""
        self.assertTrue(os.path.isfile('console.py'))

    def test_create_wto_params(self):
        """test that console creates without params"""
        with redirect_stdout(io.StringIO()) as f:
            HBNBComm.do_create("State")
        id = f.getvalue()
        id = id.replace('\n', "")
        c_name = "State"
        key = c_name + "." + id
        created_state = storage.all()[key]
        self.assertEqual(id, created_state.id)
