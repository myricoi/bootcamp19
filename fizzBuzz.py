def fizz_buzz(num):
  if(isinstance(num,int)):
    if(num%3==0 and num%5>0):
      return 'Fizz'
    elif(num%5==0 and num%3>0):
      return 'Buzz'
    elif(num%3==0 and num%5==0):
      return 'FizzBuzz'
    else:
      return num
  else:
    return None
