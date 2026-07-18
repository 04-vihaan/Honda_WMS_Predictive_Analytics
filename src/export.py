import os
import pandas as pd
import pymssql
import logging
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fetch credentials securely
SERVER = os.getenv('DB_SERVER', 'localhost')
USER = os.getenv('DB_USER', 'sa')
PASSWORD = os.getenv('DB_PASSWORD')
DATABASE = os.getenv('DB_NAME', 'Honda_WMS_Analytics')

def ingest_to_sql():
    if not PASSWORD:
        logging.error("Database password not found in environment variables.")
        raise ValueError("Missing DB_PASSWORD environment variable.")

    csv_path = 'data/processed/Honda_Tableau_Ready_100k.csv'
    logging.info(f"Reading data from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    # Handle null values for SQL insertion
    df = df.where(pd.notnull(df), None)

    logging.info(f"Connecting to MSSQL database: {DATABASE}...")
    
    try:
        conn = pymssql.connect(
            server=SERVER, 
            user=USER, 
            password=PASSWORD, 
            database=DATABASE
        )
        cursor = conn.cursor()

        logging.info("Truncating existing WMS_Processed_Data table...")
        cursor.execute("TRUNCATE TABLE WMS_Processed_Data;")
        
        insert_query = """
        INSERT INTO WMS_Processed_Data (
            PRIS_No, Supplier_Name, Part_Code, Part_Description, Rejection_Date, 
            Total_Scrap_Cost_INR, Rejection_Rate_Pct, Supplier_Enc, Part_Enc, 
            Is_High_Risk, ML_Risk_Prediction, Risk_Label
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        records = df[[
            'PRIS_No', 'Supplier_Name', 'Part_Code', 'Part_Description', 'Rejection_Date',
            'Total_Scrap_Cost_INR', 'Rejection_Rate_Pct', 'Supplier_Enc', 'Part_Enc',
            'Is_High_Risk', 'ML_Risk_Prediction', 'Risk_Label'
        ]].values.tolist()

        logging.info(f"Executing batch insert of {len(records)} records...")
        cursor.executemany(insert_query, records)
        
        conn.commit()
        logging.info("Data ingestion completed successfully.")
        
    except Exception as e:
        logging.error(f"Database operation failed: {e}")
        if 'conn' in locals():
            conn.rollback()
        raise
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    ingest_to_sql()