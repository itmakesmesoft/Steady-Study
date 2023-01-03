a, b = map(int, input().split())
cnt = 0
while a<100 or b<100:
    a += 1
    b += 1
    cnt += 1

    # if a<=100 or b<=100:
    #     break


print(cnt)