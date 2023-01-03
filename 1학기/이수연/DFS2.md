# DFS 심화

신입코테로 90% 이상 출제

DFS 문제 유형

1. 출발-도착 그래프 탐색
2. 완전탐색: 모든 트리를 탐색
3. 백트래킹: used사용

DFS 문제푸는 법

1. 트리 그리기 br lv 몇 인지/ 리턴 조건 
2. 완전탐색할지, 백트래킹할지 결정(백 할 게 있는지) / 사이클 생기는지(중복체크-visit or used배열 사용)
3. DFS를 한번돌릴지, 여러번 돌릴지 결정
4. 원상복구해야할지

연습문제1: arr의 각 행별로 하나의 수만 뽑은 누적합의 최대값 출력 

(완전탐색 문제)

```python

arr = [
    [2,5,7],
    [8,4,-8],
    [-7,1,4],
    [5,1,9]
]
max = 0
def abc(level, sum):
    global max
    if level == 4:
        if max < sum:
            max = sum
        return
    for i in range(3):

        abc(level+1, sum+arr[level][i])

abc(0, 0)
print(max)
```

연습문제2

계단을 내려갈 때 

왼쪽아래 아래 오른쪽아래 로만 내려갈 수 있음

0은 벽

```python
arr =[
    [3,2,4,1],
    [0,1,0,5],
    [2,0,3,0],
    [5,4,0,2],
    [2,-5,2,3]]

max = 0

def abc(now, level, sum):
    global max
    if level == 5:
        if sum > max:
            max = sum
        return

    for i in range(3):
        direct = [-1,0,1]
        dy = level
        dx = now+direct[i]
        if dx < 0 or dx > 3: continue # 맵 범위
        if arr[dy][dx] == 0: continue #   벽이면 노놉
        abc(dx, level+1, sum+arr[dy][dx])

for i in range(4):
    abc(i, 0, 0)

print(max)
```

연습문제 3

0: 길 1: 벽

길을 따라서 종점(3,3)으로 갈 수 있는가?

```python
arr = [
    [0,0,0,0],
    [1,0,1,0],
    [1,0,1,0],
    [0,0,0,0]] # 0: 길, 1: 벽

visit = [[0]*4 for _ in range(4)] # 중복방지

def abc(y, x):
    global flag
    if y == 3 and x == 3:
        flag = 1
        return

    direct_y = [0, 0, -1, 1]
    direct_x = [1, -1, 0, 0]

    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if dy < 0 or dx < 0 or dy > 3 or dx > 3: continue # 배열범위 벗어나면 안 됨
        if visit[dy][dx] == 1: continue # 이미 방문했던 곳이면 안 됨
        if arr[dy][dx] == 1: continue # 벽이면 못
        visit[dy][dx] = 1
        abc(dy, dx)

        if flag == 1: # 넣어도 되고 안 넣어도 되는 코드
            return

visit[0][0] = 1
abc(0, 0)
if flag == 1:
    print('갈 수 있다')
else:
    print('갈 수 없다')
```

연습문제4

미로찾기(DFS) 최단거리 출력

0,0 → 1,3 까지 이동하는 최단거리를 출력하시오

```python
arr = [[0,0,0,0,1],
       [1,0,1,0,1],
       [1,0,1,0,1],
       [0,0,0,0,0]]
Min = 10000000000000
visit = [[0]*5 for _ in range(4)]

def dfs(y, x, level): # level이 곧 cnt / 이동횟수가 됨
    global Min
    if y == 1 and x == 3:
        if level < Min: # 최소레벨 갱신
            Min = level
        return

    direct_y = [1, -1, 0, 0]
    direct_x = [0, 0, 1, -1]

    for i in range(4):
        dy = y + direct_y[i]
        dx = x + direct_x[i]
        if dy < 0 or dy > 3 or dx < 0 or dx > 4: continue
        if arr[dy][dx] == 1: continue
        if visit[dy][dx] == 1: continue
        visit[dy][dx] = 1
        dfs(dy, dx, level+1)
        visit[dy][dx] = 0

visit[0][0] = 1
dfs(0,0,0)
print(Min)
```