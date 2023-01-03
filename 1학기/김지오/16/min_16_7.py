a = [list(input()) for _ in range(3)]

cnt = 0
for i in range(3):
    for j in range(len(a[i])):
        if a[i][j] == 'M':
            cnt +=1

if cnt>0: print("M이 존재합니다")
else: print("M이 존재하지 않습니다")