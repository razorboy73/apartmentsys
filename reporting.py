import sqlite3
import os
from emailScript import emailScript

#http://docs.python.org/2/library/email-examples.html

#need to come up with unique file names
#need to create file structure for each users




path = "/Users/workhorse/thinkful/apartments"
db = "apartment.db"
SECRET = "imsosecret"

def reportModule(owner):
    choice = raw_input("""
    1 - list all my buildings
    2 - list all my tenants
    """)

    if choice =="1":
        #pull out directory related to the user
        #every month, create new folder - 
        #make a unique file name
        myOutputFile = open("buildings.txt", "w")
        with sqlite3.connect(db) as connection:
            c = connection.cursor()
            c.execute ("SELECT b_ID, owner, numOfUnits, buildingName, streetNumber, streetName, streetType, direction, \
              municipality, province, postalCode, managerFirstName, managerLastName from building WHERE owner='{}'".format(owner))
            for row in c.fetchall():
                print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]
                linesToWrite ="{},{},{},{},{},{},{},{},{},{},{},{},{}" .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
                myOutputFile.writelines(linesToWrite)
            myOutputFile.close()
            emailScript(linesToWrite)
            print "email report sent"


    if choice =="2":
        pass