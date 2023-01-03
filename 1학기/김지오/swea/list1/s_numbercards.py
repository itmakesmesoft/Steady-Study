T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    bucket = [0]*10

    for i in range(N):
        bucket[arr[i]] +=1

    MAX = 0
    MAX_idx = 0
    for j in range(len(bucket)):
        if bucket[j]>=MAX:
            MAX = bucket[j]
            MAX_idx = j



    print(f'#{tc} {MAX_idx} {MAX}')
