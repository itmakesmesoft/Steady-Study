for tc in range(1, 11):
    dump_times = int(input())
    a = list(map(int, input().split()))

    for times in range(dump_times):
        MAX = 0
        MIN = 101
        for i in range(len(a)):
            if a[i]>MAX:
                MAX = a[i]
            if a[i]<MIN:
                MIN = a[i]

        for j in range(len(a)):
            if a[j]==MAX:
                a[j]-=1
                break

        for j in range(len(a)):
            if a[j]==MIN:
                a[j]+=1
                break

    print(f'#{tc} {max(a)-min(a)}')






