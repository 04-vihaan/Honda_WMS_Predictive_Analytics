##  Live Interactive Dashboard
[Click here to view the live Honda WMS Risk Analytics Dashboard](https://public.tableau.com/app/profile/vihaan.singh/viz/HondaWMSPredictiveDiagnostics/Dashboard3?publish=yes)


#  Honda Disha: Predictive Supplier Quality & PRIS Diagnostics

**An End-to-End Machine Learning & Analytics Pipeline for Proactive Supply Chain Management**

##  The Business Problem
At scale, modern automotive manufacturing relies on just-in-time logistics. When defective parts bypass initial checks and reach the assembly line, it results in production downtime, critical safety risks, and massive scrap losses. 

Historically, Honda's Part Rejection Information System (PRIS) and Warehouse Management System (WMS) operated as *reactive* reporting tools. Managers would only see the financial impact of defects (scrap cost) *after* the incident occurred. 

**The Objective:** Transform this reactive reporting structure into a **predictive diagnostic engine**. The goal of this project was to build a machine learning model that analyzes historical PRIS data, supplier telemetry, and logistics behavior to flag high-risk shipments *before* they are accepted into inventory.

##  Internship Project Scope
This repository contains the work completed during my two-month data analytics internship. The project was broken down into three main phases:
1. **Data Engineering & EDA:** Extracting and cleaning ~100,000 historical supply chain records, standardizing categorical variables, and mapping defect severity.
2. **Predictive Modeling:** Engineering features (e.g., historical supplier reliability, transit anomalies) and training a classification model to assign a dynamic "Risk Label" to incoming shipments.
3. **Business Intelligence UI:** Designing an interactive command center in Tableau for QA Inspectors and Supply Chain Managers to easily digest the ML outputs and take immediate action.

##  Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (RandomForestClassifier, SMOTE)
* **Visualization/BI:** Tableau (Dashboarding, Parameter Actions), Matplotlib/Seaborn (EDA)
* **Version Control:** GitHub

##  Approach & Methodology

### 1. Exploratory Data Analysis (EDA) & Cleaning
Real-world WMS data is messy. A significant portion of the initial timeline was spent standardizing nomenclature across different supplier regions and handling missing transit times. I conducted deep EDA to uncover correlations between specific shifts, transit delays, and defect spikes (e.g., noticing higher defect rates during overnight transit windows).

### 2. Feature Engineering
Raw data isn't enough for an accurate model. I created several derived features to give the model better context:
* `Historical_Defect_Rate`: A rolling average of a supplier's past performance.
* `Transit_Anomaly_Flag`: A binary indicator if a shipment took 20% longer than the route's benchmark average.
* `Severity_Index`: A weighted score combining scrap quantity and defect type.

### 3. Model Training & Class Imbalance
**The Challenge:** Fortunately, the vast majority of shipped parts are perfectly fine. Unfortunately, this creates a massive class imbalance in the dataset. If a model simply guesses "Low Risk" every time, it would have 95% accuracy, but it would be useless for the business.
**The Solution:** I utilized **SMOTE (Synthetic Minority Over-sampling Technique)** during the training phase to balance the classes. We prioritized the **F1-Score** over raw accuracy to ensure a proper balance between False Positives (wasting QA inspectors' time) and False Negatives (letting defective parts onto the assembly line).

### 4. The BI Dashboard (Honda Disha)
The final deliverable was a Tableau dashboard acting as the UI for the ML model's output. 
* **KPI Banners:** High-level metrics for executive visibility.
* **Pareto Diagnostics:** To enforce the 80/20 rule, instantly identifying the defect categories driving the most scrap cost.
* **Interactive Heatmaps:** Allowing managers to filter the entire dashboard by clicking on high-risk supplier nodes.
* **Action Watchlist:** The direct output of the ML model, giving inspectors a prioritized checklist of which `PRIS_No` shipments to investigate today.

