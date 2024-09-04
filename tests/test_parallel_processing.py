import unittest
from src.parallel_processing import parallel_process_data

class TestParallelProcessing(unittest.TestCase):

    def test_parallel_process_data(self):
        data_chunks = [{'key1': 'value1'}, {'key2': 'value2'}]
        processed_chunks = parallel_process_data(data_chunks)
        self.assertEqual(len(processed_chunks), 2)
        self.assertEqual(processed_chunks[0]['key1'], 'value1')
