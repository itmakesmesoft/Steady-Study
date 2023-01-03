a = [list(map(int, input().split())) for _ in range(3) ]

add = 0
for i in range(3):
    for j in range(3):
        if i>=j:
            add += a[i][j]

print(add)