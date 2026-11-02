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
        
        -- Pull the previous month's data and the actual date of that previous month
        LAG(Monthly_Scrap_Cost) OVER(PARTITION BY Supplier_Name ORDER BY Reporting_Month) AS Raw_Prev_Scrap,
        LAG(Reporting_Month) OVER(PARTITION BY Supplier_Name ORDER BY Reporting_Month) AS Prev_Month
    FROM Monthly_Base
)
SELECT 
    Supplier_Name,
    Reporting_Month,
    Monthly_Scrap_Cost,
    Avg_Rejection_Rate,
    Total_Defect_Incidents,
    Cumulative_Scrap_Cost,
    
    -- ONLY calculate variance if the previous record was exactly 1 month ago. Otherwise, NULL.
    CASE 
        WHEN DATEDIFF(MONTH, Prev_Month, Reporting_Month) = 1 
        THEN (Monthly_Scrap_Cost - Raw_Prev_Scrap)
        ELSE NULL 
    END AS Monthly_Cost_Variance
FROM Trend_Calculations;
GO




CREATE OR ALTER VIEW v_Supplier_Risk_Rankings AS
WITH Supplier_Stats AS (
    SELECT 
        Supplier_Name, 
        COUNT(PRIS_No) AS Total_Defect_Incidents,
        SUM(Total_Scrap_Cost_INR) AS Total_Scrap_Cost,
        AVG(Rejection_Rate_Pct) AS Avg_Rejection_Rate
    FROM WMS_Processed_Data
    GROUP BY Supplier_Name
    HAVING COUNT(PRIS_No) >= 30
), 
Ranked_Suppliers AS (
    SELECT 
        *, 
        PERCENT_RANK() OVER (ORDER BY Avg_Rejection_Rate) AS Rate_Pctile 
    FROM Supplier_Stats
)
SELECT 
    Supplier_Name, 
    Total_Defect_Incidents, 
    Total_Scrap_Cost,
    CAST(Avg_Rejection_Rate AS DECIMAL(5,2)) AS Average_Rejection_Rate,
    CASE 
        WHEN Rate_Pctile >= 0.90 THEN 'Critical'
        WHEN Rate_Pctile >= 0.75 THEN 'Warning'
        ELSE 'Healthy' 
    END AS Health_Status
FROM Ranked_Suppliers;
GO