""" Practice programming of sorting functions.
"""

__author__ = 'oonix8@gmail.com (Scott Marple)'

import math
import sys

def Insertion_Sort(numlist):
	"""Sorts the list using implementation of insertion sort.

	Given a list of numbers the Insertion_Sort function sorts the numbers
	by dividing the list into two parts. You compare an element from
	second list to the already sorted elements in the first list 
	until you find a greater value than the one you have currently. Once
	found you insert the element in that location and continue until the
	entire list is sorted. 

	The runtime of this equation is O(n^2) where n is the number of elements
	in the list. The fucntion runs in place so it does not take up extra
	memory.
	"""

	for i in range(1, len(numlist)):
		currentval = numlist[i]

		while i > 0 and numlist[i-1] > currentval:
			numlist[i] = numlist[i-1]
			i = i -1

		numlist[i] = currentval

	return numlist


def Selection_Sort(numlist):
	"""Sorts the list using implementation of Selection_Sort.

	Given a list of numbers the Selection_Sort function sorts the numbers
	by comparing the elements after the sorted sublist to each other to
	find the minimum element. Once found it swaps the elements. It moves
	through the unsorted sublist until its all part of the sorted list.

	The runtime of this function is O(n^2) where n is the number of elements
	in the list. The function runs in place so it does not take up extra
	memory.
	"""

	for i in range(len(numlist)):
		small = i
		for j in range(i+1, len(numlist)):
			if numlist[small] > numlist[j]:
				small = j

		temp = numlist[i]
		numlist[i] = numlist[small]
		numlist[small] = temp

	return numlist


def Bubble_Sort(numlist):
	"""Sorts the list using implementation of Bubble_Sort.

	Given a list of numbers the Bubble_Sort function sorts the numbers
	by comparing the values next to each other and moving the smaller
	value to the left. It keeps passing over the function until the
	entire list is sorted.

	The runtime of this function is 0(n^2) where n is the number of elements
	in the list. The function runs in place so it does not take up extra
	memory.
	"""

	for i in range(len(numlist)):
		for j in range(1, len(numlist)):
			if numlist[j] < numlist[j-1]:
				numlist[j], numlist[j-1] = numlist[j-1], numlist[j]

	return numlist


def Max_Heap_Sort(numlist):
	"""Sorts the list using implementation of Max_Heap_Sort.

	Given a list of numbers the Max_Heap_Sort creates a max heap, which
	means in a tree structure where the largest number is at the root of
	the tree at index 0 and is sorted into the end of the list. This process
	is coninued until the entire list is sorted.

	The runtime of this function is O(n log n) where n is the number of
	elements in the list. The function runs in place so no extra memory.
	"""

	end = len(numlist)
	start = end/2 - 1

	def heapify(end, ind):
		left = 2 * ind + 1
		right = 2 * ind + 2
		max = ind

		if left < end and numlist[ind] < numlist[left]:
			max = left
		if right < end and numlist[max] < numlist[right]:
			max = right
		if max != ind:
			numlist[ind], numlist[max] = numlist[max], numlist[ind]
			heapify(end, max)


	for i in range(start, -1, -1):
		heapify(end, i)

	for i in range(end -1, 0, -1):
		numlist[0], numlist[i] = numlist[i], numlist[0]
		heapify(i, 0)

	return numlist


def Min_Heap_Sort(numlist):
	"""Sorts the list using implementation of Min_Heap_Sort.

	Given a list of numbers the Min_Heap_Sort creates a min heap, which
	means in a tree structure where the largest number is at the root of
	the tree at index 0 and is sorted into the end of the list. This process
	is coninued until the entire list is sorted.

	The runtime of this function is O(n log n) where n is the number of
	elements in the list. The function does not run in place and will take
	up double memory.
	"""

	end = len(numlist)
	start = end/2 -1
	sortlist = []

	def heapify(end, ind):
		left = 2 * ind + 1
		right = 2 * ind + 2
		min = ind

		if left < end and numlist[ind] > numlist[left]:
			min = left
		if right < end and numlist[min] > numlist[right]:
			min = right
		if min != ind:
			numlist[min], numlist[ind] = numlist[ind], numlist[min]
			heapify(end, min)

	for i in range(start, -1, -1):
		heapify(end, i)

	for i in range(end -1, -1, -1):
		sortlist.append(numlist[0])
		numlist[0], numlist[i] = numlist[i], numlist[0]
		del numlist[i]
		heapify(i, 0)

	return sortlist

def Merge_Sort(numlist):
	"""Sorts the list using implementation of MergeSort.

	Given a list of numbers the Merge_Sort chooses a middle point of the
	array and rounds down. Once this middle point is selected the problem
	is devided into two subarrays and the Merge_Sort is called on the
	smaller arrays. This is done recursively until there is only one element
	in each array. Then we are able to combine and compare adding the smaller
	arrays back togeather sorting them one by one.

	The complexity of this funciton is worst case O(n log n). The advantage
	of sorting with this is that its fast, but if sets are too large could
	overflow the stack becasue it does not run in place.
	"""

	if len(numlist) <= 1:
		return numlist
	
	mid = len(numlist) // 2
	left = Merge_Sort(numlist[:mid])
	right = Merge_Sort(numlist[mid:])

	return Merge(left, right)

def Merge(left, right):
	"""Helper function for Merge_Sort."""
	result = []

	while len(left) > 0 or len(right) > 0:
		if len(left) == 0:
			result.insert(len(result), right.pop(0))
		elif len(right) == 0:
			result.insert(len(result), left.pop(0))
		elif left[0] < right[0]:
			result.insert(len(result), left.pop(0))
		else:
			result.insert(len(result), right.pop(0))

	return result

def Quick_Sort(numlist):
	"""Sorts the list using implementation of Quicksort.

	Given a list of numbers the Quick_sort chooses a pivot point(usually
	the last item in the list) and compares the other elements in the list
	to the pivot sorting them to the left as less than and the right as
	greater than. Calling itself recursively to perform the sorting on
	the subarray until base case is reached. Then combine the subarrays
	togeather.

	The complexity of this funciton is best case and average of O(n log n)
	but a worst case of O(n^2). The advantage of this sorting function is
	it runs in place and requires no extra memory allocation.
	"""

	return _Quick_Sort(numlist, 0, len(numlist) - 1)
	
def _Quick_Sort(numlist, start, stop):
	"""Helper Function for Quicksort."""

	if stop - start > 0:

		pivot, left, right = numlist[start], start, stop

		while left <= right:
			while numlist[left] < pivot:
				left += 1
			while numlist[right] > pivot:
				right -= 1
			if left <= right:
				numlist[left], numlist[right] = numlist[right], numlist[left]
				left += 1
				right -= 1

		_Quick_Sort(numlist, start, right)
		_Quick_Sort(numlist, left, stop)
	
	return numlist

print '------------------'
print '  INSERTION SORT  '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Insertion_Sort(a)
print b
print '------------------'
print '  SELECTION SORT  '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Selection_Sort(a)
print b
print '------------------'
print '   BUBBLE SORT    '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Bubble_Sort(a)
print b
print '------------------'
print '  MAX HEAP SORT   '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Max_Heap_Sort(a)
print b
print '------------------'
print '  MIN HEAP SORT   '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Min_Heap_Sort(a)
print b
print '------------------'
print '    MERGE SORT    '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Merge_Sort(a)
print b
print '------------------'
print '    QUICK SORT    '
print '------------------'
a = [4,3,6,7,3,5]
print a
b = Quick_Sort(a)
print b
