#1
def print_z(n):
    for row in range(n):
        for column in range(n):
            if(
                (row==0) or
                (row==n-1) or 
                (row+column==n-1)
            ):
              print("*",end=" ")
            else:
              print(" ",end=" ")
        print()
size=5
print_z(size)
