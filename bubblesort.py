import numpy as np
from time import process_time

# Max is 1 milion numbers with 1 mil numbers
m = 1000 # highest number
n=m # array
t1_start = process_time() 
array = np.random.randint(m, size=(n))
print("Max and array length is: ", m)
print("Start")

def bubbleSort(arr): 
    for i in range(n-1): 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] # The Swap
                # print(i, ":", j,  ":" , arr)

bubbleSort(array)
print("Finish")

t1_stop = process_time()
print("Elapsed time seconds:", t1_stop-t1_start)