import string
def words(arg):
	returned_dict={}
	each_word=set()
	
	if(isinstance(arg,str)):
		if(len(arg)>0):
			str_to_list=[]
			for i in string.whitespace:
				if(i in arg):
					str_to_list=arg.split(i)
					arg=" ".join(str_to_list)
			str_to_list=arg.split(" ")
			clean_list=[i for i in str_to_list if i!='' and i!=' ']

			

			take_care_of_numbers_in_string=[]
			for i in clean_list:
				try:
					take_care_of_numbers_in_string.append(int(i))
				except:
					take_care_of_numbers_in_string.append(i)
			each_word=set(take_care_of_numbers_in_string)
			for a_word in each_word:
				returned_dict.update({a_word:take_care_of_numbers_in_string.count(a_word)})
			return returned_dict
			

		
