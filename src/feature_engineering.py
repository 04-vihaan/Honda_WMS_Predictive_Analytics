import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder


logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def engineer_features(df):
    """
    Creates machine learning features: encodes categorical variables 
    and defines the target variable for the model.
    """
    logging.info("Starting feature engineering...")
    
    try:
        df_fe = df.copy()
        
       
        if 'Rejection_Rate_Pct' in df_fe.columns:
            df_fe['Is_High_Risk'] = (df_fe['Rejection_Rate_Pct'] > 5).astype(int)
            logging.info("Created target variable: 'Is_High_Risk'")
        

        le = LabelEncoder()
        
        if 'Supplier_Name' in df_fe.columns:
            df_fe['Supplier_Enc'] = le.fit_transform(df_fe['Supplier_Name'])
            logging.info("Encoded 'Supplier_Name'.")
            
        if 'Part_Description' in df_fe.columns:
            df_fe['Part_Enc'] = le.fit_transform(df_fe['Part_Description'])
            logging.info("Encoded 'Part_Description'.")
            
        logging.info(f" Feature engineering complete. Shape: {df_fe.shape}")
        return df_fe
        
    except Exception as e:
        logging.error(f" CRITICAL ERROR during feature engineering: {e}")
        raise


if __name__ == "__main__":
    from src.extract import load_raw_data
    from src.transform import clean_data
    
   
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)
    fe_df = engineer_features(clean_df)
    
    print("\n Engineered Features Preview:")
    print(fe_df[['Supplier_Name', 'Supplier_Enc', 'Part_Description', 'Part_Enc', 'Is_High_Risk']].head())