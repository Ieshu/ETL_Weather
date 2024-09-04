import unittest
from unittest.mock import patch
from src.extract import extract_data

class TestExtractData(unittest.TestCase):

    @patch('src.extract.requests.get')
    def test_extract_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'main': {'temp': 290, 'humidity': 80}}
        data = extract_data()
        self.assertIsNotNone(data)
        self.assertIn('main', data)

    @patch('src.extract.requests.get')
    def test_extract_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        data = extract_data()
        self.assertIsNone(data)
