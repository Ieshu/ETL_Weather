import unittest
from src.transform import transform_data

class TestTransformData(unittest.TestCase):

    def test_transform_data(self):
        raw_data = {
            'main': {'temp': 290, 'humidity': 80},
            'weather': [{'description': 'clear sky'}],
            'name': 'London',
            'dt': 1627669200
        }
        transformed_data = transform_data(raw_data)
        self.assertIn('temperature', transformed_data)
        self.assertIn('humidity', transformed_data)
        self.assertIn('weather', transformed_data)
        self.assertEqual(transformed_data['city'], 'London')
