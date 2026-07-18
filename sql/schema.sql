CREATE DATABASE Honda_WMS_Analytics;
GO

USE Honda_WMS_Analytics;
GO

\CREATE TABLE WMS_Processed_Data (
    PRIS_No VARCHAR(50) PRIMARY KEY,
    Supplier_Name VARCHAR(100),
    Part_Code VARCHAR(50),
    Part_Description VARCHAR(150),
    Rejection_Date DATE,
    Total_Scrap_Cost_INR DECIMAL(18, 2), 
    Rejection_Rate_Pct DECIMAL(5, 2),
    Supplier_Enc INT,
    Part_Enc INT,
    Is_High_Risk INT,
    ML_Risk_Prediction INT,
    Risk_Label VARCHAR(20)
);
GO

PRINT 'Database and WMS_Processed_Data table successfully created!';