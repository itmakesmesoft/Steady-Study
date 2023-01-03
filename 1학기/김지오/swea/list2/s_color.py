T = int(input())

for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]

    n= int(input())
    for i in range(n):
        s_y, s_x, e_y, e_x, k = map(int, input().split())

        for s in range(s_y, e_y+1):
            for t in range(s_x, e_x+1):
                arr[s][t] += k

    cnt =0
    for a in range(10):
        for b in range(10):
            if arr[a][b] >2:
                cnt +=1

    print(f'#{tc} {cnt}')