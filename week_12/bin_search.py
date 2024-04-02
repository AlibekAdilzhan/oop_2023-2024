from typing import List

def binary_search(arr: List[int], L: int, R: int, x: int) -> bool:

    while True:
        if L > R:
            break
        m: int = L + (R - L) // 2
        if arr[m] == x:
            return True
        elif arr[m] > x:
            R = m - 1
        elif arr[m] < x:
            L = m + 1
    return False


# arr = [1, 3, 3, 21, 35, 35, 81, 91, 92, 100]
# x = 40
# print(binary_search(arr, 0, len(arr) - 1, x))