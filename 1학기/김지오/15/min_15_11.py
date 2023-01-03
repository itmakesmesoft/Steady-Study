a = [list(map(str, input())) for _ in range(4)]

cnt1 = 0
cnt2 = 0
for i in range(4):
    for j in range(len(a[i])):
        if a[i][j] =='A':
            cnt1 = 1
        if a[i][j] == 'B':
            cnt2 = 1

if cnt1 ==1 and cnt2 == 1:
    print("대발견")
elif cnt1 ==1 or cnt2 == 1:
    print("중발견")
if cnt1 == 0 and cnt2 == 0:
    print("미발견")




