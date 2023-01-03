a = [list(map(int, input().split())) for _ in range(5)]

a_sum = []
for i in range(5):
    sum1 = 0
    for j in range(4):
        sum1 += a[i][j]
    a_sum.append(sum1)

for i in range(5):
    print(a_sum[i], end = ' ')
