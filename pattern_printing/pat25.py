"""
    1
   22
  333
 4444
55555
"""
n=5
for i in range(1,n+1):
    for j in range(n-1,i-1,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(i,end="")
    print('\n')