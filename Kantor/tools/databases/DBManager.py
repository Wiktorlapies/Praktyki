
import pyodbc 
#from domain.currencies import Currencies
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
def connect():
    with pyodbc.connect(connection_string) as conn:
        return conn.cursor()

def Reset_Database():
        cursor = connect()
        cursor.execute(SQL_Drop_Tables)
        cursor.execute(SQL_Create_Table_Currencies)
        cursor.execute(SQL_Create_Table_ExchangeRates)
        cursor.execute(SQL_Create_Table_Resources)
        cursor.execute(SQL_Create_Table_Transactions)

def Add_Currencies():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        for name in Currencies.keys():
            cursor.execute(SQL_Rows_in_Currencies, name)
            cursor.execute(SQL_Get_CurrencyID, name)
            ID = cursor.fetchone()
            cursor.execute(SQL_Rows_in_ExchangeRates, ID[0], Currencies[name][0])
            

def Add_Resources():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        for name in Currencies.keys():
            cursor.execute(SQL_Get_CurrencyID, name)
            ID = cursor.fetchone()
            cursor.execute(SQL_Rows_in_Resources, ID[0], Currencies[name][1])
            

def new_transaction(currency, quantity, cost):
        cursor = connect()
        cursor.execute(SQL_Get_CurrencyID, currency)
        ID = cursor.fetchone()[0]
        cursor.execute(SQL_Add_Transaction, ID, quantity, cost)
        cursor.commit()

def get_currencies():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_Get_Currencies)
        currencies = [name[0] for name in cursor.fetchall()]
    return currencies

def cost_count(currency, quantity):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_Get_ExchangeRate, currency)
        ExRate = cursor.fetchone()[0]
    cost = round((quantity * ExRate), 2)
    return cost

def Get_Resource_quantity(currency):
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_Get_Resource_Quantity, currency)
        stock = cursor.fetchone()[0]
    return stock

def get_Resources(currency):
        cursor = connect()
        cursor.execute(SQL_Get_Resource, currency)
        Data = cursor.fetchone()
        return Data
        #cursor.execute(SQL_Update_Resources, New_Quantity, ID)

def update_resourcves(curremcy_ID, quantity):
        cursor = connect()
        cursor.execute(SQL_Update_Resources, quantity, curremcy_ID)