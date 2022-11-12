import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def Sphinkx_Override(TargetPointer):
    Qualified_Memmory = TargetPointer

    SHADOW_USERPROFILE_CONSTRUCTOR = """ CREATE TABLE IF NOT EXISTS UserClassProfiles(
                                        UserToken text NOT NULL  ,
                                        FullName text NOT NULL,
                                        EmailAddress text NOT NULL ,
                                        PrimaryPhone text NOT NULL ,
                                        SecondaryPhone text NOT NULL ,
                                        Gender text NOT NULL ,
                                        UserID text NOT NULL ,
                                        SecureID text NOT NULL ,
                                        Country text NOT NULL ,
                                        State text NOT NULL ,
                                        ProfilePath text NOT NULL
                                    ); """

    SHADOW_ASSETSTORE_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS  AssetStore (
                                
                                        AssetID text NOT NULL,
                                        AssetName text NOT NULL ,
                                        AssetCategory text NOT NULL ,
                                        AssetSubCat text NOT NULL ,
                                        AssetType text NOT NULL ,
                                        Generalization text NOT NULL ,
                                        Quantity text NOT NULL ,
                                        GeoFence text NOT NULL ,
                                        UploadTimeline text NOT NULL ,
                                        Variations text NOT NULL ,
                                        AssetBioInfo text NOT NULL ,
                                        ProfilePath text NOT NULL

                                    );"""



    SHADOW_ORDERLOGS_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS Submissions (
            
                                        OrderID text NOT NULL,
                                        Benefactor text NOT NULL ,
                                        OrderItem text NOT NULL,
                                        OrderTimeline text  NOT NULL,
                                        OrderAmount text NOT NULL,
                                        OrderStatus text NOT NULL,
                                        DeliveryTimeline text NOT NULL,
                                        ItemInfo text NOT NULL,
                                        Variations text NOT NULL ,
                                        OrderWaitTime text NOT NULL ,
                                        ItemGraphics text NOT NULL

                                    );"""




    SHADOW_ACCOUNTS_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS Accounts (
                                        AccountID text NOT NULL  PRIMARY KEY,
                                        Benefactor text NOT NULL,
                                        AccountType text NOT NULL ,
                                        LastStandingAmount text  NOT NULL , 
                                        StandingTimeline text  NOT NULL , 
                                        AccountName text  NOT NULL , 
                                        AccountKey text  NOT NULL , 
                                        SubAccounts text  NOT NULL ,
                                        AccountStatus text  NOT NULL 
                                    
                                    );"""


    SHADOW_TRANSACTIONS_CONSTRUCTOR = """CREATE TABLE IF NOT EXISTS Transactions (
                                        TransactionID text NOT NULL  PRIMARY KEY,
                                        Benefactor text NOT NULL,
                                        TransactionType text NOT NULL ,
                                        TransactionAsset text  NOT NULL , 
                                        TransactionFee text  NOT NULL , 
                                        Timeline text  NOT NULL , 
                                        TransactionStatus text  NOT NULL , 
                                        InvoicePath text  NOT NULL 
                                       
                                    
                                    
                                    );"""






    #create a database connection
    conn = create_connection(Qualified_Memmory)
    #create tables
    if conn is not None:
        # create projects table
        create_table(conn, SHADOW_USERPROFILE_CONSTRUCTOR)

        # create tasks table
        create_table(conn,  SHADOW_ASSETSTORE_CONSTRUCTOR)

        # create tasks table
        create_table(conn, SHADOW_ORDERLOGS_CONSTRUCTOR)

        # create tasks table
        create_table(conn,  SHADOW_TRANSACTIONS_CONSTRUCTOR  )

        # create tasks table
        create_table(conn,  SHADOW_ACCOUNTS_CONSTRUCTOR  )



        
    else:
        print("Error! cannot create the database connection.")

Sphinkx_Override("./static/Databases/ShadowMemmory.db")