import pandas as pd

def get_corruption_data():
    try:
        df = pd.read_csv('corruption_data.csv')
        print("Corruption data loaded successfully from corruption_data.csv")
        return df
    except FileNotFoundError:
        print("Error: corruption_data.csv not found. Please ensure the file is in the same directory.")
        return None

if __name__ == "__main__":
    data = get_corruption_data()
    if data is not None:
        print(data.head())