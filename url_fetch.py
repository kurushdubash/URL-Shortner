import requests
import math
import random
from database import *

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def strip_url(url):
	string = ''
	counter = url.index('/') + 1
	while(counter < len(url)):
		string += url[counter]
		counter+=1
	print(string)
	return string

def generate_short_code():
	code = ''
	for num in range(6):
		code += values[random.randrange(0, 63)]
	return code

def find_short_url(url):
	short_code = generate_short_code()
	while(check_database(short_code) != None):
		short_code=generate_short_code()
	add_shortcode_site(url, short_code)
	return short_code



