"""
Name: Shivank Srivastava
CWID: 20006832
Date: 8th Nov 2021
"""


import os
import sys
import string

print("Program to provide the summary of text file")


def getDict(fileContent):
    wordsDict = dict()
    for word in fileContent:
        wordsDict[word] = wordsDict.get(word, 0) + 1
    return wordsDict


def getSortedValues(wordsDict):
    wordList = list()
    for key, value in wordsDict.items():
        wordList.append((value, key))
    wordList.sort(reverse=True)
    return wordList


def getCountWords(fileContent):
    print("\nTotal number of words in file: ", len(fileContent))


def getCountofDistinctWords(fileContent):
    wordsDict = getDict(fileContent)
    print("\nTotal number of distinct words in file: ", len(wordsDict))


def getFrequentWords(fileContent):
    wordsDict = getDict(fileContent)
    wordList = getSortedValues(wordsDict)
    print("\nTop 25 most frequesnt words are: ")
    for value, key in wordList[:25]:
        print(key, value)


def getCharacterFrequency(fileContent):
    charDict = dict()
    fileStr = ''.join(fileContent)
    for i in range(0, len(fileStr)):
        char = fileStr[i]
        if str.isalpha(char):
            charDict[char] = charDict.get(char, 0) + 1
    charDict = getSortedValues(charDict)
    print("\nCharacter frequency in descending order: ")
    for value, key in charDict:
        print(key, value)


fileName = input("Enter the file name: ")
try:
    fHandle = open(fileName, 'r', encoding = "utf-8")
    strFile = fHandle.read()
except IOError:
    print("Error: can\'t find file or read data")
    sys.exit()

if os.stat(fileName).st_size != 0:  
    fileContent = strFile.translate(str.maketrans("","", string.punctuation))
    fileContent = strFile.translate(str.maketrans("","", "1234567890"))
    getCountWords(fileContent)
    getCountofDistinctWords(fileContent)
    getFrequentWords(fileContent)
    getCharacterFrequency(fileContent)
else:
    print("Oops!!!This file is empty")