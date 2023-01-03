a= [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]

y, x, n = map(int, input().split())

for i in range(3):
    for j in range(3):
        a[y][x] = n
        print(a[i][j], end = ' ')
    print()