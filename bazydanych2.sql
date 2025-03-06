USE ContosoRetailDW
GO

--1. Zwroc informacje o sumie sprzedanych produktow wraz z jego nazwa

SELECT p.ProductName, fs.SalesQuantity
FROM dbo.DimProduct p LEFT JOIN dbo.FactSales fs ON p.ProductKey = fs.ProductKey

--2. Zwroc najlepiej i najgorzej sprzedajacy sie produkt

SELECT 
	(
	SELECT TOP 1 p.ProductName
	FROM dbo.DimProduct p LEFT JOIN dbo.FactSales fs ON p.ProductKey = fs.ProductKey
	WHERE fs.SalesQuantity = 
		(
		SELECT MAX(fs.SalesQuantity)
		FROM dbo.FactSales fs
		) 
	) as HighestSale,
	(
	SELECT TOP 1  p.ProductName
	FROM dbo.DimProduct p LEFT JOIN dbo.FactSales fs ON p.ProductKey = fs.ProductKey
	WHERE fs.SalesQuantity = 
		(
		SELECT MIN(fs.SalesQuantity)
		FROM dbo.FactSales fs
		) 
	) as LowestSale


--3. Zwroc dostepne promocje dla produktow z fabryki "Northwind Traders"

SELECT DISTINCT pr.PromotionName
FROM dbo.DimProduct p INNER JOIN dbo.FactSales fs ON p.ProductKey=fs.ProductKey
	INNER JOIN dbo.DimPromotion pr ON fs.PromotionKey=pr.PromotionKey
WHERE p.Manufacturer = 'Northwind Traders'
	AND pr.PromotionName <> 'No Discount'

--4. Zwroc imie i nazwisko pracownika, jego stanowisko i dzial w jakim pracuje oraz informacje o jego przelozonym i dziale w jakim pracuje.

select 
	e1.FirstName + ' ' + ISNULL(e1.MiddleName,'') + ' ' + e1.LastName as 'Employee', e1.Title, e1.DepartmentName,
	e2.FirstName + ' ' + ISNULL(e2.MiddleName,'') + ' ' + e2.LastName as 'Supervisor', e2.DepartmentName as 'SupervisorsDepartmentName'
from dbo.DimEmployee e1 LEFT JOIN dbo.DimEmployee e2 ON e1.ParentEmployeeKey = e2.EmployeeKey
ORDER BY e1.EmployeeKey

--5. zwroc informacje ile dni oraz w jakim magazynie znajduja sie produkty

select p.ProductName, fi.DaysInStock, s.StoreName
from
	dbo.DimProduct p
	LEFT JOIN
	(
	dbo.FactInventory fi INNER JOIN dbo.DimStore s ON fi.StoreKey=s.StoreKey
	) ON p.ProductKey=fi.ProductKey
