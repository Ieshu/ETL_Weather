import unittest
from src.validation import validate_data

class TestValidateData(unittest.TestCase):

    def test_validate_data_success(self):
        data = {'temperature': 290, 'humidity': 80}
        self.assertTrue(validate_data(data))

    def test_validate_data_failure(self):
        data = {'humidity': 80}
        self.assertFalse(validate_data(data))
