import pandas as pd

class DataProcessor:
    @staticmethod
    def filter_data(df: pd.DataFrame, column: str, value) -> pd.DataFrame:
        return df[df[column] == value]

    @staticmethod
    def sort_data(df: pd.DataFrame, column: str, ascending=True) -> pd.DataFrame:
        return df.sort_values(by=column, ascending=ascending)

    @staticmethod
    def convert_categorical_to_numeric(df: pd.DataFrame, column: str) -> pd.DataFrame:
        df[column] = pd.Categorical(df[column]).codes
        return df
