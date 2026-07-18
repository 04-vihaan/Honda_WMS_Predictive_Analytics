import pandas as pd
import joblib
import logging
from src.config import MODEL_PATH, TABLEAU_EXPORT_PATH

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def generate_predictions(df):
    """
    Loads the trained model, generates risk predictions, 
    and exports the final dataset for Tableau.
    """
    logging.info("Starting prediction phase...")
    
    try:
        # 1. Load the trained model from disk
        logging.info(f"Loading model from {MODEL_PATH}...")
        model = joblib.load(MODEL_PATH)
        
        # 2. Define the exact features the model was trained on
        features = ['Supplier_Enc', 'Part_Enc', 'Unit_Cost_INR']
        X = df[features]
        
        # 3. Generate predictions
        df['ML_Risk_Prediction'] = model.predict(X)
        
        # 4. Map the numeric prediction (0 or 1) back to a readable text label for Tableau
        df['Risk_Label'] = df['ML_Risk_Prediction'].apply(
            lambda x: 'High Risk' if x == 1 else 'Low Risk'
        )
        logging.info("Predictions generated and labels applied.")
        
        # 5. Export the final dataset
        df.to_csv(TABLEAU_EXPORT_PATH, index=False)
        logging.info(f"Final dataset successfully saved for Tableau at: {TABLEAU_EXPORT_PATH}")
        
        return df
        
    except Exception as e:
        logging.error(f"CRITICAL ERROR during prediction: {e}")
        raise

if __name__ == "__main__":
    from src.extract import load_raw_data
    from src.transform import clean_data
    from src.feature_engineering import engineer_features
    
   
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)
    fe_df = engineer_features(clean_df)
    

    final_df = generate_predictions(fe_df)
    
    print("\nFinal Output Preview (Ready for Tableau):")
    print(final_df[['Supplier_Name', 'Part_Description', 'Risk_Label']].head())