"""Name: Shivank Srivastava
   Title: Convert numeric scores to grades
   CWID: 20006832
"""

import sys
"""
This import sys is used for sys.exit()
"""

while True:   
    """
        To convert user input to float.
        Print an error message and loop again if the user inputs an invalid input value.
    """    
    try:
        score = float(input("Enter your score: ")) 
        if score in range (0,100):
            if score > 92:
                print("You have scored an A grade")
            elif score >= 90 and score <= 92:
                print("You have scored an A- grade")
            elif score >= 87 and score <= 89: 
                print("You have scored an B+ grade")
            elif score >= 83 and score <= 86: 
                print("You have scored an B grade")
            elif score >= 80 and score <= 82:
                print("You have scored an B- grade")
            elif score >= 70 and score <= 79: 
                print("You have scored an C grade")
            elif score < 70: 
                print("You have scored an F grade") 
        else:
            print("Out of range! Try Again")  
    except ValueError as e:
        print("Enter number between 0 and 100 ", e)
    finally:
        sys.exit()
        