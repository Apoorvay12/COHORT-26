num=int(input("Enter a number: "))
op=1
inv=0
while num>0:
 od=num%10
 np=od
 nd=op
 temp=pow(10,np-1)
 inv=inv+ nd*temp
 op=op+1
 num=num//10
print(inv)
