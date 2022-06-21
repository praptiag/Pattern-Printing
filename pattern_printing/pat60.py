"""
      3 
    3 2
  3 2 1
3 2 1 0
  3 2 1
    3 2
      3
"""
num=3
for i in range(num,-(num+1),-1):
    for j in range(0,abs(i)):
        print(" ",end=" ")
    for p in range(num,abs(i)-1,-1):
        print(p,end=" ")
    print('\n')