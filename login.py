import hashlib
import sqlite3

path = "/Users/workhorse/thinkful/"
db = "apartment.db"
SECRET = "imsosecret"

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