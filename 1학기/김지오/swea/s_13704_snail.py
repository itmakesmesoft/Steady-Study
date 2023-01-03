T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    cnt = 1

    directx = [1, 0, -1, 0]
    directy = [0, 1, 0, -1]
    for x in range(n):
        for y in range(n):
            for i in range(4):
                ny = y + directy[i]
                nx = x + directx[i]

                if ny<0 or nx<0 or nx>n-1 or ny>n-1:
                    continue

        cnt +=1
        arr[ny][nx] = cnt

    print(f'#{tc}')
    for s in range(n):
        for t in range(n):
            print(arr[s][t], end= " ")
        print()