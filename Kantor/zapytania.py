Drop_Tables = """
    DROP TABLE dbo.Transactions
    DROP TABLE dbo.Resources
    DROP TABLE dbo.ExchangeRates
    DROP TABLE dbo.Currencies
"""

Create_Table_Currencies = """
    CREATE TABLE dbo.Currencies(
        ID INT IDENTITY(1,1) NOT NULL,
        Name VARCHAR(10) NOT NULL,
        CONSTRAINT PK_Currency PRIMARY KEY(ID)
    );
"""

Create_Table_ExchangeRates = """
    CREATE TABLE dbo.ExchangeRates(
        ID INT IDENTITY(1,1) NOT NULL,
        CurrencyID INT NOT NULL,
        ExchangeRate FLOAT NOT NULL,
        CONSTRAINT PK_ExchangeRate PRIMARY KEY(ID),
        CONSTRAINT FK_ExchangeRate_Currency FOREIGN KEY(CurrencyID) REFERENCES dbo.Currencies(ID)
    );
"""

Create_Table_Resources = """
    CREATE TABLE dbo.Resources(
        ID INT IDENTITY(1,1) NOT NULL,
        CurrencyID INT NOT NULL,
        Quantity FLOAT NOT NULL,
        CONSTRAINT PK_Resource PRIMARY KEY(ID),
        CONSTRAINT FK_Resource_Currency FOREIGN KEY(CurrencyID) REFERENCES dbo.Currencies(ID)
    );
"""

Create_Table_Transactions = """
    CREATE TABLE dbo.Transactions(
        ID INT IDENTITY(1,1) NOT NULL,
        CurrencyID INT NOT NULL,
        Quantity FLOAT NOT NULL,
        Cost FLOAT NOT NULL,
        Date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
        CONSTRAINT PK_Transaction PRIMARY KEY(ID),
        CONSTRAINT FK_Transaction_Currency FOREIGN KEY(CurrencyID) REFERENCES dbo.Currencies(ID)
    );
"""

Rows_in_Currencies = """
    INSERT INTO dbo.Currencies (Name) VALUES
        (?)
"""

Rows_in_ExchangeRates = """
    INSERT INTO dbo.ExchangeRates (CurrencyID, ExchangeRate) VALUES
        (?, ?)
"""

Rows_in_Resources = """
    INSERT INTO dbo.Resources (CurrencyID, Quantity) VALUES
        (?, ?)
"""

Get_CurrencyID = """
    SELECT ID 
    FROM Currencies
    WHERE Name = ?
"""

Get_Quantity = """
    SELECT r.Quantity, r.ID
    FROM Resources r JOIN Currencies c ON r.CurrencyID = c.ID
    WHERE c.Name = ?
"""

Get_ExchangeRate = """
    SELECT er.ExchangeRate, c.ID
    FROM ExchangeRates er JOIN Currencies c ON er.CurrencyID = c.ID
    WHERE c.Name = ?
"""

Update_Resources = """
    UPDATE dbo.Resources
    SET Quantity=?
    WHERE ID=?
"""

Add_Transaction = """
    INSERT INTO dbo.Transactions (CurrencyID, Quantity, Cost) VALUES
        (?,?,?)
"""