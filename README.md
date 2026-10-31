## Live Interactive Dashboard
[Click here to view the live Honda WMS Risk Analytics Dashboard](https://public.tableau.com/views/HondaComponentRiskMatrix/ExecutiveMatrix?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

# Honda WMS Predictive Analytics (Portfolio Simulation)

This repository is a **synthetic portfolio simulation** of the ETL and Business Intelligence pipeline I developed during my IT Internship at Honda Cars India Limited. 

**Note on Data & ML:** To comply with NDAs, no real enterprise data from Honda's WMS or PRIS databases is included. The 100,000-record dataset is entirely synthetic, generated using `Faker` and `Pandas` with hardcoded defect weights (e.g., 3 categories were hardcoded to represent ~84% of scrap costs to simulate a Pareto distribution). 

Because the data lacks genuine physical supply chain signals, the predictive ML model included in this pipeline performs near the baseline majority-class guess (~57% accuracy). The purpose of this repository is to demonstrate the data engineering architecture and Tableau visualization skills, not genuine machine learning outcomes.

## Project Scope
The project demonstrates three main phases:
1. **Data Engineering & EDA:** Generating, extracting, and cleaning synthetic records, handling missing values, and standardizing categories.
2. **Database Integration:** Loading the processed data into SQL Server and structuring views for reporting.
3. **Business Intelligence UI:** Designing an interactive command center in Tableau for QA Inspectors to identify defect bottlenecks.

## Tech Stack
- **Language:** Python (Pandas, Faker)
- **Database:** SQL Server
- **Visualization:** Tableau
- **Version Control:** Git

## Run Order
To reproduce this pipeline locally:
1. Run the data generator (or load the provided sample CSV).
2. `python src/extract.py`
3. `python src/transform.py`
4. `python src/feature_engineering.py`
5. `python src/train_model.py` *(Note: Included to demonstrate pipeline architecture only; predictions are simulated)*