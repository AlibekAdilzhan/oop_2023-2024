import time

from bubble_sort import bubble_sort
from merge_sort import merge_sort

import numpy as np

arr = list(np.random.randint(0, 10**4, 10**6))
print("hi")
# start_1 = time.time()
# bubble_sort(arr)
# end_1 = time.time()
# print(end_1 - start_1)
start_2 = time.time()
merge_sort(arr)
end_2 = time.time()
print(end_2 - start_2)