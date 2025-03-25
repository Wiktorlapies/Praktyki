
import pyodbc 
from tools.databases.DBQuerries import *
from domain.currencies import *
DRIVER_NAME = '{ODBC Driver 17 for SQL Server}'
SERVER_NAME = "KomputerWiktor\\SQLEXPRESS" #Trzeba dodac drugi \
DATABASE_NAME = 'Kantor'

connection_string = f"""
    DRIVER={DRIVER_NAME};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
"""
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

def reset_database():
        with conn:
            cursor.execute(SQL_Drop_Tables)
            cursor.execute(SQL_Create_Table_Currencies)
            cursor.execute(SQL_Create_Table_ExchangeRates)
            cursor.execute(SQL_Create_Table_Resources)
            cursor.execute(SQL_Create_Table_Transactions)

def add_currencies():
    with conn:
        for name in currencies.keys():
            cursor.execute(SQL_Rows_in_Currencies, name)
            cursor.execute(SQL_Get_CurrencyID, name)
            ID = cursor.fetchone()
            cursor.execute(SQL_Rows_in_ExchangeRates, ID[0], currencies[name][0])
            

def add_resources():
    with conn:
        for name in currencies.keys():
            cursor.execute(SQL_Get_CurrencyID, name)
            ID = cursor.fetchone()
            cursor.execute(SQL_Rows_in_Resources, ID[0], currencies[name][1])
            

def new_transaction(currency, quantity, cost):
    with conn:
        cursor.execute(SQL_Get_CurrencyID, currency)
        ID = cursor.fetchone()[0]
        cursor.execute(SQL_Add_Transaction, ID, quantity, cost)
        

def get_currencies():
    with conn:
        cursor.execute(SQL_Get_Currencies)
        currencies = [name[0] for name in cursor.fetchall()]
    return currencies

def get_exchange_rate(currency):
    with conn:
        cursor.execute(SQL_Get_ExchangeRate, currency)
        exrate = cursor.fetchone()[0]
    return exrate

def get_resource_quantity(currency):
    with conn:
        cursor.execute(SQL_Get_Resource_Quantity, currency)
        stock = cursor.fetchone()[0]
    return stock

def get_resources(currency):
    with conn:
        cursor.execute(SQL_Get_Resource, currency)
        Data = cursor.fetchone()
    return Data
            

def update_resources(curremcy_ID, quantity):
    with conn:
        cursor.execute(SQL_Update_Resources, quantity, curremcy_ID)