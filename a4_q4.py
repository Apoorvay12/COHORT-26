temp=int(input("Enter a number: "))
print("All the prime numbers upto",temp,"are: ")
for num in range(2,temp+1):
 i=2
 for i in range(2,num):
  if num%i==0:
   i=num 
   break
 if(i!=num):
  print(num,end=" ")