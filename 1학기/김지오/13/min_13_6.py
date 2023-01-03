arr = [[4, 5, 6, 1, 3, 1],
     [2, 1, 3, 6, 3, 6]]

a, b, c = map(int, input().split())

cnt1 = 0
for i in range(2):
    for j in range(6):
        if a == arr[i][j]:
            cnt1 += 1
print(f'{a}={cnt1}개')

cnt2 = 0
for i in range(2):
    for j in range(6):
        if b == arr[i][j]:
            cnt2 += 1
print(f'{b}={cnt2}개')

cnt3 = 0
for i in range(2):
    for j in range(6):
        if c == arr[i][j]:
            cnt3 += 1
print(f'{c}={cnt3}개')

