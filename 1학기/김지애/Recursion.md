# Recursion

[자주 틀리는 문제](https://www.notion.so/1bf4fa363aac41048d9d1fff491d1f07)

# 누적합

---

### 누적합_전역변수

```python
arr = [3, 4, 5, 1, 6, 9]
sum = 3
def abc(level):
    global sum
    if level == 5:
        print(sum)
        return
    print(sum)
    sum += arr[level+1]
    abc(level+1)
abc(0)
```

| sum | level |
| --- | --- |
| 3 | 0 |
| 7 | 0 |
| 12 | 1 |
| 13 | 2 |
| 19 | 3 |
| 28 | 4 |
| return | 5 |
| 28 | 4 |
| 28 | 3 |
| 28 | 2 |
| 28 | 1 |
| 28 | 0 |

### 누적합_매개변수

```python
arr = [3, 4, 5, 1, 6, 9]
def abc(level, sum):
		# print(sum)
    if level == 5:
        print(sum) # print를 밑에하면 마지막 sum이 출력이 안되니까
        return
    print(sum)
    abc(level+1,sum+arr[level+1])

abc(0, 3) # level sum
```

### 누적합 리턴_전역변수

```python
arr = [3, 4, 5, 1, 6, 9]
# 3 7 12 13 19 28
# 전역변수 : 리턴되어 나올 때 28 28 28 ...
sum = 3
def abc(lev):
    global sum
    print(sum)
    if lev == 5:
        return
    sum += arr[lev+1]
    abc(lev+1)

abc(0)
```

### 누적합 리턴_매개변수

```python
arr = [3, 4, 5, 1, 6, 9]
# 3 7 12 13 19 28
# 매개변수 : 리턴되어 나올 때 28 19 13 ...
def abc(lev, sum):
    print(sum)
    if lev == 5:
        return
    abc(lev+1, sum+arr[lev+1])

abc(0, 3)
```

### 카드묶음_전역변수

```python
# 3개의 카드 묶음에서 1장씩 뽑았을때
# 나올 수 있는 모든 합들을 출력해 주세요

arr = [3, 7, 1, 5]
# 4장의 카드 : brunch = 4
# 3묶음 : level = 3

sum = 0
def abc(level):
    global sum
    if level == 3:
        print(sum, end=' ')
        return
    for i in range(4):
        sum += arr[i]
        abc(level+1)
        sum -= arr[i] # 전역변수의 경우 sum 값이 저장되기 때문에 꼭 빼줘야 함

abc(0)
```

### 카드묶음_매개변수

```python
# 3개의 카드 묶음에서 1장씩 뽑았을때
# 나올 수 있는 모든 합들을 출력해 주세요

arr = [3, 7, 1, 5]
# 4장의 카드 : brunch = 4
# 3묶음 : level = 3

def abc(level, sum):
    if level == 3:
        print(sum, end=' ')
        return
    for i in range(4):
        abc(level+1, sum+arr[i])

abc(0, 0)
```

### 개구리 위치

```python
arr = [2, 0, 1, 1, 3, 5, 1]

def abc(lev):
    if lev == 7:
        return
    abc(lev + arr[lev])
    print(arr[lev])

abc(0)

# 3 1 1 2
```

### 누적합 10이상 count

```python
arr = [4, -7, 1, 3]
cnt = 0
def abc(lev, sum):
    global cnt
    if lev == 4:
        if sum > 10:
            cnt += 1
        return
    for i in range(4):
        abc(lev+1, sum+arr[i])

abc(0, 0)
print(cnt)
```

### 최소동전사용개수

![Untitled](Recursion%20eb0c5b9a22d64e46924e6ce4c0c3c230/Untitled.png)

```python
'''
input : 140 
output : 2
'''

change = int(input()) 
coin = [100, 70, 10]
# level = ?
# brunch = 3

Min = int(21e8)
def abc(level, change):
    global Min
    if change < 0:
        return
    if change == 0:
        if level < Min:
            Min = level
        return
    for i in range(3):
        abc(level+1, change-coin[i])

abc(0, change)
print(Min)
```

### 재귀 경로 출력하기

```python
'''
level = 2
brunch = 3
'''

arr = ['a', 'b', 'c']
path = [''] * 2

def abc(level):
    if level == 2:
        for i in range(2):
            print(path[i], end=' ')
        print() # indent 조심
        return
    for i in range(3):
				# 현 level을 index로 하는 path 배열에 다음 level에 나올 값(arr[i]) 저장
        path[level] = arr[i]
        abc(level+1)
        path[level] = ''  # 생략가능

abc(0)
```

# 순열

---

### 주사위 경로 중복순열

```python
n = int(input())
arr = [1, 2, 3, 4, 5, 6]
path = [0] * n

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end=' ')
        print()
        return
    for i in range(6):
        path[level] = arr[i]
        abc(level+1)

abc(0)
```

### 주사위 경로 순열 (금은동)

```python
n = int(input())
path = [0] * n # level
arr = [1, 2, 3, 4, 5, 6]
used = [0] * 6 # index 0~5 # brunch

def abc(level):
    if level == n:
        for i in range(n):
            print(path[i], end=' ')
        print() # for문 끝나고 new line
        return
    for i in range(6):
        if used[i] == 1: continue # i(0~5)를 사용했으면 다음 i로 넘어가기
        path[level] = arr[i]
        used[i] = 1 # insert # i(0~5)를 사용했으면 체크 # 숫자든 문자든 상관없음
        abc(level+1)
        **used[i] = 0 # delete # 반드시 있어야 함**

abc(0)
```

### 제외 (C 로 시작하는 경로 삭제)

```python
'''
경로삭제
1. 함수 들어가기 전
2. 함수 들어간 후
'''

# level = 4
# brunch = 4
arr = ['A', 'B', 'C', 'D']
path = [''] * 4

def abc(level):
    # if level == 1 and path[level-1] == 'C': return # 2
    if level == 4:
        for i in range(4):
            print(path[i], end='')
        print()
        return
    for i in range(4):
        # if level == 0 and arr[i] == 'C': continue # 1
        path[level] = arr[i] # 다음 level의 value 를 넣어주기
        abc(level+1)

abc(0)
```

### 제외 (B가 포함된 경로 삭제)

```python
'''
경로삭제
1. 함수 들어가기 전
2. 함수 들어간 후
'''

# level = 4
# brunch = 4
arr = ['A', 'B', 'C', 'D']
path = [''] * 4

def abc(level):
    # if level > 0 and path[level-1] == 'B': return # 2 # out of range 처리
    if level == 4:
        for i in range(4):
            print(path[i], end='')
        print()
        return
    for i in range(4):
        # if i == 1: continue # 1
        # if arr[i] == 'B': continue # 1
        path[level] = arr[i]
        abc(level+1)

abc(0)
```

### 제외 (연속된 문자가 같은 경로 삭제)

```python
'''
경로삭제
1. 함수 들어가기 전
2. 함수 들어간 후
'''

# level = 4
# brunch = 4
arr = ['A', 'B', 'C', 'D']
path = [''] * 4

def abc(level):
    # if level > 1 and path[level-1] == path[level-2]: return # 2 # out of range 처리
    if level == 4:
        for i in range(4):
            print(path[i], end='')
        print()
        return
    for i in range(4):
        # if level > 0 and path[level-1] == arr[i]: continue # 1 # out of range 처리
        path[level] = arr[i]
        abc(level+1)

abc(0)
```

# 조합

---

![Untitled](Recursion%20eb0c5b9a22d64e46924e6ce4c0c3c230/Untitled%201.png)

### path 배열안에 문자를 비교하면서 조합을 출력하는 방법

```python
arr = ['a', 'b', 'c', 'd']
path = [''] * 3

def abc(level):
    if level == 3:
        for i in range(3):
            print(path[i], end='')
        print()
        return

    for i in range(4):
        #1 path[level-1] -> 전단계에 들어간 경로값
        #2 arr[i] -> 앞으로 들어갈 경로값
        #3 전단계에 들어간 경로값 < 앞으로 들어갈 경로값 : True
        if level > 0 and path[level-1] >= arr[i]: continue
        path[level] = arr[i]
        abc(level+1)

abc(0)
```

### for문의 i값의 변화를 이용한 조합 출력하기

```python
arr=['a','b','c','d']
path=['']*3

def abc(level,start):
    if level==3:
        for i in range(3):
            print(path[i],end='')
        print()
        return

    for i in range(start,4):
        path[level]=arr[i]
        abc(level+1,i+1)

abc(0,0)  #level start
```

### 중복조합

```python
arr=['a','b','c','d']
path=['']*3

def abc(level,start):
    if level==3:
        for i in range(3):
            print(path[i],end='')
        print()
        return

    for i in range(start,4):
        path[level]=arr[i]
        abc(level+1,i)

abc(0,0)  #level start
```