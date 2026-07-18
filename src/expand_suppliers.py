
import pandas as pd
import numpy as np
from faker import Faker


fake = Faker()
Faker.seed(42)
np.random.seed(42)

def expand_suppliers():
    file_path = 'data/raw/Honda_Mega_PRIS_Dataset_100k.csv'
    print(f"Loading {file_path}...")
    df = pd.read_csv(file_path)

    print("Generating 450 unique manufacturing supplier names using Faker...")
    
    suffixes = ['Auto', 'Dynamics', 'Engineering', 'Manufacturing', 'Systems', 'Components', 'Tech', 'Industries', 'Parts', 'Global']
    
    unique_suppliers = set()
    while len(unique_suppliers) < 450:
        base_name = fake.company().split(',')[0].split(' ')[0]
        suffix = np.random.choice(suffixes)
        unique_suppliers.add(f"{base_name} {suffix}")
    
    suppliers_list = list(unique_suppliers)

   

    print("Applying Pareto distribution to 100,000 rows...")
    weights = np.random.pareto(a=2, size=450)
    weights /= weights.sum() 

    df['Supplier_Name'] = np.random.choice(suppliers_list, size=len(df), p=weights)

   
    df.to_csv(file_path, index=False)
    print(f"✅ Success! Dataset now contains exactly {df['Supplier_Name'].nunique()} unique suppliers.")

if __name__ == "__main__":
    expand_suppliers()