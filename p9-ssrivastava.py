""" 
Name: Shivank Srivastava
CWID: 2006832
Date: 12th Dec 2021
"""


file_input=input("Enter the file name:")

#Making a List 
word_list=[]

#Reading the file 
try:
    with open(file_input,"r") as f:
        for line in f:
            for word in line.strip('"').split(): #Removing the punctuations
                if word.strip('"').split():
                    if word.strip('"').istitle(): #Finding the capital letter
                        word_list.append(word)

    if len(word_list)==0:
        print("No capitalized words were found. ")
    else:
        print(sorted(list(set(word_list)))) #Removing the duplicates

except:
    print("The file does not exists.")