

CREATE VIEW vw_Tableau_Supplier_Risk AS
SELECT 
    Supplier_Name,
    COUNT(PRIS_No) AS Total_Incidents,
    SUM(Total_Received_Qty) AS Total_Volume,
    SUM(Scrap_Qty) AS Total_Scrap,
    (SUM(Rejected_Qty) * 100.0 / NULLIF(SUM(Total_Received_Qty), 0)) AS Avg_Rejection_Rate
FROM fact_pris_logs
GROUP BY Supplier_Name;
GO



CREATE PROCEDURE FlagCriticalDefects
AS
BEGIN
    UPDATE fact_pris_logs
    SET Risk_Label = 'CRITICAL ALERT'
    WHERE Rejection_Rate_Pct > 15.0
      AND Defect_Severity = 'Critical (Total Scrap)';
      

    INSERT INTO system_logs (log_type, log_message, run_date)
    VALUES ('CRON', 'FlagCriticalDefects executed successfully', GETDATE());
END;
GO