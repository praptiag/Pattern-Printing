"""
EEEEE
 DDDD
  CCC
   BB
    A
"""
n=5
for i in range(n,0,-1):
    for j in range(n-1,i-1,-1):
        print(" ",end="")
    for k in range(0,i):
        print(chr(64+i),end="")
    print("\n")