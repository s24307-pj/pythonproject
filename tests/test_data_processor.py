import unittest
import pandas as pd
from data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': ['a', 'b', 'a', 'b'],
            'C': [10, 20, 30, 40]
        })

    def test_filter_data(self):
        filtered_df = DataProcessor.filter_data(self.data, 'B', 'a')
        self.assertEqual(len(filtered_df), 2)
        self.assertTrue((filtered_df['B'] == 'a').all())

    def test_sort_data_ascending(self):
        sorted_df = DataProcessor.sort_data(self.data, 'C', ascending=True)
        self.assertTrue(sorted_df['C'].is_monotonic_increasing)

    def test_sort_data_descending(self):
        sorted_df = DataProcessor.sort_data(self.data, 'C', ascending=False)
        self.assertTrue(sorted_df['C'].is_monotonic_decreasing)

    def test_convert_categorical_to_numeric(self):
        converted_df = DataProcessor.convert_categorical_to_numeric(self.data, 'B')
        self.assertTrue(pd.api.types.is_integer_dtype(converted_df['B']))

if __name__ == '__main__':
    unittest.main()
