import sqlite3
from sqlite3 import Error
from flask import *

app=Flask(__name__)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

    conn = create_connection("./ShadowMemmory.db")
def Create_UserProfile(conn , MouthWash):
    """
    Create a new UserProfile into the UserProfiles table
    :param conn:
    :param UserProfile:
    :return: UserProfile id
    """

    conn = create_connection("./static/Databases/ShadowMemmory.db")

    sql = ''' INSERT INTO UserClassProfiles(UserToken ,FullName , EmailAddress  , PrimaryPhone  , SecondaryPhone , Gender , UserID , SecureID , Country , State , ProfilePath )
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    with app.app_context():
        cur = conn.cursor()
        cur.execute(sql, MouthWash)
        conn.commit()
        conn.close
    return "Success"
   



def Update_UserClassProfiles(conn, MouthWash):
    """
    update priority, begin_date, and end date of a UserClassProfiless
    :param conn:
    :param UserClassProfiless:
    :return: project id
    """
    conn = create_connection("./static/Databases/ShadowMemmory.db")
    sql = ''' UPDATE UserClassProfiles
              SET UserToken = ? ,
                  FullName = ? ,
                  EmailAddress  = ? , 
                  PrimaryPhone  = ?,
                  SecondaryPhone   = ?,
                  Gender   = ? ,
                  UserID  = ? , 
                  SecureID = ? , 
                  Country = ? , 
                  State = ? ,
                  ProfilePath  = ? ,  
              WHERE UserID = ?'''


    cur = conn.cursor()
    cur.execute(sql, MouthWash)
    conn.commit()
    


def Retreive_User_Profiles(conn):
    """
    Query all Credential in the UserClassProfilesss table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("./static/Databases/ShadowMemmory.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM UserClassProfiles ")

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential


def Retreive_User_ID(conn):
    """
    Query UserClassProfiless by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM UserClassProfiles" )

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)
    return Credential 


def Query_User_Existence(conn, UserID):
    """
    Query UserClassProfilesss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/ShadowMemmory.db")
    cur = conn.cursor()
    cur.execute("SELECT UserID FROM UserClassProfiles WHERE UserID=?", (UserID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;

def Query_CryptoHash_Existence(conn, SecureID):
    """
    Query UserClassProfilesss by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    conn = create_connection("./static/Databases/ShadowMemmory.db")
    cur = conn.cursor()
    cur.execute("SELECT SecureID FROM UserClassProfiles WHERE SecureID=?", (SecureID,))

    Credential = cur.fetchall()

    for DataChunk in Credential:
        print(DataChunk)

        return Credential;






def Remove_User_Profile(conn, UserID):
    """
    Delete a UserClassProfiless by UserClassProfiless id
    :param conn:  Connection to the SQLite database
    :param id: id of the UserClassProfiless
    :return:
    """
    sql = 'DELETE FROM UserClassProfiles WHERE UserID = ?'
    cur = conn.cursor()
    cur.execute(sql, ( UserID ,))
    conn.commit()




conn = create_connection("./static/Databases/ShadowMemmory.db")

#Retreive_AllUser_Profiles(conn)


#Alpha =( "435435-XDK-9S90" , "Clyde Javis" , "Ahoya", "Test" ,"Test", "Test", "Test" , "Test" , "Test", "Test",  "Test")
#Create_UserProfile(conn , Alpha )

#Remove_User_Profile(conn , "435435-XDK-9S90")

