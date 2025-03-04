use ContosoRetailDW
go


--select * from DimProduct

--1.zwroc pierwszych 10 produktow

select top 10 ProductName as 'Nazwa Produktu' 
from DimProduct

--2.Zwr�� nazw� produkt�w z kluczem pomi�dzy 50 a 100

select ProductName as 'Nazwa Produktu', ProductKey as 'Klucz'
from DimProduct 
where ProductKey between 50 and 100

--3. Zwr�� ilo�� produkt�w ci�szych ni� 5 funt�w (pounds)

Select count(Weight) as 'Ilo�� produkt�w' 
From DimProduct
Where WeightUnitMeasureID = 'pounds' and Weight>5

--4. Zwr�� nazw�, klucz i wag� najl�ejszego Produktu (ounces)

select  top 1 ProductName as Nazwa, ProductKey as Klucz, Weight as Waga
from DimProduct
where WeightUnitMeasureID = 'ounces' and Weight>0
order by Weight

--5. Zwr�� ilo�� produkt�w, kt�re s� bia�e

select COUNT(ColorName) as 'Bia�e produkty'
from DimProduct
where ColorName = 'White'


--6. Zwr�� produkty, kt�rych status jest r�ny od 'On'

select ProductName
from DimProduct
where Status <> 'On'

--7. Zwr�� wszystkie produkty, kt�re s� klasy Economy i koloru srebrnego

select ProductName
from DimProduct
where ClassName = 'Economy' and ColorName = 'Silver'

--8. Sprawd�, kt�ry element(-y) z tabeli FactInventory jest (s�) najd�u�ej w magazynie

--select * from FactInventory

select top 1 with ties  ProductKey
from FactInventory
Order by DaysInStock DESC

--9. Zwr�� klucz elementu, kt�ry jest najdro�szy w powy�szej tabeli

select top 1 ProductKey
from FactInventory
Order by UnitCost DESC --sortowanie malej�ce

--10.Zwr�� klucz elementu oraz ilo�� dost�pn� od r�ki 
--i na zam�wienie oraz znajduj�c� si� w magazynie, kt�ry jest najdro�szy w powy�szej tabeli

select top 1  ProductKey as Klucz, OnHandQuantity as 'Od r�ki', OnOrderQuantity as 'Na zam�wienie',
SafetyStockQuantity as 'W magazynie'
from FactInventory
order by UnitCost DESC

--11.Sprawd� czy wszystkich dost�pnych produkt�w jest wi�cej ni� 100




--12.Sprawd� ile promocji dost�pnych jest w Ameryce

select COUNT(PromotionName) as 'Promocje Ameryka'
from DimPromotion
where PromotionName like '%America%'

--13.Zwr�� nazwy 3 najwi�kszych promocji

select top 3 PromotionName
from DimPromotion
order by DiscountPercent desc

--14.Zwr�� nazwy sklep�w oraz powody ich zamkni�cia, kt�re obecnie s� nieczynne

select StoreName as 'Nazwa Sklepu', CloseReason as 'Przyczyna zamkniecia'
from DimStore
where Status = 'Off'

--15.Zwr�� wszystkie unikatowe nazwy maszyn

select distinct MachineName as 'Nazwy maszyn'
from DimMachine

--16.Sprawd� ile jest maszyn typu HUB01

select COUNT(MachineType) as 'Maszyny typu HUB01'
from DimMachine
where MachineType = 'HUB01'

--17.Sprawd� ile obecnie jest klient�w firmy Contoso

select COUNT(CustomerKey) as 'Liczba Klient�w'
from DimCustomer

--18.Sprawd� ile spo�r�d wszystkich klient�w to kobiety

select COUNT(Gender) as 'Ilo�� Kobiet'
from DimCustomer
where Gender = 'F'

--19.Sprawd� ile spo�r�d wszystkich klient�w to m�czy�ni zarabiaj�cy powy�ej 100000

select COUNT(YearlyIncome) as 'Men over 100K'
from DimCustomer
where Gender='M' and YearlyIncome>100000

--20.Sprawd� ile spo�r�d wszystkich klient�w to samotne kobiety, kt�re uko�czy�y szko�� wy�sz�

select COUNT(CustomerKey) as 'Kobiety'
from DimCustomer
where Gender='F' and MaritalStatus='S' and Education='High School'

--21.Jak si� nazywa najstarszy klient�oraz�ile�ma�lat

select top 1 FirstName + ' ' + LastName as 'Full Name',
DATEDIFF(yy,BirthDate,GETDATE()) as 'Age'

from DimCustomer
where CustomerType = 'Person'
order by Age DESC


