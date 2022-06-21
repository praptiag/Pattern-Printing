"""
        A 
      B A B
    C B A B C
  D C B A B C D
E D C B A B C D E
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(totalRows-1,row-1,-1):
        print(" ",end=" ")
    for syb in range ((2*row)-1,0,-1):
        print(chr(65+abs(syb-row)),end=" ")
    print('\n')