"""
      D 
    D C
  D C B
D C B A
  D C B
    D C
      D
"""
num=3
for i in range(num,-(num+1),-1):
    for space in range(0,abs(i)):
        print(" ",end=" ")
    for syb in range(num,abs(i)-1,-1):
        print(chr(65+syb),end=" ")
    print("\n")