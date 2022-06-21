"""
      3 
    2 3
  1 2 3
0 1 2 3
  1 2 3
    2 3
      3
"""
num=3
for i in range(num,-(num+1),-1):
    for j in range(0,abs(i)):
        print(" ",end=" ")
    for p in range(abs(i),num+1):
        print(p,end=" ")
    print('\n')