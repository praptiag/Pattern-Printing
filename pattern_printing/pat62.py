"""
      D 
    C D
  B C D
A B C D
  B C D
    C D
      D
"""
num=3
for i in range(num,-(num+1),-1):
    for space in range(0,abs(i)):
        print(" ",end=" ")
    for syb in range(abs(i),num+1):
        print(chr(65+syb),end=" ")
    print('\n')