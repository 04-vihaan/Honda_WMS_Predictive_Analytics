import pandas as pd

# 1. Load the raw dataset
file_path = 'data/raw/Honda_Mega_PRIS_Dataset_100k.csv'
print(f"Loading {file_path}...")
df = pd.read_csv(file_path)

# 2. Map the real companies to professional, fictional names
supplier_map = {
    'Bosch India': 'Alpha Auto Systems',
    'Denso India': 'Beta Dynamics',
    'Motherson Sumi': 'Gamma Parts Ltd',
    'Gabriel India': 'Delta Engineering',
    'Varroc Engineering': 'Epsilon Tech',
    'Minda Industries': 'Zeta Manufacturing',
    'Lumax Auto': 'Theta Components',
    'Endurance Tech': 'Omega Industries'
}

# 3. Replace the names in the column
df['Supplier_Name'] = df['Supplier_Name'].replace(supplier_map)

# 4. Overwrite the raw file with the clean data
df.to_csv(file_path, index=False)
print(" Success! All real supplier names have been scrubbed and anonymized.")