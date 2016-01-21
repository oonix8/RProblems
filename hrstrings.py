""" Practice string functions.
"""

__author__ = 'oonix8@gmail.com (Scott Marple)'

import math
import sys

def Pangram(text):
	"""Takes a sentence and determines if pangram.

	A pangram is a sentence that has all characters of the alphabet.
	Given a string input determine if the sentence is a pangram.

	Args:
		text: A string input as a sentence (punctuation not expected)
	Returns:
		A boolean if the sentence is a pangram or not.
	"""

	if len(set(text = text.replace(' ', '').lower())) == 26:
		return True
	else:
		return False


def FunnyString(text):
	"""Takes a string and determines if same distance from end of alphabet

	Given an input string the function will determine if the characters
	in the string are equally distant from the end of the alphabet.
	Example: acxz is 1, 3, 24, 26. The characters a and z are the same
	distance apart from the end of the alphabet.

	Args:
		text: A string input as a set of characters.
	Returns:
		A boolean value if the characters input are equally distant from
		end of alphabet.
	"""

	rev = len(text) - 1
	funny = True

	for a in range(len(text) - 1):
		if (abs(ord(text[a]) - ord(text[a + 1])) ==
			abs(ord(text[rev]) - ord(text[rev -1 ]))):
			funny = True
		else:
			funny = False
			break

	if funny:
		return True
	else:
		return False


def DuplicateCharacter(text):
	"""Takes a string and find deletion number to prevent consecutive duplicate.

	Given an input string we determine if the next character is the same
	and if true will return count how many deletions are required to make
	the string have no consecutive duplicate characters.

	Args:
		text: A string of characters
	Returns:
		A integer value for how many deletions are required.
	"""
	mindel = 0

	for a in range(len(text) - 1):
		if text[a] == text[a + 1]:
			mindel += 1

	return mindel


def StringCombo(text):
	"""Takes a string of charcters and find is anagram and palindrome.

	Give a string we determin if the characters in the string as an
	anagram for a palindrome. 

	Args:
		text: A string of characters
	Returns:
		A boolean variable of yes or no if value is a palindrome.
	"""

	text2 = set(text)
	found = False

	if len(text) % 2 == 0:
		for a in text2:
			if text.count(a) % 2 != 0:
				found = False
				break
			else:
				found = True
	else:
		odd = False
		for a in string2
			if string.count(a) % 2 != 0 and odd:
				found = False
				break
			else:
				if string.count(a) % 2 != 0:
					odd = True
					found = True

	return found


def 