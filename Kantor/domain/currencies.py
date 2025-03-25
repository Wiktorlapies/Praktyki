import tools.databases.DBManager as dbmanager

currencies = {
    "USD": [4.1, 100000],
    "EUR": [4.25, 20000],
    "GBP": [5.3, 150000],
    "CHF": [5.65, 10000],
    "CSK": [0.65, 15000],
    "UAH": [0.093, 2000000],
}

def cost_count(currency, quantity):
    exrate = dbmanager.get_exchange_rate(currency)
    cost = round((quantity * exrate), 2)
    return cost