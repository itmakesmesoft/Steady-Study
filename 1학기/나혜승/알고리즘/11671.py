def cover(y,x,k):
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    for i in range(4):
        for j in range(1,k+1):
            ny = y + (dy[i] * j)
            nx = x + (dx[i] * j)
            if ny < 0 or nx < 0 or ny > N-1 or nx > N-1:continue
            if arr[ny][nx] == 'H':
                arr[ny][nx] = 'X' 

T = int(input())
for testcase in range(1,T+1):
    dict1 = {'A':1,'B':2,'C':3}
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 'H' and arr[i][j] != 'X':
                k = dict1[arr[i][j]]
                cover(i,j,k)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print(f'#{testcase} {cnt}')
'''
1
9
XXXXXXXXX
XXXHXXXXX
XXHAHXXHX
XXHHXXXXX
XXXXXXXXX
XXAHHXXXX
XXHXXHAHX
XXAHXXHXX
XXHXHXXXX
'''