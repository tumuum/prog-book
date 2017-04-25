"""
We can have two versions of this function. One version (seclarge)
returns 5 for a list like [5,3,5]. In this setting, two equal
numbers cannot occupy the same rank. The other version (seclarge_strict), 
insists that the first and the second largest elements be
distinct. It returns 3 for [5,3,5], and it does not
return a value for [5,5,5].
"""



def seclarge(alist):
	
	# Return nothing if the list does NOT have at least
	# two elements.
	#
	# You can also return a string that says the input is not legitimate
	# or you can return the designated python object None. Returning None  is
	# equivalent to a return statement with no argument

	if len(alist) < 2:
		return

	# initiate two variables to keep the first and second
	# largest integers in the list. 
	#
	# We start with keeping the first element as both the first and
	# second largest.

	first = alist[0] 
	second = first

	# Now we will loop trough the list and update 
	# first and second largest elements if we 
	# encounter larger elements.
	#
	# As there is no point in comparing an element with itself
	# we start the loop from the second element.

	for x in alist[1:]:
		if x > first:
			second = first
			first = x
		elif x > second:
			second = x

	return second


def seclarge_strict(alist):
	
	# Return nothing if the list does NOT have at least
	# two elements.
	#
	# You can also return a string that says the input is not legitimate
	# or you can return the designated python object None. Returning None  is
	# equivalent to a return statement with no argument

	if len(alist) < 2:
		return

	# initiate two variables to keep the first and second
	# largest integers in the list. 
	#
	# At this point we differ from the previous solution. We assign None 
	# as the second largest element. The reason is that having at least two
	# elements does no longer guarantee that you will have a second largest
	# element. You need to return None for an input like [3,3], as, strictly 
	# speaking, there is no second largest element in this list.
	#

	first = alist[0] 
	second = None 

	# Now we will loop trough the list and update 
	# first and second largest elements if we 
	# encounter larger elements.
	#
	# As there is no point in comparing an element with itself
	# we start the loop from the second element.

	for x in alist[1:]:
		if x > first:
			second = first
			first = x
		# the second difference from the previous solution comes here
		# we do not update the second largest element with an element
		# greater than the second but equal to the first. 
		# 
		# We also need to be carful not to compare second with an integer,
		# when second has None as its value. 
		#
		# When second is None, if an element comes which is less than first 
		# we update second with this element 
		#
		elif second == None and x < first:
			second = x
		# If we know that second is not None, we can safely update it with an
		# element less than first but greater than secon:
		elif x > second and x != first:
			second = x

	return second
