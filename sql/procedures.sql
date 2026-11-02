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

        SET Health_Status = CASE 
    WHEN Total_Scrap_Cost > 50000 THEN 'Critical'
    WHEN Total_Scrap_Cost > 10000 THEN 'Warning'
    ELSE 'Healthy'
END
    FROM 
        WMS_Processed_Data
    WHERE 
        Supplier_Name = @TargetSupplier
    GROUP BY 
        Supplier_Name;
END;
GO



