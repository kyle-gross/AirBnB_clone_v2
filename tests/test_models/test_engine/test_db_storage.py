#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel
from models import storage
from os import environ
import MySQLdb
from models.state import State
from models.city import City
args = {
    'user': environ.get('HBNB_MYSQL_USER'),
    'passwd': environ.get('HBNB_MYSQL_PWD'),
    'db': environ.get('HBNB_MYSQL_DB'),
    'host': environ.get('HBNB_MYSQL_HOST')
}


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db', "Db only")
class test_db_Storage(unittest.TestCase):
    """Test class for dbstorage"""

    def setUp(self):
        """ Set up test environment """
        self.db_connection = MySQLdb.connect(**args)
        self.cursor = self.db_connection.cursor()

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            self.cursor.close()
            self.db_connection.close()
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to db """
        new = State(name="Oklahoma")
        new.save()
        self.assertIn(new, storage.all().values())
        new.delete()

    def test_all(self):
        """ __objects is properly returned """
        self.assertIsInstance(storage.all(), dict)

    def test_city_db(self):
        """ Tests creation of city """
        state = State(name="California")
        id = state.id
        city = City(name="Fremont", state_id=id)
        city2 = City(name="San_Francisco", state_id=id)
        self.assertIn(city, storage.all().values())
        self.assertIn(city, storage.all().values())
