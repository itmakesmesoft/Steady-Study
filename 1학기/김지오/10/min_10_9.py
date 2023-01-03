a = []
cnt = 0
for i in range(4):
    a.append([])
    for j in range(4):
        cnt += 1
        a[i].append(cnt)
# a[i][j],a[j][i] = a[j][i],a[i][j]

for i in range(4):
    for j in range(4):
        print(a[3-j][i], end=' ')
    print()