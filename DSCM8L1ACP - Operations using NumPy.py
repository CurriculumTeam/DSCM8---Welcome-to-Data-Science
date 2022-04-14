#1)Replace all odd numbers in arr with -1 without changing arr
#2)Convert a 1D array to a 2D array with 2 rows
#3)Iterate through the array and find the sum of All elements
import numpy as np
arr=np.arange(10)
out=np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)
#1D TO 2D
newarray=arr.reshape(2, -1)
print(newarray)
#SUM
sum=0
for x in range(0,len(arr)):
  sum=sum+arr[x]
print(sum)


