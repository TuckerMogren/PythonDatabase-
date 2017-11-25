import mysql.connector
import os
def mainMenu():
    print("1. Input a new Docor\n")
    print("2. Input a new Prescription\n")
    print("3. Input a new Patient\n")
    print("4. Lookup Hospital\n")
    print("5. Lookup Patient\n")
    print("6. Loop up Prescription\n")
    print("7. Look up Doctor\n")
    print("8. Display all data\n")
    print("9. Exit\n")
    choice = 0
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6 and choice != 7 and choice != 8 and choice != 9:
        choice = int(input("Please enter a choice: "))
    return choice

def main():
    temp = mainMenu()
    if temp == 1:
        inputDoctor()
    if temp == 2:
        inputPrescription()
    if temp == 3:
        inputPatient()
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
    mycursor.execute("INSERT INTO doctor VALUES(%s,'%s','%s','%s',%s) " %(docID, fName, lName, docPhone, hosID))
    conn.commit()
    print("-----------------------------------------------------")
    main()
def inputPatient():
    patientID = input("Please input the patient's ID: ")
    fName = input("Please input the patient's first name: ")
    lName = input("Please input the patient's last name: ")
    DOB = input("Please input the patient's DOB: ")
    cellPhone = input("Please input the patient's cell number: ")
    homePhone = input("Please input the patient's home number: ")
    presID = input("Please input the patient's associated prescription ID: ")
    mycursor.execute("INSERT INTO patient VALUES(%s,'%s','%s','%s','%s','%s', %s) " %(patientID, fName, lName, DOB, cellPhone, homePhone, presID))
    conn.commit()
    print("-----------------------------------------------------")
    main()
def inputPrescription():
    presID = input("Please input the prescription's ID: ")
    presName = input("Please input the prescription's name: ")
    presDate = input("Please input the prescription's date: ")
    dosageMG = input("PlMogrease input the prescription's dosage in MG: ")
    docID = input("Please input the prescriptions assiocated doctor's ID: ")
    mycursor.execute("INSERT INTO prescription VALUES(%s,'%s','%s','%s',%s) " %(presID, presName, presDate, dosageMG, docID))
    conn.commit()
    print("-----------------------------------------------------")
    main()
    
def lookupHospital():
    zipCode = input("Enter the zip code of the hospital to search by: ")
    mycursor.execute("SELECT * FROM hospital WHERE zipcode = (%s)" %(zipCode))
    for(hospitalID, hName, street, city, state, zipCode) in mycursor:
        print("Hospital ID: {}\nHospital Name: {}\nStreet: {}\nCity: {}\nState: {}\nZip Code: {}".format(hospitalID, hName, street, city, state, zipCode))
    print("-----------------------------------------------------")
    main()
def lookupPatient():
    doB = int(input("Enter the patients date of birth to search by: "))
    mycursor.execute("SELECT * FROM patient WHERE DOB = (%s)" %(doB))
    for(patientID, fName, lName, DOB, cellPhone, homePhone, presID) in mycursor:
        print("Patient ID: {}\nPatient First Name: {}\nPatient Last Name: {}\nPatient DOB: {}\nPatient Cell Phone: {}\nPatient Home Phone: {}\nPatient's Prescription ID: {}".format(patientID, fName, lName, DOB, cellPhone, homePhone, presID))
    print("-----------------------------------------------------")
    main()
def lookupPrescription():
    presID = input("Enter the prescription ID to search by: ")
    mycursor.execute("SELECT * FROM prescription WHERE presID = (%s)" %(presID))
    for(presID, presName, presDate, dosageMG, docID) in mycursor:
        print("Prescription ID: {}\nPrescription Name: {}\nPrescribed Date: {}\nDosage: {}Mg\nPrescribing Doctor ID: {}".format(presID, presName, presDate, dosageMG, docID))
    print("-----------------------------------------------------")
    main()
def lookupDoctor():
    fname = input("Enter a first name to search by: ")
    mycursor.execute("SELECT * FROM doctor WHERE fName = ('%s')" %(fname))
    for(docID, fName, lName, docPhone, hosID) in mycursor:
        print("Doctor ID: {}\nDoctor First Name: {}\nDoctor Last Name: {}\nDoctor Phone Number: {}\nDoctor's Assiocated Hospital ID: {}".format(docID, fName, lName, docPhone, hosID))
    print("-----------------------------------------------------")
    main()
def displayAll():
    print("All the data will be displayed\n")
    mycursor.execute("""SELECT patient.fName, patient.lName, patient.patientID, prescription.presName, prescription.dosageMG, prescription.presID, doctor.fname, doctor.lname, doctor.docID, hospital.hName, hospital.hospitalID
                        FROM hospital, doctor, patient, prescription
                        WHERE hospital.hospitalID = doctor.hosID
                        AND doctor.docID = prescription.docID
                        AND prescription.presID = patient.presID;""")
    for(fName, lName, patientID, presName, dosageMG, presID, fname, lname, docID, hName, hospitalID) in mycursor:
        print("""Patient First Name: {}\nPatient Last Name: {}\nPatient ID: {}
                \nPrescription Name: {}\nPerscription Dosage: {}MG's\nPrescription ID: {}
                \nDoctor First Name: {}\nDoctor Last Name: {}\nDoctor ID: {}
                \nHospital Name: {}\nHospital ID: {}\n""".format(fName, lName, patientID, presName, dosageMG, presID, fname, lname, docID, hName, hospitalID)
              )
        print("-------------------------NEXT RESULT----------------------------")

    print("------------------------------MAIN MENU-----------------------------")
    main()
def close():
    exit()
    
def askPass():
    
    dbPass = str(input("Please enter the database password: "))
    return dbPass

def clearSc():
    clear = "\n" * 40
    print(clear)
dbPass = askPass()
dbFig = {'user': 'mogrent',
        'password': dbPass,
         'host': 'cs350tucker.czmjbuzc8xmb.us-east-2.rds.amazonaws.com',
         'database': 'Medical',
         'raise_on_warnings': True,
         'use_pure': False,
}
try:
    conn = mysql.connector.connect(**dbFig)
except:
    print("Incorrect Password")
    close()


try:
    mycursor = conn.cursor()
except:
    print("Database Error")


