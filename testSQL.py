import mysql.connector
def selectmySQL():
    mycursor.execute("USE MOGRENT") #telling it which database to use
    mycursor.execute("SELECT * FROM test")
    print(mycursor.fetchall())
def insertmySQL():
    mycursor.execute(""" INSERT INTO test VALUES 
                          (78)""")
    conn.commit()

    
conn = mysql.connector.connect(user = 'root', password = '#ALC2016', host = 'localhost')
mycursor = conn.cursor()
selectmySQL()
insertmySQL()
selectmySQL()
