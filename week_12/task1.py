
n = int(input())
arr = list(map(int, input().split()))
x = int(input())

c = 0
for s in arr:
    if s == x:
        c += 1

print(c)