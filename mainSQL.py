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
##    if temp == 1:
##        inputDoctor()
##    if temp == 2:
##        inputPatient()
##    if temp == 3:
##        inputPrescription()
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
        exit()
    
##def inputDoctor():
##    ##SQL CODE
##    
##def inputPatient():
##    ##SQL CODE
##    
##def inputPrescription():
##    ##SQL CODE
##def lookupHospital():
##    ##SQL CODE
def lookupPatient():
    doB = int(input("Enter the patients date of birth to search by: "))
    ##SQL CODE
def lookupPrescription():
    presID = int(input("Enter the prescription ID to search by: "))
    ##SQL CODE
def lookupDoctor():
    fname = str(input("Enter a first name to search by: "))
    ##SQL CODE
def displayAll():
    print("All the data will be displayed")
    db = 'test'
    sqlCommand.selectmySQL(mycursor,db)
    
    ##SQL CODE
def exit():
    quit()


    
conn = mysql.connector.connect(user = 'root',
                           password = '#ALC2016',
                           host = 'localhost')
mycursor = conn.cursor()
main()
