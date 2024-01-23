from typing import List

def count_even(arr: List[int]) -> int:
    """
    Args:
        arr: list of integers
    
    Returns:
        int, the number of even elements in the arr
    """
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    return count


arr: List[int] = [1, 1, 2, 2, 3, 5, 6]
print(count_even(arr))