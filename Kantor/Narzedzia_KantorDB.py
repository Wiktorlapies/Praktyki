"""
Tworzy tabele w bazie Kantor
"""
Currencies = {
    "USD": [4.1, 100000],
    "EUR": [4.25, 20000],
    "GBP": [5.3, 150000],
    "CHF": [5.65, 10000],
    "CSK": [0.65, 15000],
    "UAH": [0.093, 2000000],
}

import pyodbc 
import zapytania
from zapytania import *

DRIVER_NAME = '{ODBC Driver 17 for SQL Server}'
SERVER_NAME = "KomputerWiktor\\SQLEXPRESS" #Trzeba dodac drugi \
DATABASE_NAME = 'Kantor'

connection_string = f"""
    DRIVER={DRIVER_NAME};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""
def Reset_Database():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(Drop_Tables)
        cursor.execute(Create_Table_Currencies)
        cursor.execute(Create_Table_ExchangeRates)
        cursor.execute(Create_Table_Resources)
        cursor.execute(Create_Table_Transactions)

def Add_Currencies():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        for name in Currencies.keys():
            cursor.execute(Rows_in_Currencies, name)
            cursor.execute(Get_CurrencyID, name)
            ID = cursor.fetchone()
            cursor.execute(Rows_in_ExchangeRates, ID[0], Currencies[name][0])
            

def Add_Resources():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        for name in Currencies.keys():
            cursor.execute(Get_CurrencyID, name)
            ID = cursor.fetchone()
            cursor.execute(Rows_in_Resources, ID[0], Currencies[name][1])
            

def Subtract_from_Resources(currency, quantity):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(Get_Quantity, currency)
        Data = cursor.fetchone()
        Current_Quantity = Data[0]
        ID = Data[1]
        New_Quantity = round((Current_Quantity - quantity),2)
        cursor.execute(Update_Resources, New_Quantity, ID)

def New_Transaction(currency, quantity):
    Subtract_from_Resources(currency, quantity)
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(Get_ExchangeRate, currency)
        Data = cursor.fetchone()
        ExRate = Data[0]
        ID = Data[1]
        Cost = round((quantity * ExRate), 2)
        cursor.execute(Add_Transaction, ID, quantity, Cost)
    return Cost