import requests
import math
from helper import*


BASE = 122

def strip_url(url):
	string = ''
	counter = url.index('/') + 1
	while(counter < len(url)):
		string += url[counter]
		counter+=1
	print(string)
	return string


def find_short_url(url):
	#url = convert_to_base(url)

	# google.com/email
	# berkeleybside.com/fox-show-1/
	# lukesheard.com/about/i-love-you-kush
	# berkeleybside.com/about/team
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
