N,M,x,y,K =  map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
orders = list(map(int,input().split()))
dice = [0]*7
#제자리, 동,서,북,남
dy = [0,0,0,-1,1]
dx = [0,1,-1,0,0]
#지도 범위 내에서 이동하기
for order in orders:
    ny = y + dy[order]
    nx = x + dx[order]
    if ny < 0 or nx < 0 or ny > N-1 or nx > M-1:
        continue
# 동,서,남,북 각각 주사위 인덱스 변화구하기
    if order == 1:
        dice[3],dice[6],dice[1],dice[4] = dice[1],dice[3],dice[4],dice[6]

    elif order == 2:
        dice[4],dice[1],dice[6],dice[3] =dice[1],dice[3],dice[4],dice[6]

    elif order == 3:
        dice[2],dice[6],dice[1],dice[5] = dice[1],dice[2],dice[5],dice[6]

    elif order == 4:
        dice[5],dice[1],dice[6],dice[2] = dice[1],dice[2],dice[5],dice[6]

# 0 일때 주사위 아래 복사
    if arr[ny][nx] == 0:
        arr[ny][nx] = dice[6]

# 주사위에 지도 숫자 복사
    else:
        dice[6] = arr[ny][nx]
        arr[ny][nx] = 0

    y,x = ny,nx

    print(dice[1])

