"""
Name: Shivank Srivastava
CWID: 20006832
Date: 11th Oct 2021
"""



import string



def init():
 a = input("Please enter the string(s): ")
 if len(a)<=1:
  print("\n OOps!!!Please enter string\n")
  init()
 words = a.split()                               
 result = ''
 invalid =''
 pluralWord = ''
 for word in words:
  pluralWord = plural(word)
  if word == pluralWord:
   invalid = (" ".join([invalid,pluralWord]))
  else:
   result = (" ".join([result,pluralWord]))

 print("\n Plural form for valid Strings: "+result)
 print("List of invalid strings: "+invalid)
 nextActivity()

def nextActivity():
 activity = input("\n Do you want to start over(Y/N)?")
 if activity=='Y'or activity=='y':
  init()
 elif activity=='N' or activity =='n':
  exit()
 else:
  print ("Please enter correct choice")
  nextActivity()

def plural(word):
 if digitChar(word) or specialChar(word):
  return word
 if word.endswith(('ay','ey','iy','oy','uy')):
  word = word+'s'
 elif word.endswith('y'):
  word = word[:-1]
  word = word+'ies'
 elif word.endswith(('o','ch','s','sh','x','z')):
  word = word+'es'
 else:
  word = word+'s'
 return word

def digitChar(inputString):
 return any(char.isdigit() for char in inputString)

def specialChar(inputString):
 return any(char in string.punctuation for char in inputString)


print("String Manipulations")
init()

