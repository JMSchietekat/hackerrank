import math
import os
import random
import re
import sys

if __name__ == "__main__":
	read_cnt = int(input())
	phonebook = {}

	for _ in range(read_cnt):
		(name, number) = input().split()		
		phonebook[name] = number

	while True:
		try:
			searchName = input()
		except:
			break
		
		print('{}={}'.format(searchName, phonebook.get(searchName)) if searchName in phonebook else 'Not found')

		if (searchName.lower() == 'q'): break 
