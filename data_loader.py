import pandas as pd

class DataLoader:
    @staticmethod
    def load_data(file_path: str) -> pd.DataFrame:
        try:
            data = pd.read_csv(file_path)
            return data
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
        except pd.errors.ParserError:
            print(f"Error parsing the file {file_path}.")
            return None
