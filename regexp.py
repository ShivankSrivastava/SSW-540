""" 
Name: Shivank Srivastava
CWID: 2006832
Date: 15th Nov 2021
"""


filename = input("Enter the file name to print all the words start with capital letter: ")
word_list=[] 
try:
    with open(filename,"r") as f:
        for line in f:
          for word in line.strip('"').split():
                if word.strip('"').istitle():
                    word_list.append(word)

    if len(word_list)==0:
        print("Sorry .No capitalized words were found in this file")

    else:
        print(list(set(word_list)))

except:
    print("The filename entered is invalid or does not exist")