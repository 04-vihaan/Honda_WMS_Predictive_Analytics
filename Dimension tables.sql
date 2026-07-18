CREATE TABLE Dim_Supplier (
    Supplier_ID INT IDENTITY(1,1) PRIMARY KEY,
    Supplier_Name NVARCHAR(100) NOT NULL,
    Supplier_Region NVARCHAR(50)
);

CREATE TABLE Dim_Part (
    Part_Code NVARCHAR(50) PRIMARY KEY,
    Part_Description NVARCHAR(100),
    Inventory_Category NVARCHAR(50),
    Unit_Cost_INR DECIMAL(10,2)
);

CREATE TABLE Fact_PRIS_Logs (
    PRIS_No NVARCHAR(50) PRIMARY KEY,
    Supplier_Name NVARCHAR(100),
    Part_Code NVARCHAR(50),
    Total_Received_Qty INT,
    Rejected_Qty INT,
    Scrap_Qty INT,
    Inventory_Location NVARCHAR(100),
    Rejected_Category NVARCHAR(100),
    Shift_Timing NVARCHAR(50),
    Inspector_ID NVARCHAR(50),
    Defect_Severity NVARCHAR(50),
    Transit_Time_Days INT,
    Rejection_Date DATE
);


GO
CREATE VIEW vw_PRIS_Executive_Summary AS
SELECT 
    Supplier_Name,
    Rejected_Category,
    SUM(Scrap_Qty) AS Total_Scrap_Items,
    SUM(Scrap_Qty * p.Unit_Cost_INR) AS Total_Financial_Loss,
    AVG(CAST(Rejected_Qty AS FLOAT) / NULLIF(Total_Received_Qty, 0)) * 100 AS Avg_Rejection_Rate
FROM 
    Fact_PRIS_Logs f
JOIN 
    Dim_Part p ON f.Part_Code = p.Part_Code
GROUP BY 
    Supplier_Name, Rejected_Category;
GO