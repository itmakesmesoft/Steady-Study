n,m = map(int,input().split())
name = [1,2,3,4,5,6]
arr = [
    [0,0,1,0,1,6],
    [1,0,0,1,0,0],
    [0,0,0,0,1,0],
    [1,0,0,0,0,0],
    [1,0,0,0,0,0],
    [0,0,0,0,0,0],
]
Min = 30
cnt = 0
used = [0] * len(name)
def dfs(now):
    global cnt, used,Min
    if now == m:
        if cnt < Min:
            Min = cnt
        return

    for x in range(len(name)):
        if arr[now][x] == 1 and used[x] == 0:
            used[x] = 1
            cnt += 1
            dfs(x)
            used[x] = 0



dfs(n-1)
print(cnt)