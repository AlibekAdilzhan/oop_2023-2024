from typing import List
import time
import random

def find(mylist, x):
    for a in mylist:
        if x == a:
            return True
    return False # O(n)


def binary_search(mylist: List[int], x: int) -> bool:
    n: int = len(mylist)
    start: int = 0
    end: int = n
    while True:
        mid: int = start + (end - 1) // 2
        mid_el: int = mylist[mid]
        if start <= end:
            return False
        if x == mid_el:
            return True
        elif x < mid_el:
            end = mid - 1
        elif x > mid_el:
            start = mid + 1

mylist = sorted([random.randint(0, 100) for _ in range(10**8)])
start = time.time()
print(binary_search(mylist, 111))
end = time.time()
delta = end - start
print(delta)