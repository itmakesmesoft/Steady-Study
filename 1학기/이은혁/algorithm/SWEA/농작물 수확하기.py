t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    mid = n//2
    total = 0
    for i in range(n):
        for j in range(n):
            if i<mid: # 행이 mid보다 작은 경우
                if mid-(i%mid)<=j and j<=mid+(i%mid): 
                    total += int(arr[i][j])
            elif i==mid: # 행이 mid와 같은 경우
                total += int(arr[i][j])
            elif i>mid: # 행이 mid보다 큰 경우
                if i-mid<=j and j<=n-(i-mid)-1:
                    total += int(arr[i][j])
    print(f'#{case} {total}')


'''
    for t in range(1,int(input())+1):
    N = int(input())
    lst = [list(map(int, list(input()))) for _ in range(N)]

    value = N // 2
    sumV = 0

    for i in range(value+1):
        for j in range(value-i, value+1+i):
            sumV += lst[i][j]
            if i != value:
                sumV += lst[N-1-i][j]

    print(f'#{t} {sumV}')
'''