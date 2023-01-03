n = int(input())

a = []
cnt = 13
for i in range(3):
    a.append([])
    for j in range(4):
        cnt -=1
        a[i].append(cnt)

    a[i][n] =0

for i in range(3):
    for j in range(4):
        print(a[i][j], end=' ')
    print()

