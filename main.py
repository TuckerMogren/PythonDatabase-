import functionsSQL as SQL


try:
    SQL.clearSc()
except:
    print("ERROR: when clearing the screen")

try:
    SQL.main()
except:
    print("ERROR: when executing main function") 

try:
    conn.close()
except:
    print("ERRPR: When closing the connection")
