"""
Name: Shivank Srivastava
CWID: 20006832
Date: 29th Oct 2021
"""
from typing import Counter
import matplotlib.pyplot as plt


def name_of_file():
	name_of_file = input("Enter the file name:")
	return name_of_file



def remove_values(filename):
	name_of_file = filename
	try:
		fp = open(name_of_file, "r")
	except FileNotFoundError:
		print("File not found")
		exit()
	else:
		with fp:
			for line in fp:
				line = line.strip("\n")
				offset = line.find("From")
				offset1 = line.find("@")
				line = line[-24:]
				offset3 = line.find("@")
				if offset == 0 and offset1>0 and offset3==-1:
					line = line[:-21]
					yield line


def main():
	name = name_of_file()
	dd = {'Sun':0, 'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0}
	a = remove_values(name)
	count = 0
	for i in a:
		if i in dd:
			dd[i] += 1
		count += len(i)
	val= dd.values()
	keys = dd.keys()
	zp = zip(dd.keys(), dd.values())
	for i in val:
		i = val
		j = keys
		plt.bar(j, i, align='center', alpha=0.5, color = 'k')
	
	plt.xlabel('Weekdays')
	plt.ylabel('Number of messages')
	plt.title('Emails per day')
	plt.show()



main()