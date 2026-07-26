import pandas as pd
import numpy as np

def apply_pareto_skew(input_file, output_file):
    print("Firing up the data engine... loading dataset.")
    df = pd.read_csv(input_file)

    np.random.seed(42)

    categories = [
        'Dimension Mismatch', 
        'Corrosion', 
        'Missing Components', 
        'Failed Stress Test', 
        'Material Defect', 
        'Scratched in Transit', 
        'Improper Packaging'
    ]
    category_weights = [0.45, 0.28, 0.12, 0.07, 0.04, 0.03, 0.01]
    
    df['Rejected_Category'] = np.random.choice(categories, size=len(df), p=category_weights)

    shifts = ['Morning (06:00-14:00)', 'Evening (14:00-22:00)', 'Night (22:00-06:00)']
    shift_weights = [0.25, 0.35, 0.40]
    df['Shift_Timing'] = np.random.choice(shifts, size=len(df), p=shift_weights)

    severities = ['Minor (Reworkable)', 'Major (Return to Supplier)', 'Critical (Total Scrap)']
    severity_weights = [0.65, 0.25, 0.10]
    df['Defect_Severity'] = np.random.choice(severities, size=len(df), p=severity_weights)

    cost_modifier = {
        'Dimension Mismatch': 1.0,
        'Corrosion': 1.2,
        'Missing Components': 1.0,
        'Failed Stress Test': 1.3,
        'Material Defect': 1.1,
        'Scratched in Transit': 0.9,
        'Improper Packaging': 0.5
    }

    df['Total_Scrap_Cost_INR'] = (df['Scrap_Qty'] * df['Unit_Cost_INR'] * df['Rejected_Category'].map(cost_modifier))

    print("-" * 40)
    print("SANITY CHECKS")
    print("-" * 40)
    
    total_cost = df['Total_Scrap_Cost_INR'].sum()
    print(f"Total Scrap Cost: INR {total_cost:,.2f}")
    
    print("\nCategory Distribution Skew:")
    print(df['Rejected_Category'].value_counts(normalize=True).round(3))

    print("\nShift Timing Distribution Skew:")
    print(df['Shift_Timing'].value_counts(normalize=True).round(3))

    print("\nDefect Severity Distribution Skew:")
    print(df['Defect_Severity'].value_counts(normalize=True).round(3))
    
    print("\nCritical Columns Untouched:")
    print(f"Unique Suppliers: {df['Supplier_Name'].nunique()}")
    print("High Risk Flags (Is_High_Risk):")
    print(df['Is_High_Risk'].value_counts(normalize=True).round(3))

    df.to_csv(output_file, index=False)
    print("\nPipeline finished! Data successfully tuned and exported.")

if __name__ == "__main__":
    file_path = 'data/processed/Honda_Tableau_Ready_100k.csv'
    apply_pareto_skew(file_path, file_path)