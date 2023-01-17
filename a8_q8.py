def rotation(N):
  output = []
  for i in range(len(N)): 
   output.append(N[i:] + N[:i]) 
  return output 
Q=[5,9,3] 
r=rotation(Q)
print(r)