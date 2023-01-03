a = list(map(str, input().split()))

for i in range(5):
    for j in range(5-i):
        print(a[i+j], end= ' ')
    print()