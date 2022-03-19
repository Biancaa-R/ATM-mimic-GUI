#-----------------------------------------------
#Connecting to server and creating new database
#-----------------------------------------------

import pymysql

def exec(dbuser, dbpass):
    #Connecting to server
    mydb = pymysql.connect(
                host = "localhost",
                user = "root",            
                password = "biancaa",
            )

    cursor = mydb.cursor()
    
    #Creating database
    cursor.execute("CREATE DATABASE IF NOT EXISTS ATM")
    cursor.execute("USE ATM")

    #Creating login table
    cursor.execute("""CREATE TABLE IF NOT EXISTS EATM
    (name VARCHAR(50),
    dob VARCHAR(10),
    acc_num varchar(4) PRIMARY KEY,
    acc_pin varchar(3),
    contact_num varchar(10),
    email_id varchar(50),
    balance bigint)""")
    mydb.commit()

    
