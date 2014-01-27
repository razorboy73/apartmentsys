import sqlite3
import datetime
import random
import hashlib
from login import userSignIn
import os
import sys


path = "/Users/workhorse/thinkful/apartments"
db = "apartment.db"
SECRET = "imsosecret"

def checkAndCreateDB():
    if not os.path.exists(os.path.join(path, db)):
    #not checking for some reason
    #fullPath = os.path.join(path, db)
    #if os.path.exists(fullPath):
    #   print "Database Exists"
    #else:
        connection = sqlite3.connect(db)
        createUserRegTable()
        print "Creating Admin User Table"
        createBuildingRegTable()
        print "Created Building Table"
        registerTenantPerBuilding()
        print "Created Tenant Table"
    else:
        print "exists"


def createUserRegTable():
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE People
            (p_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            userName TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            salt Text NOT NULL,
            confirmPassword TEXT NOT NULL,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            companyName TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phoneNumber TEXT NOT NULL,
            faxNumber TEXT NOT NULL,
            addressLine1 TEXT NOT NULL,
            addressLine2 TEXT,
            addressLine3 TEXT,
            suitNumber TEXT,
            zipCode TEXT NOT NULL,
            province TEXT NOT NULL,
            country TEXT NOT NULL,
            regDate DATE NOT NULL,
            userDirectory TEXT NOT NULL )
            """)
        print "user table made"

def createBuildingRegTable():
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE building
            (b_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            owner INTEGER NOT NULL,
            numOfUnits INTEGER NOT NULL,
            buildingName TEXT NOT NULL UNIQUE,
            streetNumber TEXT NOT NULL,
            streetName  TEXT NOT NULL,
            streetType TEXT NOT NULL,
            direction TEXT NOT NULL,
            municipality TEXT NOT NULL,
            province TEXT NOT NULL,
            postalCode TEXT NOT NULL,
            managerFirstName TEXT NOT NULL,
            managerLastName TEXT NOT NULL,
            FOREIGN KEY(owner) REFERENCES people(p_ID))
            """)
        print "building table made"


def registerTenantPerBuilding():
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE units
            (u_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            buildingName TEXT NOT NULL UNIQUE,
            owner INTEGER NOT NULL,
            unitNum INTEGER NOT NULL,
            rent INTEGER NOT NULL,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            FOREIGN KEY(owner) REFERENCES people(p_ID),
            FOREIGN KEY(buildingName) REFERENCES building(b_ID)
            )
            """)
        print "Tenant table made"


def make_salt():
	salt_char =[]
	for x in range(15):
		z =random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
		salt_char.append(z)
	#print salt
	salt = ''.join(salt_char)
	return salt

current_salt =[]

def hash_str(pw):
	salt = make_salt()
	#print salt
	#salted.append(salt)
	#print name
	#print SECRET
	#return hashlib.md5(s).hexdigest()
	current_salt.append(salt)
	h = hashlib.sha256(pw+salt).hexdigest()
	return h, salt

def valid_pw(pw, salt, password):
    x = hashlib.sha256(pw+salt).hexdigest()
    y = password
    print "confirmed pw", x
    print "original pw", y
    if x == y:
        return True
    else:
        return False



def userSignUp():
    print "You are signing up as a new user"
    userName = raw_input("Enter a user name: ")
    password, salt = hash_str(raw_input("Enter a password: "))
    print password
    print "salt: ", salt
    confirmPassword = valid_pw(raw_input("Confirm Your Password: "), salt, password)
    print confirmPassword
    firstName = raw_input("Enter your first name: ")
    lastName = raw_input("Enter your last name: ")
    companyName = raw_input("Enter your company name: ")
    email = raw_input("Enter your email: ")
    phoneNumber = raw_input("Enter your phone number: ")
    faxNumber = raw_input("Enter your fax number: ")
    addressLine1 = raw_input("Enter your address: ")
    addressLine2 = raw_input("Enter second line of your address (Not Required): ")
    addressLine3 = raw_input("Enter third line of your address (Not Required): ")
    suiteNumber = raw_input("Enter your suite code: ")
    zipCode = raw_input("Enter your zip code: ")
    province = raw_input("Enter your state or province: ")
    country = raw_input("Enter your country: ")
    regDate = datetime.date.today()
    userDirectory = str(regDate)+str(userName)+str(salt)
    print regDate
    print userDirectory
    fullPath = os.path.join(path, userDirectory)
    print fullPath
    os.makedirs( fullPath, 0755 )

    params = ( userName,password, salt, confirmPassword,firstName, lastName, companyName, email, phoneNumber, faxNumber, addressLine1, addressLine2, addressLine3, suiteNumber, zipCode, province, country, regDate, userDirectory)



    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("INSERT INTO People VALUES (NULL, ?,?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)", params)


#checkAndCreateDB()

userSignUp()
#userSignIn()




