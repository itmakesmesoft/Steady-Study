## Union Find

: 각각의 독립된 data를 그룹화 시켜 자료들을 관리할 때 사용하는 자료구조이다.

#### 필요 코드

1\. 그룹화 진행 코드: union 함수

2\. 문자 2개 입력받아서 같은 그룹인지 확인해주는 코드: findboss 함수

```
arr = [0]*200

def findboss(member):
    # arr[ord(member] : member의 상사
    global arr
    if arr[ord(member)] == 0: # member의 상사가 없음 => 자신이 보스
        return member # 자신을 리턴
    ret = findboss(arr[ord(member)]) # 자신이 보스가 아니면, 자신의 상사의 상사를 찾아봄 
    return ret


# 두 그룹을 하나의 그룹으로 합쳐주는 함수
def union(a,b):
    global arr
    a_boss, b_boss = findboss(a), findboss(b) # 보스 찾기 먼저
    if a_boss == b_boss: # 이미 같은 그룹 / 합칠 필요 없음
        return
    arr[ord(b_boss)] = a_boss # b_boss자리에 a_boss를 넣어줌



union('A', 'B') # 두 그룹을 하나의 그룹으로 합쳐주는 함수
union('D', 'E')
union('B', 'E')
union('B', 'D')
union('F', 'E')

y, x = input().split()
if findboss(y) == findboss(x):
    print('같은 그룹')
else:
    print('다른 그룹')
```

※ 참고: 위와 똑같은 코드인데, 효율성을 좀 더 높임

def findboss(member):  
      global arr  
      if arr\[ord(member)\] == 0:  
           return member  
      ret = findboss(arr\[ord(member)\])

      **arr\[ord(member)\] = ret**

      # 추가 코드 / 상위 보스로 갱신해줌 / 다음에 boss를 찾으려 많이 올라가지 않아도 됨 - 경로 단축 (효율성을 높이는 코드)  
            return ret

※ 참고

정점 n개일 때,

정점을 모두 잇는 최소 간선의 개수: n-1

#### ※ 응용

union find를 통해 사이클 존재 여부를 확인할 수 있다. 

findboss 해서 같은 boss 면 이미 같은 그룹인데 연결하는 것이므로 사이클 형성됨

```
n = int(input()) # 간선의 개수
edge = []
for _ in range(n):
    edge.append(input().split())

arr = [0]*200


def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    else:
        ret = findboss(arr[ord(member)])
        return ret


def union(a, b):
    global arr
    if findboss(a) == findboss(b):
        return 1
    arr[ord(findboss(b))] = findboss(a)


flag = 0
for i in range(n):
    a, b = edge[i]
    ret = union(a,b)
    if ret == 1:
        flag = 1
        break
if flag:
    print('cycle 발견')
else:
    print('cycle 미발견')
```