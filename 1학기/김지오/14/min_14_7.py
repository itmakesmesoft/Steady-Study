a = list(map(int, input().split()))

for i in range(5):
    for j in range(i, 6):
        if a[i]<a[j]:
            a[i], a[j]= a[j], a[i]

for k in range(6):
    print(a[k], end = '')