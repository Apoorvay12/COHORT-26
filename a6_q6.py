num=int(input("Enter number to reverse"))
numcopy=num
temp=10
reverse=0
while(num>=1):
 digit=num%10
 reverse=reverse+(digit*temp)
 temp=int(temp/10)
 num=int(num/10)
print("Reverse number of ",numcopy,"is",reverse)