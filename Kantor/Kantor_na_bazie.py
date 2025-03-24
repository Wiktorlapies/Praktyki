import tools.databases.DBManager as dbmanager
import domain.resources as resources 

currencies = dbmanager.get_currencies()

print("Witaj w kantorze")
while True:
    try:   
        input_value = input("Podaj budzet jakim dysponujesz(PLN): ")
        budget = round(float(input_value), 2)
        break
    except ValueError:
        print("Podaj liczbe")

print(f"Dostępne waluty: {' '.join(currencies)}")


while True:
    currency_input_value = input("Wybierz walute, ktora chcesz kupic: ")
    currency = currency_input_value.upper()
    if currency not in currencies:
        print("Nie mamy takiej waluty (3 litery)")
        continue
    break


print(f"Wybrales {currency}")
currency_in_stock = dbmanager.Get_Resource_quantity(currency)


while True:
    try:
        quantity = round((float(input(f"Podaj ile {currency} chcesz zakupic: "))), 2)
        if quantity > currency_in_stock:
            print(f"W magazynie jest za malo zasobow {currency}, dostepnych maksymalnie {currency_in_stock} {currency}")
        else:
            break
    except ValueError:
        print("Podaj liczbe")
    
    

cost = dbmanager.cost_count(currency, quantity)
if budget < cost:
    print(f"Masz za malo srodkow by zakupic {quantity:.2f} {currency}, koszt wynosi {cost} PLN")
else:
    resources.new_transaction(currency, quantity, cost)
    print(f"Do zaplaty {cost:.2f} PLN")