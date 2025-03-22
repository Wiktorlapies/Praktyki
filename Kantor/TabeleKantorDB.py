"""
Tworzy tabele w bazie Kantor
"""
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


with pyodbc.connect(connection_string) as conn:
    cursor = conn.cursor()
    cursor.execute(Create_Table_Currencies)
    cursor.execute(Create_Table_ExchangeRates)
    cursor.execute(Create_Table_Resources)
    cursor.execute(Create_Table_Transactions)


