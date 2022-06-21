"""
        *   
      *   *
    *   *   *
  *   *   *   *
*   *   *   *   *
  *   *   *   *
    *   *   *
      *   *
        *
"""
size=4
for i in range(size,-(size+1),-1):
    for j in range(0,abs(i)):
        print(" ",end=" ")
    for p in range(size,abs(i)-1,-1):
        print("*  ",end=" ")
    print("\n")