y1, x1 = map(int, input().split())
y2, x2 = map(int, input().split())

a = []
cnt = -1
for i in range(3):
    a.append([])
    for j in range(3):
        cnt += 1
        a[i].append(chr(ord('A')+cnt))

a[y1][x1],a[y2][x2] = a[y2][x2],a[y1][x1]

for i in range(3):
    for j in range(3):
        print(a[i][j], end ='')
    print()
