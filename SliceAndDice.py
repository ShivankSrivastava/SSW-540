"""
Name: Shivank Srivastava
Cwid: 20006832
Date: 17 Oct 2021
"""


import os
import time
import sys

def main():
    
    print("Program to find the Average Spam Confidence Value")
    file_name = input("Enter the file name: ")
    try:
        fileHandle = open(file_name, 'r')
    except IOError:
        print("Error: can't find file or read data")
        sys.exit()
    if os.stat(file_name).st_size != 0:  
        numberOfLines = 0.0
        sumOfConfidence = 0.0
        for line in fileHandle:
            if line.startswith("X-DSPAM-Confidence:"):
                str = line[line.find(":") + 1:].lstrip()
                confidenceValue = str[:str.find(' ')].strip()
                try:
                    confidenceValue = float(confidenceValue)
                    numberOfLines += 1
                    sumOfConfidence += confidenceValue
                except ValueError:
                    print("Not a valid value:", confidenceValue)

        try:
            average = sumOfConfidence / numberOfLines
        except ZeroDivisionError:
            print("No rows found with X-DSPAM-Confidence")
            sys.exit()
        print("Average spam confidence: %.4f " % average)
        fileHandle.close()
    else:
        print("This file is empty")


main()