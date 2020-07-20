import datetime
import random
import time

odds = [1,3,5,7,9,10,13,15,17,19,20,23,25,27,29,30,33,35,37,39,40,43,45,47,49,50,53,55,57,59]

for num in odds:
	if (num%2)>0:
		print(str(num) + " is odd")

	else:
		print(str(num), " is even")

