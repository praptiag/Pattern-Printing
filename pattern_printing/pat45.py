#palindromic pyramid
"""
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
"""
totalRows=4
#outer loop for each row
for i in range(1,totalRows+1):
    #1st inner loop for printing blank spaces in each row
    for j in range(i,totalRows):
        print(" ",end=" ")
    #2nd inner loop for printing increasing half in each row
    for k in range(1,i+1):
        print(k,end=" ")
    #3rd inner loop for printing decreasing half in each row
    for p in range (i-1,0,-1):
        print(p,end=" ")
    print('\n')
