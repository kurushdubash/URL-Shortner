import requests
import math
from helper import*


BASE = 122

def find_short_url(url):
	#url = convert_to_base(url)
	test = saturate(url)
	print(test[1])
	return test[0]

def convert_to_base(url):
	base_value = []


	url = url[::-1]

	int_sum=0
	counter = math.log(url,BASE) + 1
	

	for idx, char in enumerate(url):
		int_sum += true_ord(char) * int(math.pow(BASE, idx))
	return base_value[::-1]

def true_ord(char):
	return 0

