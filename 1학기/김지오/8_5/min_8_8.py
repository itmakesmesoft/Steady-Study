a= [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    ]
n, m = map(int, input().split())

for i in range(6):
    for j in range(3):
        if i<3:
            a[i][j] =n
        else:
            a[i][j] = m
        print(a[i][j], end ='')
    print()