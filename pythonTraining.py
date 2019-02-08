import numpy as np

# def tax(bill):
# 	"""Adds 8% tax to a restaurant bill"""
# 	bill *= 1.08
# 	print "With tax: %f" % bill
# 	return bill

# def tip(bill):
# 	"""addds 15% tip to a restaurant bill"""
# 	bill *= 1.15
# 	print "With tip %f" % bill
# 	return bill

# meal_cost = 200
# meal_with_tax = tax(meal_cost)
# meal_with_tip = tip(meal_cost)

# a = 50
# b = 10

# if a > b:
# 	print("a is bigger than b")

# def power(base,exponent):
# 	result = base ** exponent
# 	print "%d to the power of %d is %d." % (base, exponent, result)


# power(5,5)


# def cube(number):
#   return number * number * number

# def by_three(number):
#   if number % 3 == 0:
#     return cube(number)
#   else:
#     print "False, %d is not divisible by 3" % (number)

# by_three(4)

# ###############

# def hotel_cost(nights):
#   #print 140 * nights
#   return 140 * nights

# hotel_cost(3)

# def plane_ride_cost(city):
#   if city == "Charlotte": 
#     #print " Charlotte cost $183"
#     return 183
#   if city == "Tampa": 
#   	#print " Tampa cost $220"
#   	return 220
#   if city == "Pittsburgh":
#   	#print " Pittsburgh cost $222"
#   	return 222
#   if city == "Los Angeles": 
#   	#print " Los Angeles cost $475"
#   	return 475
  
# plane_ride_cost("Charlotte")

# def rental_car_cost(days):
#   rental_cost = 40
#   if days >= 7:
#     print "7 day car discount applies"
#     return (rental_cost * days - 50)
#   elif days >= 3:
#     print "3 day discount is being applied to the %d day cost is %d" % (days, rental_cost * days - 20)
#     return (rental_cost * days - 20)
#   else: 
#   	print  "%d days cost is %d" % (days, rental_cost * days)
#   	return (rental_cost * days)

# rental_car_cost(4)

# def trip_cost(city, days, spending_money):
# 	total = plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days -1) + spending_money
# 	print plane_ride_cost(city) + rental_car_cost(days) + hotel_cost(days -1);
# 	print "rental car = %d,plane ride cost = %d,hotel_cost = %d,spending_money = %d" % (rental_car_cost(days), plane_ride_cost(city), hotel_cost(days-1), spending_money)
# 	print total
# trip_cost("Tampa", 9, 600)

#####################

# zoo_animals = ["pangolin", "cassowary", "sloth", "cat" ];

# if len(zoo_animals) >= 3:
#   print "The first animal at the zoo is the " + zoo_animals[0]
#   print "The second animal at the zoo is the " + zoo_animals[1]
#   print "The third animal at the zoo is the " + zoo_animals[2]
#   print "The fourth animal at the zoo is the " + zoo_animals[3]

# print zoo_animals[0] + " " + zoo_animals[3]
#####################
# animals = "catdogfrog"
# cat = animals[:3]
# print cat
# dog = animals[3:6]
# print dog
# frog = animals[6:]
# print frog


# my_list = [1,9,3,8,5,7]

# for number in my_list:
  
#   print 2 * number
###############
# start_list = [5,3,1,2,4]
# square_list = []

# for squared_number in start_list:
# 	square_list.append(squared_number ** 2)
# 	#print squared ** 2

# square_list.sort()
# print square_list

# # Object Oriented Programming Python
# # Assigning a dictionary with three key-value pairs to residents:
# residents = {
#   'Puffin' : 104, 
#   'Sloth' : 105, 
#   'Burmese Python' : 106
# }

# print residents['Puffin']
# print residents["Sloth"]
# print residents["Burmese Python"]

# # Adding objects to an object dictionary
# menu = {} # Empty dictionary
# menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
# print menu['Chicken Alfredo']

# # Your code here: Add some dish-price pairs to menu!
# menu['PBJ sandwich'] = 100
# menu['Pickels'] = 200
# menu['Spam'] = 400
# print "There are " + str(len(menu)) + " items on the menu."
# print menu

# # Deleting and changing associated values
# # key - animal_name : value - location 
# zoo_animals = { 'Unicorn' : 'Cotton Candy House',
# 'Sloth' : 'Rainforest Exhibit',
# 'Bengal Tiger' : 'Jungle House',
# 'Atlantic Puffin' : 'Arctic Exhibit',
# 'Rockhopper Penguin' : 'Arctic Exhibit'}
# # A dictionary (or list) declaration may break across multiple lines
# # Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
# del zoo_animals['Unicorn']
# # Your code here!
# del zoo_animals['Sloth']
# del zoo_animals['Bengal Tiger']
# zoo_animals["Rockhopper Penguin"] = "Zoo"
# print zoo_animals

# #################
# inventory = {
#   'gold' : 500,
#   'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
#   'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
# }
# # Adding a key 'burlap bag' and assigning a list to it
# inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# # Sorting the list found under the key 'pouch'
# inventory['pouch'].sort() 
# # Your code here
# inventory['pocket'] = "seashell", "strange berry", "lint"
# inventory["backpack"].sort()
# inventory["backpack"].remove('dagger')
# inventory['gold'] = 550
# ####################
# # Use the 'for' to print out all the definitions
# webster = {
#   "Aardvark" : "A star of a popular children's cartoon show.",
#   "Baa" : "The sound a goat makes.",
#   "Carpet": "Goes on the floor.",
#   "Dab": "A small amount."
# }

# # Add your code below!
# for definitions in webster:
#   print webster[definitions]

# #############
# Write your function below!
# def fizz_count(x):
#   count = 0
#   for item in x:
#     if item == "fizz": 
#     	count = count + 1
#   return count
    


# word_list = ["fizz", "cat", "bob", "fizz", "this is super long with the word fizz in it only once"]
# full_list = fizz_count(word_list)
# print full_list



# this prints out every letter and space in the string
# for words in "this is super long with the word fizz in it only once":
# 	print words
#########################
# shopping_list = ["banana", "orange", "apple"]

# prices = {
#   "banana": 4,
#   "apples": 2,
#   "orange": 1.5,
#   "pear": 3
# }

# stock = {
#   "banana": 1,
#   "apples": 0,
#   "orange": 1,
#   "pear": 1
# }
    


# def compute_bill(food):
# 	total = 0
# 	total_list = 0
	
# 	for items in food:
# 		if stock[items] > 0:
# 			total_list = prices[items] * stock[items]
# 			#print "total_list = {}".format(total_list)
# 			total += prices[items]
# 		else:
# 			print "{} is out of stock".format(items)

		
# 		# print "item = {}".format(items)
# 		# print "price total so far is {}".format(total)
# 		# print "stock items total is {}".format(stock[items])
# 		#return total #why does this change it from a list to a sinlge string?
# 		print " the total bill is {}".format(total)

# compute_bill(shopping_list)

# one = 1
# two = 'two'
# string = "this is a string"

# print "variable one = {2}, variable two = {0}, variable string {1}".format(one, two, string)
### ^ Are we able to increase the number in the curly-brackets?
### ^^ As in, can we do a 'for' & an 'if' statement to move these formatted variables through the list?

# shopping_list = ["banana", "orange", "apple"]

# stock = {
#   "banana": 6,
#   "apple": 0,
#   "orange": 32,
#   "pear": 15
# }
    
# prices = {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }

# # Write your code below!
# def compute_bill(food):
# 	total = 0
# 	for item in food:
# 		if stock[item] > 0:
# 			total += prices[item]
# 			stock[item] -= 1
# 		#return total #--  when this is uncommented, i get nothing when print...why?
# 	print total

# compute_bill(shopping_list)
##################
# steam_list = ["tab", "astroneer", "no mans sky", "dead cells", "hollow knight"]

# stock = {
# 	"tab": 10,
# 	"astroneer": 5,
# 	"no mans sky": 20,
# 	"dead cells": 3,
# 	"hollow knight": 0,
# 	"fire emblem": 200,
# 	"metro 2099": 120
# }

# price = {
# 	"tab": 20,
# 	"astroneer": 24,
# 	"no mans sky": 30,
# 	"dead cells": 30,
# 	"hollow knight": 15,
# 	"fire emblem": 5
# }

# def video_games(wants):
# 	for games in wants:
# 		if stock[games] > 0:
# 			print games
# 		else:
# 			print " {} is out of stock".format(games)

# video_games(steam_list)


# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0, 97.0, 75.0, 92.0],
#   "quizzes": [88.0, 40.0, 94.0],
#   "tests": [75.0, 90.0]
# }
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }
# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }


# students = [ lloyd, alice, tyler]
# for student in students:
# 	print student["name"]
# 	print student["homework"]
# 	print student["quizzes"]
# 	print student["tests"]
# 	print (", ". join( repr(e) for e in student["homework"] ) )


# def average(numbers):
# 	total = sum(numbers)
# 	len_num = len(numbers)
# 	float_total = float(total)
	
	#float_total / len_num = float_total
	# print "float total = {}".format(float_total)
	# print "len_num = {}".format(len_num)
	# print float_total / len_num 


# list_of_numbers = [1,2,3,4,5,6,76.5]
# average(list_of_numbers)

# def average(numbers):
#   total = sum(numbers)
#   len_num = len(numbers)
#   float_total = float(total)
#   return float_total / len_num
  
# def get_average(student):
#   homework = average(student["homework"])
#   quizzes = average(student["quizzes"])
#   tests = average(student["tests"])
#   sum = (homework * .1) + (quizzes * .3) + (tests * .6)
#   return sum

# get_average(tyler)

# def get_letter_grade(score):
# 	if score >= 90:
# 		return "A"
# 	elif score < 90 and score >= 80:
# 		return "B"
# 	elif score < 80 and score >= 70:
# 		return "C"
# 	elif score < 70 and score >= 60:
# 		return "D"
# 	else:
# 		return "F"
# #print get_letter_grade(get_average(lloyd))


# def get_class_average(class_list):
#   results = []
#   for student in class_list:
#     ga = get_average(student)
#     results.append(ga)
#     #print student["name"]
#   return average(results)

# get_class_average(students)

# one-line list comprehension
x = [1,2,3,4,5,6,7,8,9]
out = [numbers ** 2 for numbers in x]
print out
#  lambda functions
double = lambda x: x * 2
print double(5)
# Map and Filter
#Map
seq = [1,2,3,4,5]
double = list(map(lambda x: x * 2, seq))
print double
#Filter
seq = [ 1,2,3,4,5]
filt = list(filter(lambda x: x > 2, seq))
print filt
# Arange
# np.arange(start,stop,skip)
array =  np.arange(0,100,3)
print array
# Linspace
# np.linspace(start, stop, num)
linspace = np.linspace(2.0, 3.0, 100)
print linspace












