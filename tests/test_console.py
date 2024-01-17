#!/usr/bin/python3
"""unit testing module for the console.
"""
import json
import MySQLdb
import os
import sqlalchemy
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from tests import clear_stream


class TestHBNBCommand(unittest.TestCase):
    """Representing test class for HBNBCommand class
    """
    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_Create(self):
        """Testing the create cmd with file storage
        """
        with patch('sys.stdout', new=StringIO()) as cout:
            conss = HBNBCommand()
            conss.onecmd('create City name="Texas"')
            mdlId = cout.getvalue().strip()
            clear_stream(cout)
            self.assertIn('City.{}'.format(mdlId), storage.all().keys())
            conss.onecmd('show City {}'.format(mdlId))
            self.assertIn("'name': 'Texas'", cout.getvalue().strip())
            clear_stream(cout)
            conss.onecmd('create User name="James" age=17 height=5.9')
            mdlId = cout.getvalue().strip()
            self.assertIn('User.{}'.format(mdlId), storage.all().keys())
            clear_stream(cout)
            conss.onecmd('show User {}'.format(mdlId))
            self.assertIn("'name': 'James'", cout.getvalue().strip())
            self.assertIn("'age': 17", cout.getvalue().strip())
            self.assertIn("'height': 5.9", cout.getvalue().strip())