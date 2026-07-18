import logging
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.config import MODEL_PATH, RANDOM_STATE

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def train_risk_model(df):
    """
    Trains a Random Forest classifier to flag high-risk shipments 
    using pre-inspection features.
    """
    logging.info("Starting model training phase...")
    
    try:
        # Define features and target variable
        features = ['Supplier_Enc', 'Part_Enc', 'Unit_Cost_INR']
        X = df[features]
        y = df['Is_High_Risk']
        
       
       
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=RANDOM_STATE
        )
        logging.info(f"Data split - Training rows: {len(X_train)}, Testing rows: {len(X_test)}")
        
       
        model = RandomForestClassifier(
            max_depth=10, 
            min_samples_leaf=30, 
            random_state=RANDOM_STATE
        )
        model.fit(X_train, y_train)
        logging.info("Model training complete.")
       

        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        logging.info(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")
        
      
        joblib.dump(model, MODEL_PATH)
        logging.info(f"Model successfully saved to: {MODEL_PATH}")
        
        return model
        
    except Exception as e:
        logging.error(f"Error during model training: {e}")
        raise

if __name__ == "__main__":
    from src.extract import load_raw_data
    from src.transform import clean_data
    from src.feature_engineering import engineer_features
    
    raw_df = load_raw_data()
    clean_df = clean_data(raw_df)
    fe_df = engineer_features(clean_df)
    
    trained_model = train_risk_model(fe_df)