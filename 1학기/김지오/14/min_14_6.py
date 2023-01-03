vect = [3, 5, 1, 1, 2, 3, 2]
a = list(map(int, input().split()))


for i in range(4):
    cnt = 0
    for j in range(7):
        if a[i] == vect[j]:
            cnt += 1

    print(f'{a[i]}={cnt}개')
