T = 10

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    sum2 = 0

    def add_all(y, x):
        sum1=0
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if nx<0 or ny<0 or ny>n-1 or nx>n-1:
                continue
            sum1 += abs(arr[y][x]-arr[ny][nx])
        return sum1


    for i in range(n):
        for j in range(n):
            sum2+= add_all(i, j)

    print(f'#{tc} {sum2}')