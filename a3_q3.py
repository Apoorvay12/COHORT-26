temp=False
num=int(input("Enter a digit: "))
if num==1:
 print("It is not a prime number")
elif num>1:
 for i in range(2,num):
  if(num%i)==0:
   temp=True
   break
 if temp:
  print("It is a prime number")
 else:
  print("It is not a prime number") 