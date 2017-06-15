def find_missing(list1,list2):
	# Ensure the lists are not empty if so proceed with checking
	if(list1 or list2):
		set1=set(list1)
		set2=set(list2)
		missing_number=list((set1-set2) or (set2-set1))
		if(missing_number):
			return missing_number[0]
		else:
			return 0
	# if the lists are empty, return 0
		
	else:
		return 0



