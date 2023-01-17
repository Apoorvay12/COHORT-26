def countDigit(n): 
 if n//10 == 0: 
  return 1 
 return 1 + countDigit(n//10) 
n=345289467 
print("Number of digits : % d" % (countDigit(n)))