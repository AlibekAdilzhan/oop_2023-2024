
def contains_duplicate(mylist):
    n = len(mylist)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if mylist[i] == mylist[j]:
                return True
    return False

mylist = [1, 2, 3, 4, 4]
print(contains_duplicate(mylist))