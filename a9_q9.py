def hcf(x,y): 
   if(y==0): 
     return x
   else: 
     return hcf(y,x%y) 
x=42
y=12
print("The gcd of 42 and 12 is : ", end="") 
print(hcf(42,12))
