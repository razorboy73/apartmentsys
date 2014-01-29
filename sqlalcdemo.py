from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

engine = create_engine('sqlite:///apartments.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

session = Session()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    userName = Column(String)
    password = Column(String)
    salt = Column(String)
    confirmPassword = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    companyName = Column(String)
    email = Column(String)
    phoneNumber = Column(String)
    faxNumber = Column(String)
    addressLine1 = Column(String)
    addressLine2 = Column(String)
    addressLine3 = Column(String)
    suiteNumber = Column(String)
    zipCode = Column(String)
    province = Column(String)
    country = Column(String)
    regDate = Column(String)
    userDirectory = Column(String)

    def __init__(self, userName, salt,password,confirmPassword, firstName,lastName, companyName, email,phoneNumber,
                 faxNumber, addressLine1, addressLine2, addressLine3, suiteNumber,zipCode,province,country,regDate,userDirectory):
        self.userName = userName
        self.salt = salt
        self.password = password
        self.confirmPassword = confirmPassword
        self.firstName = firstName
        self.lastName = lastName
        self.companyName = companyName
        self.email = email
        self.phoneNumber = phoneNumber
        self.faxNumber = faxNumber
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.addressLine3 = addressLine3
        self.suiteNumber = suiteNumber
        self.zipCode = zipCode
        self.province = province
        self.country = country
        self.regDate = regDate
        self.userDirectory = userDirectory

    def __repr__(self):
        return "<Users('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
        '%s', '%s', '%s', )>"% (self.userName, self.salt, self.password, self.confirmPassword, \
        self.firstName, self.lastName, self.companyName, self.email, self.phoneNumber, self.faxNumber, self.addressLine1, self.addressLine2, self.addressLine3, self.suiteNumber, self.zipCode, self.province, self.country, self.regDate, self.userDirectory)



Base.metadata.create_all(engine)



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

    user = Users( userName,password, salt, confirmPassword,firstName, lastName, companyName, email, phoneNumber, \
                  faxNumber, addressLine1, addressLine2, addressLine3, suiteNumber, zipCode, province, country, regDate, userDirectory)

