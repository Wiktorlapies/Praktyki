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
        Date DATETIME DEFAULT GETDATE() NOT NULL,
        CONSTRAINT PK_Transaction PRIMARY KEY(ID),
        CONSTRAINT FK_Transaction_Currency FOREIGN KEY(CurrencyID) REFERENCES dbo.Currencies(ID)
    );
"""