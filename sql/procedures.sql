USE Honda_WMS_Analytics;
GO



CREATE OR ALTER PROCEDURE sp_GetSupplierHealthProfile
    @TargetSupplier VARCHAR(100) 
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        Supplier_Name,
        COUNT(PRIS_No) AS Total_Defect_Incidents,
        SUM(Total_Scrap_Cost_INR) AS Total_Financial_Damage_INR,
        CAST(AVG(Rejection_Rate_Pct) AS DECIMAL(5,2)) AS Average_Rejection_Rate,

        SUM(CASE WHEN ML_Risk_Prediction = 1 THEN 1 ELSE 0 END) AS Total_High_Risk_Flags,

        CASE 
            WHEN SUM(CASE WHEN ML_Risk_Prediction = 1 THEN 1 ELSE 0 END) > 10 THEN 'CRITICAL RISK'
            WHEN SUM(CASE WHEN ML_Risk_Prediction = 1 THEN 1 ELSE 0 END) BETWEEN 1 AND 10 THEN 'MONITOR'
            ELSE 'HEALTHY'
        END AS Supplier_Health_Status
    FROM 
        WMS_Processed_Data
    WHERE 
        Supplier_Name = @TargetSupplier
    GROUP BY 
        Supplier_Name;
END;
GO



