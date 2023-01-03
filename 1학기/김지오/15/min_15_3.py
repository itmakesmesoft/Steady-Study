a = list(map(int, input().split()))
cnt = 0
for i in range(1, 6):
    if abs(a[i-1]-a[i]) < 3:
        cnt +=1

if cnt ==5:
    print("완벽한배치")
else:
    print("재배치필요")