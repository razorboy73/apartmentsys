import hashlib
import sqlite3
from reporting import reportModule


path = "/Users/workhorse/thinkful/"
db = "apartment.db"
SECRET = "imsosecret"

def userSignIn():

    userName = raw_input("Enter your user name: ")
    password = raw_input("Enter a password: ")
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute ("SELECT p_ID, firstName, lastName, password, salt from People WHERE userName='{}'".format(userName))
        for row in c.fetchall():
            print row[0]
            print row[1]
            print row[2]
            print row[3]
            #p_ID, firstName, lastName, password, salt = row
            x = hashlib.sha256(password+row[4]).hexdigest()
            print x
            if x  == password:
                userActions(row[3])
            else:
                print "reject"

def registerBuilding(owner):
    print "The following information will be used to complete legal forms and notices"
    owner = owner
    numOfUnits = int(raw_input("Number of units: "))
    buildingName =raw_input("Legal Name of Corporation holding building - to be used on forms: ")
    streetNumber =raw_input("Street Number for the Building: ")
    streetName  =raw_input("Street Name - do not include Type (St/Ave/Dr) or direction: ")
    streetType =raw_input("Street Type (e.g. Street, Avenue, Road): ")
    direction =raw_input("Direction of Street: ")
    municipality =raw_input("City/Municpality: ")
    province =raw_input("Province/State - 2 Letter Abbreviations: ")
    postalCode =raw_input("Zip or Postal Code: ")
    managerFirstName =raw_input("Building Manager First Name- This individual's  names will appear on forms: ")
    managerLastName =raw_input("Building Manager Last Name- This individual's names will appear on forms: ")



    params = (owner, numOfUnits, buildingName, streetNumber, streetName, streetType, direction, municipality, province, postalCode,
               managerFirstName, managerLastName)

    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("INSERT INTO building VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?)", params)

    #add a tenant to this building
    userActions(owner)



def registerTenant(owner):
    print "You are signing up new tenant. which building"
    print "You are owner number:", owner
    print "you manage the following buildings"
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute ("SELECT b_ID, buildingName, owner, numOfUnits from building WHERE owner='{}'".format(owner))
        for row in c.fetchall():
            print row[0], row[1], row[2], row[3]


    buildingName  = raw_input("Enter a building number: ")
    owner = owner
    unitNum = raw_input("Enter the unit number: ")
    #check for duplications
    rent = raw_input("Enter Monthly Rent - do not include dollar sign: ")
    fname = raw_input("tenant first name: ")
    lname = raw_input("tenant last name: ")

    params = ( buildingName, owner, unitNum, rent, fname, lname)



    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("INSERT INTO units VALUES (NULL, ?, ?,?,?,?,?)", params)

    userActions(owner)

def modifyingTenant(owner):
    print "You are modifying an existing tenant. which building"
    print "You are owner number:", owner
    print "you manage the following buildings"
    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute ("SELECT b_ID, buildingName, owner, numOfUnits from building WHERE owner='{}'".format(owner))
        for row in c.fetchall():
            print row[0], row[1], row[2], row[3]


    buildingName  = raw_input("Enter a building number: ")
    owner = owner
    unitNum = raw_input("Enter the unit number: ")
    #check for duplications
    rent = raw_input("Enter Monthly Rent - do not include dollar sign: ")
    fname = raw_input("tenant first name: ")
    lname = raw_input("tenant last name: ")

    params = ( buildingName, owner, unitNum, rent, fname, lname)



    with sqlite3.connect(db) as connection:
        c = connection.cursor()
        c.execute("INSERT INTO units VALUES (NULL, ?, ?,?,?,?,?)", params)

    userActions(owner)


def userActions(owner):
    choice = raw_input( """Authenticated
    What do you want to do now?
    Enter the number of your choice:
    1. Register a new building
    2. add a tenant
    3. Modify a tenant
    4. collect rent
    5. Modify global settings
    6. Manually generate reports
    """)
    if choice=="1":
        print "new building"
        registerBuilding(owner)
    if choice=="2":
        print "new tenant"
        registerTenant(owner)
    if choice=="3":
        print" Modify a Tenant"
        pass
    if choice=="4":
        print "Collect Rent"
        pass
    if choice=="5":
        print "Modify Global Setting"
        pass
    if choice=="6":
        print "Transferring to Reporting module"
        reportModule(owner)