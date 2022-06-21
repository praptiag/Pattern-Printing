"""
    A
   AB
  ABC
 ABCD
ABCDE
"""
for i in range(0,5):
    for j in range(4,i,-1):
        print(" ",end="")
    for k in range(0,i+1):
        print(chr(65+k),end="")
    print("\n")