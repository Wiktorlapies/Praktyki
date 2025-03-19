import json
zasoby = {
    "USD": 100000.00,
    "EUR": 25000.00,
    "GBP": 150000.00,
    "CHF": 10000.00,
    "CSK": 250000.00, 
}
with open("zasoby.json", 'w') as jf:
    json.dump(zasoby, jf)