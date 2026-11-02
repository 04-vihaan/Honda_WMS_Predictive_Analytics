CREATE OR ALTER PROCEDURE sp_GetSupplierHealthProfile
    @TargetSupplier VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
        Supplier_Name,
        COUNT(PRIS_No) AS Total_Defect_Incidents,
        SUM(Total_Scrap_Cost_INR) AS Total_Scrap_Cost_INR,
        CAST(AVG(Rejection_Rate_Pct) AS DECIMAL(5,2)) AS Average_Rejection_Rate,
        CASE
            WHEN SUM(Total_Scrap_Cost_INR) > 50000000 THEN 'Critical'
            WHEN SUM(Total_Scrap_Cost_INR) > 25000000 THEN 'Warning'
            ELSE 'Healthy'
        END AS Health_Status
    FROM WMS_Processed_Data
    WHERE Supplier_Name = @TargetSupplier
    GROUP BY Supplier_Name;
END;
GO