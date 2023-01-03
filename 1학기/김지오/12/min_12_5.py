n = int(input())
a = [[' ' for _ in range(4)] for _ in range(3)]
cnt = -1
for i in range(3):
    for j in range(4):
        if i+j>=2:
            cnt +=1
            a[i][j] = n+cnt
        print(a[i][j], end = '')
    print()