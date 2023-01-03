자료구조: 데이터를 저장하거나 관리하는 방식

### 선형 자료구조

- 리스트
    - 단점: 3 4 7 7 9 7 3  2 4 7 8 9
    - 값을 추가하거나 삭제할 때 느림
    - (공백이나 배열 조정이 필요)

- 링크드 리스트(연결리스트) 장점: 값을 추가하거나 삭제할 때 용이
    
    3 → 4 → 7 → 7 → 8
    

### 비선형 자료구조

### 1. 그래프

: data들의 관계를 나타내고 표현할 때 사용

ex) 지하철노선도, 버스노선

### 그래프의 종류

### (1) 트리

ex) 회사 조직도(상하관계)

1. 단방향
2. 부모 자식 관계를 가짐
맨 바닥(맨끝자식): 리프누드
3. cycle 발생 안 함

### (2)트리가 아닌 그래프: 양방향 그래프

1. 양방향
2. cycle 발생함

---

# 그래프 저장: 그래프를 코드로 표현하기

<img src="../../Downloads/KakaoTalk_Photo_2022-08-18-23-12-03.jpeg" width="200"/>

## 1. 인접행렬(이차원 리스트)

- 가로축: 자식을 나타냄
- 세로축: 부모를 나타냄

```python
name = ['A', 'B', 'C', 'D', 'E']
arr = [
    [0,1,1,0,0], #A의 자식은 1로 표시
    [0,0,0,0,1], #B
    [0,1,0,0,0], #C
    [0,1,0,0,0], #D
    [0,0,0,1,0]  #E
		]
# A의 부모는 1로 표시
```

## 2. 인접리스트

```python
# 인접리스트
brr = [[1,2],
     [3,4]
     [5],
     [],
     []]
```

<img src="../../Downloads/KakaoTalk_Photo_2022-08-18-23-15-03.jpeg" width="200"/>

## 3. 이진 트리에 한해서 일차원리스트 - 가지가 2 개뿐

```python
# 첫번째 인덱스는 비워둔다
arr = ['', 'A', 'B', 'C', 'D', 'E', 'F']
```

---

### 그래프 연습문제

가장 인기있는 사람 출력하기

```python
# 인덱스 번호는 임의로 부여해도됨 어차피 코드랑만 맞으면 됨!
# 인덱스 번호에 맞춰서 arr에 입력 잘 하면 됨
name = ['A', 'B', 'C', 'D', 'E']
arr = [
    [0,1,1,0,0], #A
    [0,0,0,0,1], #B
    [0,1,0,0,0], #C
    [0,1,0,0,0], #D
    [0,0,0,1,0] #E
]

total = 0
max = 0
max_name = 0
for i in range(5):
    for j in range(5):
        total += arr[j][i]
    if total > max:
        max = total
        max_name = name[i]
    total = 0

print(max_name)
```

---

# 데이터 저장법

저장: 리스트(배열), 링크드리스트, 그래프

---

# 데이터 관리법

# 큐

: 맛집 1 2 3 4 5 6 7 줄을 서있으면 (first in first out) FIFO

콘서트 티켓팅

 

# 스택

: 1 2 3 4 5 6 7

7 먼저 출력 7 6 5 4 3 2 1 순으로 출력 (Last in First out) LIFO

웹브라우저 뒤로가기 버튼

---

- 그래프 탐색 방법 : DFS, BFS (리스트로 따지자면 for문 돌리는 것과 똑같음)

# DFS(깊이 우선탐색)

## 기본

```python
name = list(input().split())
arr = [[0,1,1,0,0,0],
       [0,0,0,1,1,0],
       [0,0,0,0,0,1],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0]]

answer = []
def dfs(now):
    global answer
    answer.append(name[now])
    for i in range(6):
        if arr[now][i] == 1:
            dfs(i)
    return # 리턴 안써도 이 코드는 돌아감. for문 끝나면 어차피 꺼지니까!

dfs(0) # 0번 인덱스부터 깊이 우선 탐색
print(answer)
```

## 경로탐색

```python
name=list(input().split())  # B A C D
arr=[
    [0,0,1,1],
    [1,0,1,0],
    [1,0,0,1],
    [0,0,0,0],
]
used=[0]*4
cnt=0
def dfs(now):
    global cnt
    if now==3:
        cnt+=1
    for i in range(4):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1
            dfs(i)
            used[i]=0

used[1]=1
dfs(1)
print(cnt)
```

---

## 연습문제

![](../../Downloads/Untitled.png)
출발점을 입력 받습니다.
입력받은 출발점 알파벳 부터  E 가 써있는곳 까지 갈 수 있는 방법이
몇가지 있는지 출력해 주세요.
A 입력시 3가지
D 입력시 1가지
B 입력시 3가지

```python
# 연습문제
name=['A','B','C','D','E']
st=input()
arr=[
    [0,1,0,0,0],
    [0,0,1,1,1],
    [1,0,0,1,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
used=[0]*5
cnt=0
def dfs(now):
    global cnt
    if name[now]=='E':
        cnt+=1
    for i in range(5):
        if arr[now][i]==1 and used[i]==0:
            used[i]=1
            dfs(i)
            used[i]=0

st_index=0
for i in range(5):
    if name[i]==st:
        st_index=i
        break
used[st_index]=1
dfs(st_index)
print(cnt)
```

## 연습문제

![](../../Downloads/Untitled1.png)

```python

name=['A','B','C','D','E']
st=input()  # 출발점 입력
arr=[
    [0,4,0,0,0],
    [0,0,1,2,9],
    [5,0,0,7,0],
    [0,0,0,0,1],
    [0,0,0,0,0],
]
used=[0]*5

Min=int(21e8)
def dfs(now,sum):
    global Min
    if name[now]=='E':
        # 최소 비용 (최소 sum)
        if sum<Min:
            Min=sum

    for i in range(5):
        if arr[now][i]>0:
            if used[i]==0:
                used[i]=1
                dfs(i,sum+arr[now][i])
                used[i]=0

# 출발점의 인덱스 확인
st_index=0
for i in range(5):
    if name[i]==st:
        st_index=i
        break

used[st_index]=1
dfs(st_index,0)
print(Min)
```