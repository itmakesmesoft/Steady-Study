t = int(input())
for case in range(1, t+1):
    p, a, b = map(int, input().split())
    res = []
    for target in [a, b]:
        start = 1
        end = p
        cnt=1
        while True:
            mid = (start + end)//2
            if mid==target:
                break
            elif mid>target:
                end=mid
            else:
                start=mid
            cnt+=1
        res.append(cnt)
    result = (res[0]<res[1])*"A"+(res[0]>res[1])*"B"+(res[0]==res[1])*'0'
    print(f'#{case} {result}')