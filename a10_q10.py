n=int(input("Enter an integer:"))
print("The factors are:")
i=1
while(i<=n):
  a=0
  if(n%i==0):
   j=1
   while(j<=i):
     if(i%j==0):
       a=a+1
     j=j+1
   if(a==2):
     print(i)
  i=i+1