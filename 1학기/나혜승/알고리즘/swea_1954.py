T = int(input())
for testcase in range(1,T+1):
    N = int(input())
    dy =[0,1,0,-1]
    dx = [1,0,-1,0]
    y,x = 0,0
    d_plus = 0
    arr = [[0]*N for _ in range(N)]
    for i in range(1,N*N+1):
        arr[y][x] = i
        y += dy[d_plus]
        x += dx[d_plus]
        if y < 0 or x < 0 or y > N-1 or x > N-1 or arr[y][x] != 0:
            y -= dy[d_plus]
            x -= dx[d_plus]
            d_plus = (d_plus+1) % 4
            y += dy[d_plus]
            x += dx[d_plus]
    print(f'#{testcase}')
    for m in range(N):
        for n in range(N):
            print(arr[m][n],end = ' ')
        print()
            
        
                
    
