import tools.databases.DBManager as dbmanager
import domain.resources as resources 
import domain.currencies as currencies
import tools.converters.number_converters as number_converts
import tools.const.messages as messages

currencies_list = dbmanager.get_currencies()

print("Witaj w kantorze")
while True:
    try:   
        budget_input_value = input("Podaj budzet jakim dysponujesz(PLN): ")
        budget = number_converts.rounded_float(budget_input_value)
        break
    except ValueError:
        print("Budzet musi byc liczba rzeczywista")

##print(f"Dostępne waluty: {' '.join(currencies_list)}")
##while True:
##    currency_input_value = input("Wybierz walute, ktora chcesz kupic: ")
##    currency = currency_input_value.upper()
##    if currency in currencies_list:
##        break
##    else:   
##        print("Nie mamy takiej waluty (Podaj 3 litery)")
##        continue

for n, currency_name in enumerate(currencies_list, 1):
    print(f"{n}. {currency_name}")
print("X. wyjscie")

while True:
    try:
        currency_input_value = input(f"Wybierz walute, ktora chcesz kupic (wpisz cyfre od 1 do {n}) lub wyjdz(x): ")
        if currency_input_value == "x" or currency_input_value == "X":
            print("Do zobaczenia!")
            quit()
        else:
            currency = currencies_list[(int(currency_input_value)) - 1]
            break
    except ValueError:
        print(messages.currencyerror(n))
    except IndexError:
        print(messages.currencyerror(n))

print(f"Wybrales {currency}")
currency_in_stock = dbmanager.get_resource_quantity(currency)


while True:
    try:
        quantity_input_value = input(f"Podaj ile {currency} chcesz zakupic: ")
        quantity = number_converts.rounded_float(quantity_input_value)
        if quantity > currency_in_stock:
            print(f"W magazynie jest za malo zasobow {currency}, dostepnych maksymalnie {currency_in_stock} {currency}")
        else:
            break
    except ValueError:
        print("Ilosc musi byc liczba rzeczywista")
    
    

cost = currencies.cost_count(currency, quantity)
if budget < cost:
    print(f"Masz za malo srodkow by zakupic {quantity:.2f} {currency}, koszt wynosi {cost} PLN")
else:
    resources.new_transaction(currency, quantity, cost)
    print(f"Do zaplaty {cost:.2f} PLN")