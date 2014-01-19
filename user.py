import sqlite3
import datetime
import random
import hashlib
from login import userSignIn
import hmac


path = "/Users/workhorse/thinkful/"
db = "apartment.db"
SECRET = "imsosecret"

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
            salt Text NOT NULL,
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

"""
def userSignIn():

    userName = raw_input("Enter your user name: ")
    password = raw_input("Enter a password: ")
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute ("SELECT firstName, lastName, password, salt from People WHERE userName='{}'".format(userName))
        for row in c.fetchall():
            print row[0]
            print row[1]
            print row[2]
            print row[3]
            x = hashlib.sha256(password+row[3]).hexdigest()
            print x
            if x  == row[2]:
                print "Authentic"
            else:
                print "reject"
"""

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
    addressLine1 = raw_input("Enter your address: ")
    addressLine2 = raw_input("Enter second line of your address (Not Required): ")
    addressLine3 = raw_input("Enter third line of your address (Not Required): ")
    zipCode = raw_input("Enter your zip code: ")
    province = raw_input("Enter your state or province: ")
    country = raw_input("Enter your country: ")
    regDate = datetime.date.today()
    print regDate


    params = ( userName, password, salt, confirmPassword, firstName, lastName,
          companyName, email, phoneNumber, addressLine1, addressLine2,
          addressLine3, zipCode, province, country, regDate)



    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("INSERT INTO People VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)


#checkAndCreateDB()

userSignUp()
userSignIn()




