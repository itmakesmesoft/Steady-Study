a = [list(map(str, input().split())) for _ in range(2)]

c = []


for i in range(2):
    for j in range(len(a[i])):
        c.append(a[i][j])

for i in range(2):
    print(c[i], end = '')