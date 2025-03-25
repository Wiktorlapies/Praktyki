import tools.databases.DBManager as dbmanager 

def subtract_from_resources(currency, quantity):
        data = dbmanager.get_resources(currency)
        Current_Quantity = data[0]
        
        new_Quantity = round((Current_Quantity - quantity),2)
        currency_ID = data[1]

        dbmanager.update_resources(currency_ID, new_Quantity)

def new_transaction(currency, quantity, cost):
    subtract_from_resources(currency, quantity)
    dbmanager.new_transaction(currency, quantity, cost)
        