import sqlite3
import os
#from emailScript import emailScript
from emailexper import mailReports
import datetime
import sys

i = datetime.datetime.now()

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
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute ("SELECT p_ID, userName, userDirectory  from people WHERE p_ID='{}'".format(owner))
        for row in c.fetchall():
            print "p_ID: ", row[0], "userName: ", row[1],"userDirectory: ", row[2]

    fullPath = os.path.join(path, row[2])
    print "Full Path based on file structure and userDirector", fullPath

    if choice =="1":
        currentMonthYear = i.strftime('%B%Y')
        print currentMonthYear
        newDir = os.path.join(fullPath, currentMonthYear)
        print "New Directory to be Created based on path and date: ", newDir
        if os.path.isdir(newDir):
            print newDir, "Exists"
        else:
            print "making new Dir"
            os.mkdir( newDir, 0755 )

        fileBase = str(newDir)+"/"+str(currentMonthYear)+"buildings.txt"
        print "Filename: ", fileBase


        #pull out directory related to the user - create path - done
        #every month, create new folder - MonthYear
        #check if a folder exists for that month
        #make a unique file name - ReportName+Month+Year
        myOutputFile = open(fileBase, "w")
        with sqlite3.connect(db) as connection:
            c = connection.cursor()
            c.execute ("SELECT b_ID, owner, numOfUnits, buildingName, streetNumber, streetName, streetType, direction, \
              municipality, province, postalCode, managerFirstName, managerLastName from building WHERE owner='{}'".format(owner))
            for row in c.fetchall():
                print row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]
                linesToWrite ="{},{},{},{},{},{},{},{},{},{},{},{},{}" .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12])
                myOutputFile.writelines(linesToWrite)
            myOutputFile.close()
            mailReports(newDir)
            print "email report sent"


    if choice =="2":
        pass