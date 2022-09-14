"""
Name: Shivank Srivastava
CWID: 20006832
Date: 1st Nov 2021
"""


import os
import time
import sys

    

fileName = input("Enter the file name: ")

try:
    fHandle = open(fileName, 'r')
except IOError:
    print("Error: can\'t find file or read data")
    sys.exit()
if os.stat(fileName).st_size != 0:  
    uniqueEmail = 0
    items = set()
    for line in fHandle:
        if line.startswith("From:"):
            email = line.split(":")[1].split()
            if email[0].find("@"):
                items.add(email[0])
                print(email)
    uniqueEmail = len(items)
    if uniqueEmail > 0:
        print("Number of unique addresses in " + fileName + " is ", uniqueEmail)
    else:
        print("File does not contain any sender's email address.")
else:
    print("Oops!!!This file is empty")



try:
    fHandle = open(fileName,'r')
except IOError:
    print("Error: can\'t find file or read data")
    sys.exit()

if os.stat(fileName).st_size != 0: 
   
    senders = dict()
    for line in fHandle:
        if line.startswith("From:"):
            email = line.split(":")[1].split()
            if email[0].find("@"):
                senders[email[0]] = senders.get(email[0],0)+1
    highCount = 0
    moreEmail = 0
    for email,count in senders.items():
        if highCount == 0 or highCount < count:
            moreEmail = email
            highCount = count
    if moreEmail != 0 and highCount > 0:
        print("Most mails are sent by",moreEmail)
        print("Number of mails sent is",highCount)
    else:
        print("File does not contain any sender's email address.")
else:
    print("Oops!!!This file is empty")

