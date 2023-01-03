T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    bucket = [0]*(N+1)

    for i in range(M):
        bucket[arr[i]] =1

    cnt = 0 #몇번만에 도달했는지

    def rcr(now):
        global cnt

        if now>=N-K:
            return

        flg = 0
        for i in range(K, 0, -1):
            if bucket[now+i]==1:
                cnt+=1
                flg = 1
                rcr(now+i)
                break
        if flg == 0:
            cnt = 0
            return



    rcr(0)
    print(f'#{tc} {cnt}')

