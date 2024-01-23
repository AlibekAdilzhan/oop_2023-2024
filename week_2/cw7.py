from typing import List


def count_unique(arr: List[int]) -> int:
    """
    Args:
        arr: list of integers
    Returns:
        number of unique elements
    """
    s = set(arr)
    return len(s)


print(count_unique([1,1,1,1]))