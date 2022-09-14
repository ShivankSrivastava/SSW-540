"""
Name: Shivank Srivastava
CWID: 20006832
Date: 3rd Oct 2021
Objective: The aim is to generate an random number which the user has to guess in 6 tries.
"""


import random


def game():

    print("Well, " + name + " , I am thinking of a number between 1 and 20. \n")
    random_number = random.randint(1, 20)
    i = 1
    while (i <= 6):
        try:
            guess_number = int(input("Take a guess: "))
        except Exception as e:
            print("Please enter the correct number ")
            continue  
        if range(guess_number) == 1:
            print("Please Enter the number which is in the range 1,20 \n")
            continue  
        result = guess_check(guess_number, random_number)
        if result == 0:
            print("Good job, " + name + "! You guessed my number in " + str(i) + " guesses!")
            break
        elif result == -1:
            print("Your guess is too low.\n")
        elif result == 1:
            print("Your guess is too high.\n")
        i = i + 1 
    if i > 6:
        print("You have not guessed the number correctly. The number I was thinking of was " + str(random_number))


def guess_check(guess_number, random_number):
    if guess_number == random_number:
        return 0
    elif guess_number < random_number:
        return -1
    elif guess_number > random_number:
        return 1


def range(guess_number):
    if guess_number < 1 or guess_number > 20:
        return 1
    else:
        return 0

def next_step():
    activity = input("\nDo you want to start over(y/n)?")
    if activity == 'Y' or activity == 'y':
        initiate()
    elif activity == 'N' or activity == 'n':
        exit()
    else:
        print("Please enter correct choice")
        next_step()

def initiate():
    game()
    next_step()



name = input("Hello! What is your name? ")
initiate()