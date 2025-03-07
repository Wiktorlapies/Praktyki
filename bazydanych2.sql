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

--6. Dla kazdego sklepu Zwroc informacje o jego nazwie, miescie kraju i kontynencie, w ktoym sie znajduje


SELECT s.StoreName, g.CityName as 'City', g.ContinentName as Continent 
FROM DimStore s LEFT JOIN DimGeography g ON s.GeographyKey=g.GeographyKey

--7. Zwroc informacje ile jest sklepow na kazdym kontynencie

SELECT g.ContinentName, COUNT(s.StoreName) as 'StoreQuantity'
FROM DimGeography g LEFT JOIN DimStore s ON g.GeographyKey=s.GeographyKey
GROUP BY g.ContinentName 

--8. Dla kazdego sklepu z Azji zwroc informacje kto jest producentem maszyny fiskalnej oraz jej typir

SELECT s.StoreName, m.VendorName, m.MachineType
FROM DimStore s 
	INNER JOIN 
	DimGeography g ON s.GeographyKey=g.GeographyKey 
	AND g.ContinentName='Asia'
	LEFT JOIN
	DimMachine m ON s.StoreKey=m.StoreKey

--9. Sprawdz ile maszyn kazdego producenta jest uzywanych w sklepach w Europie

SELECT m.VendorName, COUNT(m.MachineName) as 'Quantity'
FROM DimStore s 
	INNER JOIN 
	DimGeography g ON s.GeographyKey=g.GeographyKey 
	AND g.ContinentName='Europe'
	INNER JOIN
	DimMachine m ON s.StoreKey=m.StoreKey
GROUP BY m.VendorName

--10. Sprawdz ile maszyn kazdego producenta oraz roznego typu jest uzywanych w sklepach w Europie

SELECT m.VendorName, m.MachineType, COUNT(m.MachineName) as 'Quantity'
FROM DimStore s 
	INNER JOIN 
	DimGeography g ON s.GeographyKey=g.GeographyKey 
	AND g.ContinentName='Europe'
	INNER JOIN
	DimMachine m ON s.StoreKey=m.StoreKey
GROUP BY m.VendorName, m.MachineType


--11. Zwroc informacje o produktach sprzedanych online:
--nazwe produktu, marke, ilosc sprzedanych sztuk, cene,
--kwote obnizki, procent obnizki, nazwe sklepu sprzedajacego, typ klienta, nazwe waluty

SELECT p.ProductName, 
	COUNT(os.SalesQuantity) as 'SalesQuantity', 
	os.UnitPrice,
	os.DiscountAmount, 
	pr.DiscountPercent, 
	s.StoreName,
	c.CustomerType,
	cu.CurrencyName
FROM DimProduct p
	INNER JOIN 
	FactOnlineSales os ON p.ProductKey=os.ProductKey
	INNER JOIN
	DimPromotion pr ON os.PromotionKey=pr.PromotionKey
	INNER JOIN
	DimStore s ON os.StoreKey=s.StoreKey
	INNER JOIN 
	DimCustomer c ON os.CustomerKey=c.CustomerKey
	INNER JOIN
	DimCurrency cu ON os.CurrencyKey=cu.CurrencyKey

GROUP BY p.ProductName,
	os.UnitPrice,
	os.DiscountAmount,
	pr.DiscountPercent,
	s.StoreName,
	c.CustomerType,
	cu.CurrencyName

