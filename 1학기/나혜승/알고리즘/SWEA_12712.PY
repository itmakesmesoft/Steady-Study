def topdown(y,x):
    global arr
    total1 = arr[y][x]
    dy1 = [-1,1,0,0]
    dx1 = [0,0,-1,1]
    for i in range(1,M):
        for m in range(4):
            topdown_y  = y + (dy1[m] * i)
            topdown_x = x + (dx1[m] * i)
            if topdown_x < 0 or topdown_y < 0 or topdown_y > N-1 or topdown_x > N-1:continue
            total1 += arr[topdown_y][topdown_x]
    return total1      
def diag(y,x):
    global arr
    total2 = arr[y][x]
    dy2 = [-1,-1,1,1]
    dx2 = [-1,1,-1,1]
    for i in range(1,M):
        for m in range(4):
            diagy = y + (dy2[m] * i)
            diagx = x + (dx2[m] * i)
            if diagx < 0 or diagy < 0 or diagx > N-1 or diagy > N-1:continue
            total2 += arr[diagy][diagx]
    return total2      

T = int(input())
for testcase in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    MAX = int(-21e8)
    for i in range(N):
        for j in range(N):
            ret1= topdown(i,j)
            ret2 = diag(i,j)
            if MAX < max(ret1,ret2):
                MAX = max(ret1,ret2)
    print(f'#{testcase} {MAX}')
    
             

'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
'''