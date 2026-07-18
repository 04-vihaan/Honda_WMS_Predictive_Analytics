import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DATA_DIR = BASE_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "Honda_Mega_PRIS_Dataset_100k.csv"
PROCESSED_DATA_PATH = DATA_DIR / "processed" / "honda_wms_engineered.csv"
TABLEAU_EXPORT_PATH = DATA_DIR / "processed" / "Honda_Tableau_Ready_100k.csv"


MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "supplier_risk_model.joblib"
REPORTS_DIR = BASE_DIR / "reports"

RANDOM_STATE = 42

print(" Configuration loaded successfully.")