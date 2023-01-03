def topdown(y,x):
    global map,N,cnt
    idx1 = 1
    dy1 = [-1,1,0,0] #상하좌우
    dx1 = [0,0,-1,1]
    for i in range(4):
        ny = y + (dy1[i] * idx1)
        nx = x + (dx1[i] * idx1)
        while (1):
            # 벽에 부딪히면 방향 바꿔
            if ny < 0 or nx < 0 or ny > N-1 or nx > N-1 or MAP[ny][nx] == 3:
                idx1 = 1
                break
            if MAP[ny][nx] == 2: #토끼 찾으면 카운트 세주고
                cnt += 1         #사냥 범위 1늘려주기
            idx1 += 1
            ny = y + (dy1[i] * idx1)
            nx = x + (dx1[i] * idx1)
    return

def zig(y,x):
    global cnt
    idx1 = 1
    dy2 = [-1,-1,1,1] #좌좌우우
    dx2 = [-1,1,-1,1]
    for m in range(4):
        ny = y + (dy2[m] * idx1)
        nx = x + (dx2[m] * idx1)
        while (1):
            # 벽에 부딪히면 방향 바꿔
            if ny < 0 or nx < 0 or ny > N-1 or nx > N-1 or MAP[ny][nx] == 3:
                idx1 = 1
                break
            if MAP[ny][nx] == 2: #토끼 찾으면 카운트 세주고
                cnt += 1         #사냥 범위 1늘려주기
            idx1 += 1
            ny = y + (dy2[m] * idx1)
            nx = x + (dx2[m] * idx1)
    return

T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    MAP = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                topdown(i,j)  #사냥꾼 위치
                zig(i,j)
    print(f'#{testcase} {cnt}')


'''
3                     
9                     
3 2 2 0 3 2 3 2 2     
0 2 3 0 2 1 2 2 0
0 0 3 0 0 2 2 0 2
0 3 2 0 2 2 0 2 0
2 3 2 2 3 3 0 0 3
2 3 2 3 2 2 3 0 2
2 0 3 2 0 0 3 0 0
2 0 0 0 0 0 0 2 1
2 3 2 1 0 0 2 0 0
7                     
2 2 0 3 2 2 2
2 2 0 0 0 3 0
2 3 2 2 3 2 2
0 2 0 0 1 3 2
3 2 2 2 0 0 0
0 3 0 0 0 2 0
3 0 1 2 0 2 2
'''   