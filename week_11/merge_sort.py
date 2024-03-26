

def merge(arr_1, arr_2):
    i = 0
    j = 0
    res_arr = []
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] > arr_2[j]:
            res_arr.append(arr_1[i])
            i += 1
        else:
            res_arr.append(arr_2[j])
            j += 1
    if i == len(arr_1):
        while j < len(arr_2):
            res_arr.append(arr_2[j])
            j += 1
    if j == len(arr_2):
        while i < len(arr_1):
            res_arr.append(arr_1[i])    
            i += 1
    return res_arr


def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    mid = n // 2
    arr_1 = merge_sort(arr[:mid])
    arr_2 = merge_sort(arr[mid:])
    merged_arr = merge(arr_1, arr_2)
    return merged_arr

arr = [8, 1, 2, 56, 42, 1]
print(merge_sort(arr))
