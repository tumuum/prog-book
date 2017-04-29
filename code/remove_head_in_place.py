# This function does not return anything. It alters its argument.

def remove_head(alist):
	"""Removes the first item in a list"""
	if alist == []:
		print("Sorry, I can't remove anything from an empty list")
	else:
		item = alist.pop(0) # pop(x) removes and returns the item at index x
		print("Just removed",item)
		print("Your list is now: ",alist)
