import math
class BinarySearch(list):
	def __init__(self,a,b):
		list_len=1
		item=0
		while(list_len<=a):
			item+=b
			self.append(item)
			list_len+=1
		self.length=len(self)

	def search(self,arg):
		# since it is a list of numbers ensure the input is numbers
		try:
			search_for=int(arg)
		except:
			return "not found"
		first=0                 # index of first element in the list
		last =self.length-1       #index of last element in the list
		found=False               # flag to check if the element being searched has been found
		counter=0 
		mid=0
		# before searching in the middle of the list check to see if the element being searched is at the start or end of the list
		# if so no need to search the middle of the list
		if(search_for==self[first]):
			return {'count':counter,'index':first}
		elif(search_for==self[last]):
			return {'count':counter,'index':last}

		# if the element is neither at the start nor at the end, search through the list by dividing and conquering
		else:
			counter=-1  # counter set to -1 because the first run of the loop is not an iteration hence considered iteration 0
			while(first<last):
				counter+=1
				mid=math.floor((first+last)/2)
				if(self[mid]==search_for):
					found=True
					break
				else:
					if(search_for<self[mid]):
						last=mid-1
					else:
						first=mid+1
				
			if(found):
				return {'count':counter,'index':mid}
			else:
				return {'count':counter,'index':-1}
