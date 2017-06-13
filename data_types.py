from types import *
def data_type(arg):
	if(isinstance(arg,bool)):
		return arg
	if(isinstance(arg,str)):
		return len(arg)
	if(isinstance(arg,list)):
		if(len(arg)>=3):
			return arg[2]
		else:
			return None
	if(isinstance(arg,int)):
		if(arg<100):
			return 'less than 100'
		elif(arg==100):
			return 'equal to 100'
		else:
			return 'more than 100'
	if(repr(type(arg)=="<class \'NoneType\'>")):
		return 'no value'
if(__name__=='__main__'):
	data_types(None)