import datetime
import json

waluty_na_PLN = {
    "USD": 4.1,
    "EUR": 4.25,
    "GBP": 5.3,
    "CHF": 5.65,
    "CSK": 0.65,
}
with open('zasoby.json', 'r') as jf:
    zasoby = json.load(jf)

def rachunek(waluta, ilosc, cena):
    
    """Funkcja zapisuje dane transakcji do pliku z nazwa waluty
     Odejmuje od zasobow kantoru ilosc waluty zakupionej przez klienta"""
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    zasoby[waluta] = zasoby[waluta] - ilosc
    
    with open('zasoby.json', 'w') as jf:
        json.dump(zasoby, jf)

    with open(waluta + ".txt", "a") as file:
        print(f"Data transakcji: {date} \nIlosc zakupionej waluty: {(ilosc):.2f} {waluta} \nCena(PLN): {(cena):.2f} \n", file=file)



print(f"Witaj w kantorze \nDostepne waluty: \n{list(waluty_na_PLN.keys())}")
waluta = str(input("Jaka walute chcesz zakupic?:")).upper()
if waluta not in waluty_na_PLN.keys():
    print("Nie mamy takiej waluty wybierz inna")
else:
    try:   
        
        ilosc = float(input("W jakiej ilości?:"))
        if zasoby[waluta] < ilosc:
            print(f'Za malo zasobow {waluta} w kantorze, dostepnych jest {zasoby[waluta]:.2f} {waluta}')
        else:
            
            budzet = float(input("Podaj jakim budzetem dysponujesz(PLN):"))
            cena = round((ilosc * waluty_na_PLN[waluta]), 2) 
            if budzet < cena:
                print(f'Masz za malo pieniedzy by kupic {(ilosc):.2f} {waluta}')
            else:
                rachunek(waluta, ilosc, cena)
                print(f"Do zaplacenia {cena:.2f} PLN")
        
    except ValueError:
        print("Podaj liczbowo")
