## Live Interactive Dashboard
[Click here to view the live Honda WMS Risk Analytics Dashboard](https://public.tableau.com/views/HondaComponentRiskMatrix/ExecutiveMatrix?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

# Honda WMS Predictive Analytics (Portfolio Simulation)

This repository is a **synthetic portfolio simulation** of the ETL and Business Intelligence pipeline built during my Data Analyst Internship (IT Department) at Honda Cars India Limited. Our team built the Python pipeline; my part was the SQL reporting layer and aligning requirements with my manager.

**Note on Data & ML:** To comply with NDAs, no real enterprise data is included. The 100,000-record dataset is entirely synthetic, generated outside this repo using `Faker` with hardcoded defect weights (e.g., 3 categories were hardcoded to represent 84.5% of scrap costs to simulate a Pareto distribution). Because the data lacks genuine physical supply chain signals, the predictive ML model performs near the baseline (test accuracy 56.7% vs 56.5% baseline). The purpose of this repository is to demonstrate the architecture, not genuine machine learning outcomes.

## Project Scope
The project demonstrates three main phases:
1. **Data Engineering & EDA:** Cleaning synthetic records, handling missing values, and standardizing categories.
2. **Database Integration:** Loading the processed data into SQL Server and structuring views for reporting.
3. **Business Intelligence UI:** Designing an interactive command center in Tableau for QA Inspectors to identify defect bottlenecks.

## Tech Stack
- **Language:** Python (Pandas)
- **Database:** SQL Server (T-SQL)
- **Visualization:** Tableau
- **Version Control:** Git

## Run Order
To reproduce this pipeline locally:
1. Base dataset generated outside this repo (load the provided raw CSV).
2. Execute `sql/schema.sql` *(Creates target tables)*
3. `python src/extract.py`
4. `python src/transform.py`
5. `python src/expand_suppliers.py`
6. `python src/pareto.py`
7. `python src/feature_engineering.py`
8. `python src/train_model.py` *(Note: Architecture demonstration only)*
9. `python src/export.py` *(Loads into SQL)*
10. Execute `sql/views.sql` and `sql/procedures.sql`