import pandas as pd
import numpy as np

file_path = 'data/processed/Honda_Tableau_Ready_100k.csv'
df = pd.read_csv(file_path)


categories = ['Dimension Mismatch', 'Corrosion', 'Missing Components', 'Material Defect', 'Failed Stress Test', 'Scratched in Transit', 'Improper Packaging']
cat_weights = [0.45, 0.28, 0.12, 0.07, 0.04, 0.03, 0.01]
df['Rejected_Category'] = np.random.choice(categories, size=len(df), p=cat_weights)


shifts = ['Morning (06:00-14:00)', 'Evening (14:00-22:00)', 'Night (22:00-06:00)']
shift_weights = [0.25, 0.35, 0.40]
df['Shift_Timing'] = np.random.choice(shifts, size=len(df), p=shift_weights)


severities = ['Minor (Reworkable)', 'Major (Return to Supplier)', 'Critical (Total Scrap)']
sev_weights = [0.65, 0.25, 0.10]
df['Defect_Severity'] = np.random.choice(severities, size=len(df), p=sev_weights)


base_costs = df['Total_Scrap_Cost_INR'].copy()

df['cost_modifier'] = 1.0
df.loc[df['Defect_Severity'] == 'Critical (Total Scrap)', 'cost_modifier'] *= 3.5
df.loc[df['Defect_Severity'] == 'Major (Return to Supplier)', 'cost_modifier'] *= 1.8
df.loc[df['Rejected_Category'] == 'Dimension Mismatch', 'cost_modifier'] *= 2.0
df.loc[df['Rejected_Category'] == 'Corrosion', 'cost_modifier'] *= 1.5
df.loc[df['Shift_Timing'] == 'Night (22:00-06:00)', 'cost_modifier'] *= 1.2

df['Total_Scrap_Cost_INR'] = base_costs * df['cost_modifier']
df.drop(columns=['cost_modifier'], errors='ignore', inplace=True)


df.to_csv(file_path, index=False)
print(" True, 80/20 Manufacturing Distributions Generated Successfully!")