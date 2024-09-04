import unittest
import os
import json
from src.load import load_data
from src.utils import read_config

class TestLoadData(unittest.TestCase):

    def setUp(self):
        self.config = read_config()

    def test_load_data(self):
        data = {'temperature': 290, 'humidity': 80}
        load_data(data, stage="final")
        with open(self.config['file_paths']['final_data'], 'r') as f:
            loaded_data = json.load(f)
        self.assertEqual(data, loaded_data)

    def tearDown(self):
        os.remove(self.config['file_paths']['final_data'])
