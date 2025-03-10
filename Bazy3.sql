use ContosoRetailDW
go

--1. zwroc ilosc pracownikow w kazdym departamencie, 
--sume wolnych godzin oraz stosunek sumy wolnych godzin do ilosci pracownikow. 
--Calosc posortuj po stosunku malejaco oraz po nazwie departamentu alfabetycnie

SELECT DepartmentName, 
	COUNT(EmployeeKey) as 'EmpQt', 
	SUM(VacationHours) as 'VHSum',
	(SUM(VacationHours)/COUNT(EmployeeKey)) as 'VHtoEmp'
FROM DimEmployee
GROUP BY DepartmentName
ORDER BY  VHtoEmp DESC, DepartmentName ASC

--2.zwoc identyfikator produktu, jego nazwe, ilosc sprzedanych sztuk tego produktu, 
--sumaryczna kwote, minimalna oraz maksymalna znizke. Calosc posortuj po kwocie sprzedazy od najwyzszej.

SELECT p.ProductLabel,
	p.ProductName, 
	SUM(s.SalesQuantity) as 'SalesQt', 
	sq.Quota,
	MIN(s.DiscountAmount) as 'MinDiscount',
	MAX(s.DiscountAmount) as 'MaxDiscount'
FROM DimProduct p
	LEFT JOIN
	FactSales s
	ON p.ProductKey=s.ProductKey
	LEFT JOIN
	(
		SELECT ProductKey, SUM(SalesQuantityQuota) as Quota 
		FROM FactSalesQuota
		GROUP BY ProductKey
	) sq ON p.ProductKey=sq.ProductKey
GROUP BY p.ProductLabel, p.ProductName, sq.Quota
ORDER BY sq.Quota DESC

--3. Uwzgledniajac tylko prognozowana sprzedaz wylicz srednia kwote brutton marzy sprzedazy
--dla kazdego produktu, zwroc tez klucz produktu oraz ilosc produktow


SELECT AVG(sq.GrossMarginQuota) as "AVGMargin", sq.ProductKey, SUM(s.SalesQuantity) as "ProductQt"
FROM (
	SELECT ProductKey, GrossMarginQuota
	FROM FactSalesQuota
	WHERE ScenarioKey=3
	) sq
	INNER JOIN
	FactSales s
	ON sq.ProductKey=s.ProductKey
GROUP BY sq.ProductKey
