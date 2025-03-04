use ContosoRetailDW
go


--select * from DimProduct

--1.zwroc pierwszych 10 produktow

select top 10 ProductName as 'Nazwa Produktu' 
from DimProduct

--2.Zwróæ nazwê produktów z kluczem pomiêdzy 50 a 100

select ProductName as 'Nazwa Produktu', ProductKey as 'Klucz'
from DimProduct 
where ProductKey between 50 and 100

--3. Zwróæ iloœæ produktów ciê¿szych ni¿ 5 funtów (pounds)

Select count(Weight) as 'Iloœæ produktów' 
From DimProduct
Where WeightUnitMeasureID = 'pounds' and Weight>5

--4. Zwróæ nazwê, klucz i wagê najl¿ejszego Produktu (ounces)

select  top 1 ProductName as Nazwa, ProductKey as Klucz, Weight as Waga
from DimProduct
where WeightUnitMeasureID = 'ounces' and Weight>0
order by Weight

--5. Zwróæ iloœæ produktów, które s¹ bia³e

select COUNT(ColorName) as 'Bia³e produkty'
from DimProduct
where ColorName = 'White'


--6. Zwróæ produkty, których status jest ró¿ny od 'On'

select ProductName
from DimProduct
where Status <> 'On'

--7. Zwróæ wszystkie produkty, które s¹ klasy Economy i koloru srebrnego

select ProductName
from DimProduct
where ClassName = 'Economy' and ColorName = 'Silver'

--8. SprawdŸ, który element(-y) z tabeli FactInventory jest (s¹) najd³u¿ej w magazynie

--select * from FactInventory

select top 1 with ties  ProductKey
from FactInventory
Order by DaysInStock DESC

--9. Zwróæ klucz elementu, który jest najdro¿szy w powy¿szej tabeli

select top 1 ProductKey
from FactInventory
Order by UnitCost DESC --sortowanie malej¹ce

--10.Zwróæ klucz elementu oraz iloœæ dostêpn¹ od rêki 
--i na zamówienie oraz znajduj¹c¹ siê w magazynie, który jest najdro¿szy w powy¿szej tabeli

select top 1  ProductKey as Klucz, OnHandQuantity as 'Od rêki', OnOrderQuantity as 'Na zamówienie',
SafetyStockQuantity as 'W magazynie'
from FactInventory
order by UnitCost DESC

--11.SprawdŸ czy wszystkich dostêpnych produktów jest wiêcej ni¿ 100




--12.SprawdŸ ile promocji dostêpnych jest w Ameryce

select COUNT(PromotionName) as 'Promocje Ameryka'
from DimPromotion
where PromotionName like '%America%'

--13.Zwróæ nazwy 3 najwiêkszych promocji

select top 3 PromotionName
from DimPromotion
order by DiscountPercent desc

--14.Zwróæ nazwy sklepów oraz powody ich zamkniêcia, które obecnie s¹ nieczynne

select StoreName as 'Nazwa Sklepu', CloseReason as 'Przyczyna zamkniecia'
from DimStore
where Status = 'Off'

--15.Zwróæ wszystkie unikatowe nazwy maszyn

select distinct MachineName as 'Nazwy maszyn'
from DimMachine

--16.SprawdŸ ile jest maszyn typu HUB01

select COUNT(MachineType) as 'Maszyny typu HUB01'
from DimMachine
where MachineType = 'HUB01'

--17.SprawdŸ ile obecnie jest klientów firmy Contoso

select COUNT(CustomerKey) as 'Liczba Klientów'
from DimCustomer

--18.SprawdŸ ile spoœród wszystkich klientów to kobiety

select COUNT(Gender) as 'Iloœæ Kobiet'
from DimCustomer
where Gender = 'F'

--19.SprawdŸ ile spoœród wszystkich klientów to mê¿czyŸni zarabiaj¹cy powy¿ej 100000

select COUNT(YearlyIncome) as 'Men over 100K'
from DimCustomer
where Gender='M' and YearlyIncome>100000

--20.SprawdŸ ile spoœród wszystkich klientów to samotne kobiety, które ukoñczy³y szko³ê wy¿sz¹

select COUNT(CustomerKey) as 'Kobiety'
from DimCustomer
where Gender='F' and MaritalStatus='S' and Education='High School'

--21.Jak siê nazywa najstarszy klient oraz ile ma lat

select top 1 FirstName + ' ' + LastName as 'Full Name',
DATEDIFF(yy,BirthDate,GETDATE()) as 'Age'

from DimCustomer
where CustomerType = 'Person'
order by Age DESC


