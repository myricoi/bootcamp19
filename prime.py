def gen_prime(n):
	if(isinstance(n,int)):
		is_prime=1
		possible_primes=[i for i in range(n+1) if (i==2) or (i>1 and i%2!=0)]
		return_list=[]

		for num in possible_primes:
			if(num==2):
				return_list.append(num)
			
				
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





