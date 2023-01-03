T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    cnt = 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    x, y, idx = 0, 0, 0


    while cnt<n*n:
        ny = y + dy[idx]
        nx = x + dx[idx]

        if ny<0 or nx<0 or nx>n-1 or ny>n-1 or arr[ny][nx]!=0:
            idx +=1

        if idx>3:
            idx = 0

        if arr[y][x]==0:
            cnt+=1
            arr[y][x]=cnt
            y+=dy[idx]
            x+=dx[idx]

    print(f'#{tc}', end=' ')
    print()
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()



