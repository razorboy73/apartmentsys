import sqlite3
import datetime


path = "/Users/workhorse/thinkful/"
db = "apartment.db"

def checkAndCreateDB():
    #not checking for some reason
    #fullPath = os.path.join(path, db)
    #if os.path.exists(fullPath):
    #   print "Database Exists"
    #else:
    connection = sqlite3.connect(db)
    print "Creating database"
    createUserRegTable()

def createUserRegTable():
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE People
            (p_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            userName TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            confirmPassword TEXT NOT NULL,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            companyName TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phoneNumber TEXT NOT NULL,
            addressLine1 TEXT NOT NULL,
            addressLine2 TEXT,
            addressLine3 TEXT,
            zipCode TEXT NOT NULL,
            province TEXT NOT NULL,
            country TEXT NOT NULL,
            regDate DATE NOT NULL)
            """)
        print "table made"


def userSignIn():
    pass

def userSignUp():
    userName = raw_input("Enter a user name: ")
    password = raw_input("Enter a password: ")
    confirmPassword = raw_input("Confirm Your Password: ")
    firstName = raw_input("Enter your first name: ")
    lastName = raw_input("Enter your last name: ")
    companyName = raw_input("Enter your company name: ")
    email = raw_input("Enter your email: ")
    phoneNumber = raw_input("Enter your phone number: ")
    addressLine1 = raw_input("Enter your address: ")
    addressLine2 = raw_input("Enter second line of your address (Not Required): ")
    addressLine3 = raw_input("Enter third line of your address (Not Required): ")
    zipCode = raw_input("Enter your zip code: ")
    province = raw_input("Enter your state or province: ")
    country = raw_input("Enter your country: ")
    regDate = datetime.date.today()
    print regDate

    #userInfo = (userName, password, confirmPassword, firstName,lastName, companyName, email, phoneNumber,addressLine1,
    #addressLine2, addressLine3, zipCode, province, country, regDate)

    params = (userName, password, confirmPassword, firstName, lastName,
          companyName, email, phoneNumber, addressLine1, addressLine2,
          addressLine3, zipCode, province, country, regDate)



    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("INSERT INTO People VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)

checkAndCreateDB()

userSignUp()



