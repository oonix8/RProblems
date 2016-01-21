""" This program is a compliation of functions that solve different
problems.
"""

__author__ = 'marples@google.com (Scott Marple)'

import math
import sys
import time


def Simple_Sum_Array(array):
	"""Finds the sum of an array of integers.

	You are given an arrray of integers of size N. Finds the sum
	of the elements in the array. Runtime in O(n).

	Args:
		array: List of integers to find sum of.
	Returns:
		A integer value of sum of the array.
	"""
	sum = 0

	for n in array:
		sum += n
	return sum


def Diagonal_Difference(array):
	"""Finds the sum of a diagonal in a matrix.

	Given a matrix of size N x N, calculate the absolute difference
	between the sum of its diagonals.

	Args:
		array: Nested list where both length and height are equal.
	Returns:
		An integer difference between both diagonals of the matrix.
	"""
	sum1, sum2 = 0
	rev = len(array) - 1

	for i, x in enumerate(array):
		sum1 += array[i]
		sum2 += array[rev]
		rev -= 1

	return abs(sum1 -sum2)


def Plus_Minus(array):
	"""Find positive, negative, and zero values in an array.

	Given an array of integers, calculate which fraction of the elements
	are positive, negative, and zero, respectively. Returning the
	decimal value of each fraction as well.

	Args:
		array: List of integers to find sum of.
	Returns:
		A three tuple value of floats where the values are representative
		of fraction of the elements in the array. For example -
		(positive, negative, zero).
	"""

	pos, null, neg = 0.0

	for x in array:
		if x == 0:
			null += 1
		elif x < 0:
			neg += 1
		else:
			pos += 1

	return ('%0.4f', '%0.4f', '%0.4f') % (pos/len(array),
		neg/len(array), null/len(array))


def Staircase(height):
	"""Creates a staircase out of spaces and #'s.

	Given a required height integer N, return a staircase structure of
	height N that consists of # symbols and spaces. For example for N = 3,
	  # - 2 spaces, one step
	 ## - 1 space, two steps
	### - 0 spaces, three steps

	Args:
		array: An integer value representing height.
	Returns:
		A string "staircase" constructed using spaces and #'s at a height 
		value of N.
	"""

	staircase = ''

	for i in range (1, h+1):
		staircase += ' '*(h-i) + '#'*(i) + '\n'

	return staircase


def Time_Converter(time):
	"""Converts time from AM/PM to 24-hour time.

	Given a time in AM/PM format will conert it to military (24-hour)
	time. Midnight or 12:00:00AM is considered 00:00:00 and noon or
	12:00:00PM is considered 12:00:00.

	Args:
		time: A string value of time in AM/PM format. Example -
			09:00:00AM or 04:40:00PM.
	Returns:
		A string value of the input time in 24-hour format.
	"""

	time = time.split(':')
	
	if time[0] == '12':
		time[0] == '00'
	if 'AM' in time:
		return time[0] + ':' + time[1] + ':' + time[2].split('AM')[0]
	else:
		return (str(int(time[0]) + 12) + ':' + time[1] + 
			time[2].split['PM'][0])


def Cancel_Class(atten_threshold, arrival_time):
	"""Determine if class is cancelled based on students attendance.

	Given the amount of students who attend a class and the arrival
	tolerence threshold. From the given arrival times of the students,
	determine if class is cancelled. If the threshold is not met before
	class starts at time of 0 then class is cancelled. A negative arrival
	time indicates the student arrived before class started and a positive
	value they arrived after.

	Args:
		atten_threshold: An integer value representing how many students
			need to attend class.
		arrival_time: A list of integers both positive and negative.
	Returns:
		A boolean value representing if the threshold for class was met.
	"""

	bef = 0

	for x in arrival_time:
		if x <= 0:
			bef += 1

	if bef >= atten_threshold:
		return True
	else:
		return False


def Decent_Number(number):
	"""Finds the largest decent number having N digits.

	Given a number find the largest Decent Number having N digits. A
	decent number is a number where the only digits can be 2's or 5's.
	The number of 3's it contains is divisible by 5 and the number of 5's
	it contains is divisble by 3. If no such number exists it will return
	a -1. 

	Args:
		number: An integer value to find the decent number of.
	Returns:
		An integer value as a decent number.
	"""

	c = 5*(2*number%3)

	if c > n:
		return -1
	else:
		return n - c


def Utopian_Tree(cycles):
	"""Find the height of a Utopian tree after N cycles.

	A Utopian tree is planted with a height of 1 meter. A Utopian tree
	grows in 2 cycles every year. Each spring it doubles height and
	over the summer its height increses by 1 meter. Determine the height
	after N cycles.

	Args:
		cycles: An integer value for how long the tree grows.
	Returns:
		An integer value as the height of the tree after N cycles.
	"""

	height = 1

	for i in range(cycles):
		if i % 2 == 0:
			h *= 2
		else:
			h += 1

	return height


def Find_Digits(number):
	"""Seperates a number and finds if those are divisible by N.

	Given an integer, N, traverse it's digits and determine how many
	digits evenly divide N and return the number of evenly divisible
	digits. Each digit is considered to be unique, so each occurance
	of the same evenly divisible digit shoudl be counted.
	Example - N = 111, the answer is 3.

	Args:
		number: An integer value to traverse.
	Returns:
		An integer of the amount of digits divisible by N.
	"""

	nlist = map(int, number)
	count = 0

	for i in nlist:
		if i != 0 and number % i == 0:
			count += 1
	return count


def Service_Lane(shoulder_size, enter, exit):
	"""Finds largest vehicle size that can fit in shoulder from enter to exit.

	Your vehicle breaks down and you need to enter the side of the road.
	Each part of the shoulder can only fit a vehicle of a certain width.
	Determine what size vehicle can enter the shoulder from enter - exit
	given an array of shoulder widths from 1 to 3 at each point. A width
	value of 1 can fit a bicicle, a width value of 2 can fit a car and a
	value of 3. 

	Args:
		shoulder_size: An array of values between 1 and 3.
		enter: An integer value within the index values of the shoulder
			array and before the exit value.
		exit: An integer value within the index values of the shoulder
			array and after the enter value.
	Returns:
		An integer that is the size of the largest vehicle that pass
			through that part of the shoulder.
	"""

	minimum = 3

	for x in range(exit - enter + 1):
		if width[(x + enter)] < minimum:
			minimum = width[(x + i)]

	return minimum


def Cut_the_Sticks(array):
	"""Gets the amount of cuts needed to go through the array.

	With N sticks, where the lengths of each stick is a positive integer.
	A cut operation is performed on all the sticks in the array and
	reduced by the length of the smallest stick. The sticks equal to the
	smallest stick are completely cut out. This is repeated until all sticks
	are cut.

	Args:
		array: An array of integers that are greater than 0.
	Returns:
		A string of values representing the amount of cuts each operation.
	"""
	results

	while len(array) != 0:
		val = min(array)
		cut, zed = 0

		for stick in range(len(array)):
			array[stick] -= val
			cut += 1

			if array[stick] <= =:
				zed += 1
		array = sorted(array, reverse=True)
		del array[len(array) - zed:len(array)]

		results += cut
	return results


def Chocolate(money, cost, exchange):
	"""

	A chocolate store sells their candy bars for a certain cost. They
	a certain number of wrappers to exchange for another candy bar.
	This function finds how many candy bars you can get with N money. A
	certain cost of bars and the wrapper exchange rate.

	Args:
		money: An integer value for the amount of starting money.
		cost: An integer value for the cost of the chocolate bars.
		exchange: An integer value for the exchange rate of candy wrappers.
	Returns:
		An integer value for how many chocolate bars you get based on the
			given values.
	"""

	# Method 1:
	#
	# bar, wrap = money / cost
	# newbar = wrap / exchange
	# 
	# while newbar >= 1:
	# 	bar += int(newbar)
	#   wrap = int(nbar) / exchange + (newbar - int(newbar))
	# 	newbar = wrap
	#
	# return 
	#
	# Method 2:

	bar = money/cost

	return bar + (bar - 1) / (m - 1)


def Small_Cipher(word, encryption):
	"""Encrypts a word through character switching.

	Given a word the cipher will rotate the characters a certain number
	of times to encrypt the word. For example, 'cat' with an encryption of
	2 will become 'ecv'. If the word reaches 'z' it should wrap around back
	to 'a'.

	Args:
		word: A string word to be encrypted.
		encryption: An integer value to move characters in the word by.
	Results:
		A new string word containing the encryted original word. 
	"""

	results = ''
	cipher = int(encryption - int(encryption / 26) * 26)

	for char in range(n):
		if 97 <= ord(s[char]) <= 122:
			if ord(s[char]) + cipher > 122:
				results += chr(96 + (ord(s[char]) + cipher - 90))
			else:
				results += chr(ord(s[char]) + cipher)
		elif 65 <= ord(s[char]) <= 90:
			if ord(s[char]) + cipher > 90:
				results += chr(64 + (ord(s[char]) + cipher - 90))
			else:
				results += chr(ord(s[char]) + cipher)
		else:
			results += s[char]

	return results


def Manasa_and_Stones(stones, disa, disb):
	"""Finds the distance between stones given two distances.

	Given a trail of stones with numbers on them. The stones are
	spread apart by either length a or b. Given the number of the first
	stone is 0, this will find all possible values of the last stone.

	Args:
		stones: An integer amount of stones in the path.
		disa: An integer first distance between a set of stones.
		disb: An integer second distance between a set of stones.
	Returns:
		A string ov values that represent the possible end distance
		value of the stones.
	"""
	results = []
    val = (stones * disa) - disa
        
    if disa != disb:

        for i in range(stones):
            results.append(val)
            val = (val + disb) - disa

        return' '.join(map(str, results))
    else:
        return val


def Library_Fine(dueday, duemonth, dueyear,
	returnday, returnmonth, returnyear):
	"""Finds the late fee for returned books.

	A librarian needs to find out what the late fee for returned books is.
	Based on a set of rules where if the book is returned on or before the
	due date there is no late fee. If it is returned by the end of the
	calendar month the fee is 15 X days late. If it is retunred in the
	same calendar year the fee is 500 X months late. If the book is not
	returned in the same year the flat rate is 10,000.

	Args:
		dueday: An integer value representing the book due date.
		duemonth: An integer value representing the book due month.
		dueyear: An integer value representing the books due year.
		returnday: An integer value representing the books return day.
		returnmonth: An inteer value representing the books return month.
		returnyear: An integer value representing the books return year.
	Returns:
		An integer value representing the late fee for the returned book.
	"""

	if dy > ry:
    	return 0
	elif dy == ry:
    	if dm > rm:
        	return 0
    	elif dm == rm:
        	if dd >= rd:
            	return 0
        	else:
            	return (rd - dd) * 15
    	else:
        	return (rm - dm) * 500
	else:
    	return 10000



def Team_Finder(contestants, contestant_knowledge):
	"""Finds the max number of subjects and how many teams know them.

	In order to find the best team of two. This program compares the
	amount of people in the competition and the subjects they know
	in order to find the max subjects a team knows and how many teams
	know the max amount of subjects.

	Args:
		contestants: An integer for the amount of contestants in tourney.
		contestant_knowledge: List of strings containing each contestants
			knowledge in the form of '1' - knows subject and '0' - does
			not know subject.
	Returns:
		A tuple of two integer values where the first value is the max
		amount of subjects that can be known and the second is a value
		representing the amount of teams that know max subjects.
	"""
	knowledge = []
	pairs_max_top = []
	tmax = 0
	knowmax = 0

	for i in range(contestants):
	    knowledge.append(int(raw_input().strip(), 2))

	for i in xrange(contestants-1):
	    for j in xrange(i+1, contestants):
	        pairs_max_top.append((knowledge[i] | knowledge[j]).count('1'))          

	tmax = max(pairs_max_top) 
	knowmax = pairs_max_top.count(tmax)
	        
	return (tmax, knowmax)


def Long_Factorial(number):
	"""Finds the factorial of a number at larger length.

	Args:
		number: An integer value to find factorial of.
	Returns:
		An integer value for the factorial of supplied number.
	"""

	results = number

	for i in range(number-1, 1, -1):
	    results *= i

	return results


def Recursive_Factorial(number):
	"""Finds the factorial of a number using recursion.

	Args:
		number: An integer value to find the factorial of.
	Returns:
		An integer value for the factorial of supplied number.
	"""

	if number == 1:
        return 1
    else:
        return number * Recursive_Factorial(number-1)


def Present_Exchange(present1, present2, cost1, cost2, exchange):
	"""Finds the most cost effective gift purchasing options.

	Given that you have to purchase two different types of presents for
	a party. They each cost a certain amount, you find out that in some
	cases its cheaper to buy one of the presents and exchange it for the
	other one. This finds the cheapest way to purchase off the gifts.

	Args:
		present1: An integer for how many of the first gift is required
		present2: An integer for how many fo the second gift is required
		cost1: An integer for the cost of the first gift
		cost2: An integer for the cost of the second gift
		exchange: An integer for the cost to exchange one gift for another
	Returns:
		An integer value for the cheapest cost of purchanging that amount
		of gifts at that price.
	"""
    cost = 0
    
    if cost1 + exchange < cost2:
        cost = ((present1 * cost1) + (present2 * cost1) + (present2 * exchange))
    elif cost2 + exchange < cost1:
        cost = ((present1 * cost2) + (present2 * cost2)  + (present1 * exchange))
    else:
        cost = (present1 * cost1) + (present2 * cost2)

    return cost


def Kaprekar_Number(start, stop):
	"""Finds the Kaprekar numbers between a number range.

	A kaprekar number is a number that you can square and then split in
	half and the split number will sum back to the original number.
	An example would be 9, where 9^2 = 81. 8 + 1 = 9. Given a number range
	this will find all the Kaprekar Numbers withing that range.

	Args:
		start: An integer for start of number range.
		stop: An integer for the stop of number range.
	Returns:
		A string of Kaprekar numbers within the given range.
	"""

	results = ''

	for i in range(start, end+1):
	    left = ''
	    left1 = ''
	    right = ''
	    right1 = ''
	    val = str(i * i)
	    
	    if i == 1:
	        results += '%d ' % (i)
	    elif i < 8:
	        pass
	    else:
	        if len(val) % 2 == 0:
	            left = ''.join(val[0: len(val)/2])
	            right = ''.join(val[len(val)/2: len(val)])
	        else:
	            left = ''.join(val[0: len(val)/2])
	            right = ''.join(val[len(val)/2: len(val)])
	        
	        if int(left) + int(right) == i:
	            results += '%d ' % (i)
	if results == '':
	    results = 'INVALID RANGE'
	return results