"""
    *
   ***
  *****
 *******
*********
"""
n=5      #total number of rows
for row in range(1,n+1):
    #print space
    for space in range(1,(n-row)+1):            #space=(total number of rows - row number)
        print(" ",end="")
    #print the symbols
    for syb in range(0,(2*row)-1):              #symbol_in_row =((2*row number)-1)
        print("*",end="")
    print('\n')