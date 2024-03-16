n = list(map(int, input().split(':')))
if n[0] < n[1]:
    print(2)
elif n[1] < n[0]:
    print(1)
elif n[0] == n[1]:
    print(0)
