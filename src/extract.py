import pandas as pd
import logging
from src.config import RAW_DATA_PATH


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_raw_data(file_path=RAW_DATA_PATH):
    """
    Extracts the raw WMS dataset from the specified file path.
    Includes error handling to catch missing files or corruption.
    """
    try:
        logging.info(f"Attempting to load raw data from: {file_path}")
        
       
        df = pd.read_csv(file_path)
        
        logging.info(f" Successfully loaded raw data. Dataset Shape: {df.shape}")
        return df
        
    except FileNotFoundError:
        logging.error(f" CRITICAL: File not found at {file_path}. Is the file in data/raw?")
        raise 
        
    except Exception as e:
        logging.error(f" CRITICAL: An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    test_df = load_raw_data()
    print("\nFirst 3 rows preview:")
    print(test_df.head(3))