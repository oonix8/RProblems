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
