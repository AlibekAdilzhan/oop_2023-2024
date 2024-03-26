
# [1, 0, 5, 100, 1, 2, 50, 3], j = 0, n - 1 - j = n - 1
# [1, 0, 5, 1, 2, 50, 3, 100], j = 1, n - 1 - 1 = n - 2
# [1, 0, 5, 1, 2, 3, 50, 100], j = 2, n - 1 - 2 = n - 3
# [1, 0, 1, 2, 3, 5, 50, 100]
def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
