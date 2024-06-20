import unittest
import pandas as pd

from data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    def test_load_data_valid_file(self):
        df = DataLoader.load_data('../data/netflix_titles.csv')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_load_data_file_not_found(self):
        df = DataLoader.load_data('non_existing_file.csv')
        self.assertIsNone(df)

    def test_load_data_invalid_format(self):
        df = DataLoader.load_data('invalid_format.txt')
        self.assertIsNone(df)

if __name__ == '__main__':
    unittest.main()
