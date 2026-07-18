import logging
import pandas as pd


from src.extract import load_raw_data
from src.transform import clean_data
from src.feature_engineering import engineer_features
from src.predict import generate_predictions


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_the_whole_thing():
    """
    this function triggers the full ETL + ML prediction pipeline.
    TODO: add argparser later if manager asks for it.
    """
    logging.info("!!! starting the master pipeline !!!")
    
    try:
      
        logging.info("step 1: loading raw data...")
        raw_data = load_raw_data()
        
       
        logging.info("step 2: running data transformation...")
        cleaned_data = clean_data(raw_data)
        
       
        logging.info("step 3: generating features...")
        fe_data = engineer_features(cleaned_data)
        
       
        logging.info("step 4: running model prediction and scoring...")
        final_output = generate_predictions(fe_data)
        
        logging.info("pipelline finished successfully!! file exported for tableau dashboard.")
        
    except Exception as err:
        logging.error(f"pipeline crashed hard somewhere: {err}")
        raise

if __name__ == "__main__":
   
    run_the_whole_thing()