import numpy as np
import time

size = 1000000

# Python list
list1 = list(range(size))
list2 = list(range(size))

start = time.time()
result_list = [list1[i] + list2[i] for i in range(size)]
end = time.time()

print("Python list time:", end - start)

# NumPy array
arr1 = np.array(list1)
arr2 = np.array(list2)

start = time.time()
result_array = arr1 + arr2
end = time.time()

print("NumPy array time:", end - start)
