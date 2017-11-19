import sqlCommand
import mysql.connector
def mainMenu():
    
    print("1. Input a new Docor\n")
    print("2. Input a new Patient\n")
    print("3. Input a new Prescription\n")
    print("4. Lookup Hospital\n")
    print("5. Lookup Patient\n")
    print("6. Loop up Prescription\n")
    print("7. Look up Doctor\n")
    print("8. Display all data\n")
    print("9. Exit\n")
    choice = int(input("Please enter a choice: "))
    return choice

def main():
    temp = mainMenu()
    if temp == 1:
        inputDoctor()
    if temp == 2:
        inputPatient()
    if temp == 3:
        inputPrescription()
    if temp == 4:
        lookupHospital()
    if temp == 5:
        lookupPatient()
    if temp == 6:
        lookupPrescription()
    if temp == 7:
        lookupDoctor()
    if temp == 8:
        displayAll()
    if temp == 9:
        close()
    
def inputDoctor():
    print("-----------------------------------------------------")
    main()
def inputPatient():
    print("-----------------------------------------------------")
    main()
def inputPrescription():
    print("-----------------------------------------------------")
    main()
    
def lookupHospital():
    zipCode = input("Enter the zip code of the hospital to search by: ")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("SELECT * FROM hospital WHERE zipcode = (%s)" %(zipCode))
    print(mycursor.fetchall())
    print("-----------------------------------------------------")
    main()
def lookupPatient():
    doB = int(input("Enter the patients date of birth to search by: "))
    mycursor.execute("USE MOGRENT")
    mycursor.execute("SELECT * FROM patient WHERE DOB = (%s)" %(doB))
    print(mycursor.fetchall())
    print("-----------------------------------------------------")
    main()
def lookupPrescription():
    presID = input("Enter the prescription ID to search by: ")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("SELECT * FROM prescription WHERE presID = (%s)" %(presID))
    print(mycursor.fetchall())
    print("-----------------------------------------------------")
    main()
def lookupDoctor():
    fname = input("Enter a first name to search by: ")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("SELECT * FROM doctor WHERE fName = ('%s')" %(fname))
    print(mycursor.fetchall())
    print("-----------------------------------------------------")
    main()
def displayAll():
    print("All the data will be displayed")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("SELECT * FROM hospital, doctor, patient, prescription")
    print(mycursor.fetchall())
    print("-----------------------------------------------------")
    main()
def close():
    exit()


conn = mysql.connector.connect(user = 'root',
                           password = '#ALC2016',
                           host = 'localhost')
mycursor = conn.cursor()

main()
