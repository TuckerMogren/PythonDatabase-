import mysql.connector
def selectmySQL(mycursor,db):
    mycursor.execute("USE MOGRENT") #telling it which database to use
    mycursor.execute("SELECT * FROM (%s)"  %(db))
    print(mycursor.fetchall())
def insertmySQL():
    mycursor.execute(""" INSERT INTO test VALUES 
                          (78)""")
    conn.commit()
