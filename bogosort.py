import random as r
import time as t

arr = [-4,0,2,16,7,2,8,4,1,3] # Temp array for testing, change values as needed


def eval(arr): # Evaluative function to check whether sorted correctly
	for x in range(0, len(arr)-1):
		if arr[x] > arr[x+1]:
			return False

	return True

def bogosort(arr): # Main sort function, calls eval() after each attempt
	print("Unsorted array:", arr)
	t0 = t.time()
	x = 0

	while not eval(arr):
		r.shuffle(arr)
		x += 1

	t1 = t.time()
	print(f"Sorted array: {arr}\nAttempts taken: {x}\nTime taken: {t1 - t0} seconds")


bogosort(arr)
