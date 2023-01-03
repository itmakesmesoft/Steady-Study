T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    a = list(map(int, input().split()))

    array_bucket=[]
    for i in range(n):
        bucket = [0] * max(a)
        for j in range(a[i]):
            bucket[j] += 1
        array_bucket.append(bucket)
    print(array_bucket)

    # bucket1 = [0] * (n + 1)
    # for y in range(n):
    #     for x in range(n):
    #         bucket1[x] +=array_bucket[y][x]
    # print(bucket1)
    #
    # min = 999999
    # for s in range(1, n+1):
    #     if bucket1[s] != 0:
    #         if bucket1[s] <min:
    #             min = bucket1[s]
    #
    # print(f'#{tc} {n-min}')

    MAX = 0
    for i in range(n):
        for j in range(max(a)):
            if array_bucket[i][j]==1:
                cnt=0
                for k in range(n-1, i, -1):
                    if array_bucket[k][j]==0:
                        cnt +=1
                    else: cnt +=0

                    if cnt>MAX:
                        MAX = cnt
            else:
                continue


    print(f'#{tc} {MAX}')