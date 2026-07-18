import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean_data(df):
    """
    Cleans the raw WMS data: handles missing values, fixes data types, 
    and prepares it for feature engineering.
    """
    logging.info("Starting data transformation and cleaning...")
    
    try:

        df_clean = df.copy()
        

        if 'Rejection_Date' in df_clean.columns:
            df_clean['Rejection_Date'] = pd.to_datetime(df_clean['Rejection_Date'], errors='coerce')
            logging.info("Converted 'Rejection_Date' to Datetime objects.")
            


        text_cols = df_clean.select_dtypes(include=['object']).columns
        num_cols = df_clean.select_dtypes(include=['number']).columns
        
        df_clean[text_cols] = df_clean[text_cols].fillna('Unknown')
        df_clean[num_cols] = df_clean[num_cols].fillna(0)
        

        for col in text_cols:
            df_clean[col] = df_clean[col].astype(str).str.strip()

        logging.info(f" Data cleaning complete. Final shape: {df_clean.shape}")
        return df_clean
        
    except Exception as e:
        logging.error(f"CRITICAL ERROR during transformation: {e}")
        raise


if __name__ == "__main__":
    from src.extract import load_raw_data
    

    raw_df = load_raw_data()
    

    cleaned_df = clean_data(raw_df)
    
    print("\nCheck out the clean Data Types:")
    print(cleaned_df.dtypes.head())