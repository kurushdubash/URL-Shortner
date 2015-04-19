import requests

# api ask a server for data and it will give you that data.
# api's are usually URLs. 

#URL : https://data.ny.gov/resource/d6yy-54nr.json

nysixnum = "https://data.ny.gov/resource/d6yy-54nr.json"
nyfivemeg = "https://data.ny.gov/resource/5xaw-6ayf.json"
#this is a comment

def get_data_from_powerball():
	everypower = open('powerball.txt', 'r')
	workinglst = []
	for lst in everypower:
		workinglst.append(lst[12:33])
	finallst = parse_data(workinglst[1:])
	everypower.close()
	return finallst

def get_lottery_data(URL):
	"""Returns data (which is list of dictionaries) for Lottery"""
	data = requests.get(URL) #one bigass list where each item is a dictionary. 
	data = data.json() #from object to dictionary
	return data

def get_lottery_numbers(URL):
	"""takes in URL, uses parse_data to return a list (size 1000) of list of winning numbers"""
	# """Returns an array of the frequency of each number in the lottery"""
	thelist = get_lottery_data(URL)
	win_numbers = []
	for element in thelist:
		if element["draw_date"]=="2013-10-29T00:00:00":
			break;
		win_numbers.append(element['winning_numbers'])
	finallst = parse_data(win_numbers)
	return finallst

def how_many_entries(URL):
	"""should always return 1000, for number of entries"""
	return len(get_lottery_numbers(URL))

def get_mega_numbers(URL):
	"""Input: URL of selected lottery
		Output: Array of ints containing every single megaball number"""
	result=[];
	data=get_lottery_data(URL)
	for e in data:
		if e["draw_date"]=="2013-10-29T00:00:00":
			break;
		result.append(int (e["mega_ball"]))
	return result

def parse_string_to_listint(string):
	"""takes in string and converts to int (hardcoded) This is the helper method for parse_data."""
	string = string.split()
	length = len(string)
	newlist = []
	first = int (string[0])
	second = int (string[1])
	third = int (string[2])
	forth = int (string[3])
	fifth = int (string[4])
	newlist.append(first)
	newlist.append(second)
	newlist.append(third)
	newlist.append(forth)
	newlist.append(fifth)
	return newlist

def parse_data(lst):
	"""takes in list of strings (result from get_lottery_numbers),
		returns list of list of integers."""
	finallist = []
	for element in lst:
		finallist.append(parse_string_to_listint(element))
	return finallist

def frequency_winning_numbers(lottery_array):
	result_numbers=[0 for x in range(76)]
	for element in lottery_array:
		for element1 in element:
			result_numbers[element1]=result_numbers[element1]+1
	count=1
	while(count<75 and result_numbers[count]!=0):
		count+=1
	return result_numbers[:count]
def frequency_mega(lottery_array):
	result_numbers=[0 for x in range(16)]
	for element in lottery_array:
		result_numbers[element]=result_numbers[element]+1
	return result_numbers
	
def probability(freqlst):
	"""Takes in a tuple where lottery_array[0] is an array of number frequency by index
		and lottery_array[1] is the frequency of mega numbers by index"""
	problist = []
	total = 0
	totes = 0
	for elem in freqlst:
		total = total + elem
	for item in freqlst:
		prob = item / total
		problist.append(prob)
	for la in problist:
		totes = totes + la
	return problist

def find_probability(problist, listoffive):
	"""given result of probability and list of 5 numbers, return the probability 
		that all 5 hit. Should always be less than result of best_five"""
	probs = []
	for i in listoffive:
		probs.append(problist[i])
	totprob = 1
	for n in probs:
		totprob = totprob * n
	return totprob


	
def best_five(freqlst):
	temp=sorted(range(len(freqlst)),key=lambda i:freqlst[i])
	return [temp[-1],temp[-2],temp[-3],temp[-4],temp[-5]]

def random_lottery():
	"""Retursn a tuple of which the first element is an array of 5 random,
		non duplicate numbers, and the second element is a mega number"""
	return 0

def check(keyword):
	if keyword.upper() == 'NY':
		return get_lottery_numbers(nyfivemeg)
	elif keyword.upper()== 'PB':
		return get_data_from_powerball()