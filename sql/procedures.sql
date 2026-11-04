CREATE OR ALTER PROCEDURE sp_GetSupplierHealthProfile @TargetSupplier VARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;
    IF EXISTS (SELECT 1 FROM v_Supplier_Risk_Rankings WHERE Supplier_Name = @TargetSupplier)
        SELECT * FROM v_Supplier_Risk_Rankings WHERE Supplier_Name = @TargetSupplier;
    ELSE
        SELECT @TargetSupplier AS Supplier_Name,
               'Insufficient data (<30 incidents) or unknown supplier' AS Health_Status;
END;
GO