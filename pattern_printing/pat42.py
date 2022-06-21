"""
        A 
      C B A
    E D C B A
  G F E D C B A
I H G F E D C B A
"""
totalRows=5
for row in range(1,totalRows+1):
    for space in range(1,(totalRows-row)+1):
        print(" ",end=" ")
    for syb in range((2*row)-1,0,-1):
        print(chr(64+syb),end=" ")
    print("\n")