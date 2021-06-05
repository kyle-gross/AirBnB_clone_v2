#!/usr/bin/python3
"""console testing module"""


from io import StringIO
import sys
import unittest
from unittest.mock import patch
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
from console import HBNBCommand

fs = FileStorage()


class TestConsole(unittest.TestCase):
    """A unittesting class for console"""

    def test_create(self):
        if os.path.exists(fs._FileStorage__file_path):
            os.remove(fs._FileStorage__file_path)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            state_id = f.getvalue()[:-1]
        with open(fs._FileStorage__file_path, 'r') as fd:
            self.assertIn(state_id, fd.read())
if __name__ == "__main__":
    unittest.main()
