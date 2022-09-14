"""Name: Shivank Srivastava
   Title: User defined functions
   CWID: 20006832
"""
import sys


def maxOfThree(a, b, c):
    if(a>=b and a>=c):
        largest = a
    elif(b>=a and b>=c):
        largest = b
    else:
        largest = c
    return largest

"""
maxOfThree() is a user defined function to find the largest of three.
"""

#def main():

try:
    a = int(input("Enter the 1st number: "))
except ValueError:
    print("Error, enter a number")
    sys.exit()

try:
    b = int(input("Enter the 2nd number: "))
except ValueError:
    print("Error, enter a number")
    sys.exit()

try:
    c = int(input("Enter the 3rd number: "))        
except ValueError:
    print("Error, enter a number")
    sys.exit()

print("The largest number is: " ,maxOfThree(a,b,c))

#main()