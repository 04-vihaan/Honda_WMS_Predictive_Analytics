## Live Interactive Dashboard
[Click here to view the live Honda WMS Risk Analytics Dashboard](https://public.tableau.com/app/profile/vihaan.singh/viz/HondaWMSPredictiveDiagnostics/Dashboard3?publish=yes)

# Honda Disha: Predictive Supplier Quality & PRIS Diagnostics

**An End-to-End Machine Learning & Analytics Pipeline for Proactive Supply Chain Management**

## The Business Problem
At scale, modern automotive manufacturing relies on just-in-time logistics. When defective parts bypass initial checks and reach the assembly line, it results in production downtime, critical safety risks, and massive scrap losses. 

Historically, Part Rejection Information Systems (PRIS) and Warehouse Management Systems (WMS) operate as reactive reporting tools. Managers often only see the financial impact of defects after the incident has occurred. 

**The Objective:** Transform this reactive reporting structure into a predictive diagnostic engine. The goal of this portfolio project was to build a machine learning pipeline that analyzes historical data, supplier trends, and logistics behavior to flag high-risk shipments before they are accepted into inventory.

## Project Scope & Simulated Environment
To demonstrate real-world Data Engineering and Machine Learning skills without violating corporate data privacy, this project is built entirely on a simulated enterprise environment. 

I generated 100,000 synthetic supply chain records using Python and the Faker library. To make the data realistic, I distributed the data across 450 fictional suppliers following an 80/20 Pareto distribution (where a few massive suppliers handle most of the volume, and hundreds of small suppliers handle the rest).

The project is broken down into three main phases:
1. **Data Engineering & EDA:** Extracting and cleaning the synthetic records, standardizing categorical variables, and mapping defect severity.
2. **Predictive Modeling:** Training a classification model using pre-inspection features to assign a dynamic "Risk Label" to incoming shipments.
3. **Business Intelligence UI:** Designing an interactive command center in Tableau for QA Inspectors to easily digest the ML outputs and take immediate action.

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (RandomForestClassifier)
* **Visualization/BI:** Tableau (Dashboarding, Parameter Actions)
* **Version Control:** Git & GitHub

## Approach & Methodology

### 1. Exploratory Data Analysis (EDA) & Cleaning
Real-world WMS data is messy, so I designed the synthetic dataset to require heavy cleaning. I spent time standardizing nomenclature, handling missing values, and structuring the data so it was ready for SQL ingestion and analysis. 

### 2. Feature Engineering & Avoiding Data Leakage
A major learning curve in this project was understanding data leakage. Early in development, my model was accidentally using post-inspection data (like rejection rates) to predict pre-inspection risk. I corrected this by re-engineering the pipeline to strictly use pre-inspection features (like encoded supplier IDs, part codes, and unit costs) so the model makes fair, real-world predictions.

### 3. Model Training
I trained a Random Forest Classifier to identify high-risk shipments. Initially, the model heavily overfit the training data, resulting in an artificially high accuracy and a massive file size. By placing strict limits on the maximum tree depth and minimum leaf size, I optimized the model down to a lightweight size with a realistic accuracy of ~60%. This proves the model is finding genuine, subtle patterns in the data without memorizing the answers.

### 4. The BI Dashboard (Honda Disha)
The final deliverable is a Tableau dashboard acting as the user interface for the ML model's output. 
* **KPI Banners:** High-level metrics for quick executive visibility.
* **Pareto Diagnostics:** Identifying the defect categories driving the most scrap cost.
* **Interactive Filtering:** Allowing managers to filter the entire dashboard by interacting with supplier risk nodes.
* **Action Watchlist:** The direct output of the ML model, giving inspectors a prioritized checklist of shipments to investigate today.