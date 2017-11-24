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
    docID = input("Please input the doctor's ID: ")
    fName = input("Please input the doctor's first name: ")
    lName = input("Please input the doctor's last name: ")
    docPhone = input("Please input the doctor's phone number: ")
    hosID = input("Please input the doctor's associated hospital ID: ")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("INSERT INTO doctor VALUES(%s,'%s','%s','%s',%s) " %(docID, fName, lName, docPhone, hosID))
    conn.commit()
    print("-----------------------------------------------------")
    main()
def inputPatient():
    patientID = input("Please input the patient's ID: ")
    fName = input("Please input the patient's first name: ")
    lName = input("Please input the patient's last name: ")
    cellPhone = input("Please input the patient's cell number: ")
    homePhone = input("Please input the patient's home number: ")
    DOB = input("Please input the patient's DOB: ")
    presID = input("Please input the patient's associated prescription ID: ")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("INSERT INTO patient VALUES(%s,'%s','%s','%s','%s','%s', %s) " %(patientID, fName, lName, cellPhone, homePhone, DOB, presID))
    conn.commit()
    print("-----------------------------------------------------")
    main()
def inputPrescription():
    presID = input("Please input the prescription's ID: ")
    presName = input("Please input the prescription's name: ")
    presDate = input("Please input the prescription's date: ")
    dosageMG = input("Please input the prescription's dosage in MG: ")
    docID = input("Please input the prescriptions assiocated doctor's ID: ")
    mycursor.execute("USE MOGRENT")
    mycursor.execute("INSERT INTO prescription VALUES(%s,'%s','%s','%s',%s) " %(presID, presName, presDate, dosageMG, docID))
    conn.commit()
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
    mycursor.execute("SELECT * FROM hospital")
    print(mycursor.fetchall())
    print("-----------------------------------------------------")
    main()
def close():
    exit()
#ALC2016
    
def askPass():
    dbPass = str(input("Please enter the database password: "))
    return dbPass



dbPass = askPass()

dbFig = {'user': 'mogrent',
        'password': dbPass,
         'host': 'cs350tucker.czmjbuzc8xmb.us-east-2.rds.amazonaws.com',
         'database': 'Medical',
         'raise_on_warnings': True,
         'use_pure': False,
}
conn = mysql.connector.connect(**dbFig)
mycursor = conn.cursor()
main()
conn.close()

