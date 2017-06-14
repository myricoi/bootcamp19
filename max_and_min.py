def find_max_min(arg):
	"""Function to return the minimum and mximum value from input list"""
	#check to ensure the input is alist
	if(isinstance(arg,list)):
		#return length of the list if max and min are equal
		if(min(arg)==max(arg)):
			return [len(arg)]
		else:
			minimum=min(arg)
			maximum=max(arg)
			return [minimum,maximum]

