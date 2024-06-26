import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    @staticmethod
    def plot_count(df: pd.DataFrame, column: str):
        plt.figure(figsize=(12, 6))
        sns.countplot(data=df, x=column, order=df[column].value_counts().index)
        plt.xticks(rotation=90)
        plt.title(f'Count Plot for {column}')
        plt.xlabel(column)
        plt.ylabel('Count')
        plt.show()

    @staticmethod
    def plot_scatter(df: pd.DataFrame, x_column: str, y_column: str):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(data=df, x=x_column, y=y_column)
        plt.title(f'Scatter Plot between {x_column} and {y_column}')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()

    @staticmethod
    def plot_histogram(df: pd.DataFrame, column: str, bins=10):
        plt.figure(figsize=(12, 6))
        sns.histplot(data=df, x=column, bins=bins, kde=True)
        plt.title(f'Histogram for {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    @staticmethod
    def plot_box(df: pd.DataFrame, column: str):
        plt.figure(figsize=(12, 6))
        sns.boxplot(data=df, y=column)
        plt.title(f'Box Plot for {column}')
        plt.ylabel(column)
        plt.show()
