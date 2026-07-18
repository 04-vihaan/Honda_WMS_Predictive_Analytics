USE Honda_WMS_Analytics;
GO


CREATE OR ALTER VIEW v_Executive_Monthly_Trends AS
WITH Monthly_Base AS (
    SELECT 
        Supplier_Name,

        DATEFROMPARTS(YEAR(Rejection_Date), MONTH(Rejection_Date), 1) AS Reporting_Month,
        SUM(Total_Scrap_Cost_INR) AS Monthly_Scrap_Cost,
        AVG(Rejection_Rate_Pct) AS Avg_Rejection_Rate,
        COUNT(PRIS_No) AS Total_Defect_Incidents
    FROM WMS_Processed_Data
    GROUP BY Supplier_Name, YEAR(Rejection_Date), MONTH(Rejection_Date)
),
Trend_Calculations AS (
    SELECT 
        Supplier_Name,
        Reporting_Month,
        Monthly_Scrap_Cost,
        Avg_Rejection_Rate,
        Total_Defect_Incidents,

        SUM(Monthly_Scrap_Cost) OVER(PARTITION BY Supplier_Name ORDER BY Reporting_Month) AS Cumulative_Scrap_Cost,

        LAG(Monthly_Scrap_Cost) OVER(PARTITION BY Supplier_Name ORDER BY Reporting_Month) AS Prev_Month_Scrap
    FROM Monthly_Base
)
SELECT 
    Supplier_Name,
    Reporting_Month,
    Monthly_Scrap_Cost,
    Avg_Rejection_Rate,
    Total_Defect_Incidents,
    Cumulative_Scrap_Cost,

    (Monthly_Scrap_Cost - ISNULL(Prev_Month_Scrap, 0)) AS Monthly_Cost_Variance
FROM Trend_Calculations;
GO




CREATE OR ALTER VIEW v_Supplier_Risk_Rankings AS
WITH Supplier_Metrics AS (
    SELECT 
        Supplier_Name,
        COUNT(PRIS_No) AS Total_Rejections,
        SUM(Total_Scrap_Cost_INR) AS Total_Financial_Loss,

        SUM(CASE WHEN ML_Risk_Prediction = 1 THEN 1 ELSE 0 END) AS ML_High_Risk_Count
    FROM WMS_Processed_Data
    GROUP BY Supplier_Name
)
SELECT 
    Supplier_Name,
    Total_rejections,
    Total_Financial_Loss,
    ML_High_Risk_Count,

    DENSE_RANK() OVER (ORDER BY Total_Financial_Loss DESC) AS Financial_Risk_Rank
FROM Supplier_Metrics;
GO