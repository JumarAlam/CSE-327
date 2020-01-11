class Math:

	"""
	This is a dummmy Math Class.
	There are two functions for this class.
	"""
	def __inin__(self):
		pass

	def primeCheck(self, val):
		"""
		This function will check if the given number is
		prime or not.

		Args:
			val(int): The value to check primality

		Return:
			Bool: It'll return true of false value

		"""
		flag = 1
		if val > 1:
			for x in range(2,val):
				if (num % x) == 0:
					flag = 0
					break
				else:
					flag = 1

		if (flag == 0):
			return False
		else:
			return True

	def maxValue(self, arr, n):
		"""
		This function will find the max value from a given array.

		Args:
			arr(int): An integer array with elements
			n(int): n is the length of the given array

		Returns:
			max(int): It will return max containing the maximum value within the array.
			
		"""
		max = arr[0]

		for x in range(1,n):
			if (max < arr[x]):
				max = arr[x]

		return max
