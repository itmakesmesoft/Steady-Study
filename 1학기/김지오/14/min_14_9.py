a = [10, 50, 40, 20, 30, 40]

b=  list(map(int, input().split()))

for i in range(6):
    cnt = 0
    for j in range(6):
        if b[i] < a[j]:
            cnt += 1
    print(f'{b[i]}={cnt}개')