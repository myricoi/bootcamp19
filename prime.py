def gen_prime(n):
	if(isinstance(n,int)):
		is_prime=1
		return_list=[]

		for num in range(0,n+1):
			if(num<2):
				continue
			elif(num==2):
				return_list.append(num)
			elif(num%2==0):
				continue
				
			else:
				for divisor in range(2,num):
					if(num%divisor==0):
						is_prime=0
						break
				if(is_prime):
					return_list.append(num)
				
				is_prime=1
		return return_list
	else:
		return "Only an integer is allowed"
if(__name__=='__main__'):
	gen_prime(100)





