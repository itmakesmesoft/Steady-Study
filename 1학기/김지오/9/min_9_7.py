a = []

for _ in range(6):
    a.append(list(map(int, input().split())))

cnt = 0
for i in range(6):
    if a[i][0]< a[i][1]:
        cnt += 1
        a[i][0], a[i][1] = a[i][1], a[i][0]

for i in range(6):
    for j in range(2):
        print(a[i][j], end = ' ')
    print()
print(f'{cnt}명')