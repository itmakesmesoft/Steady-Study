a = list(map(str, input()))

cnt =0
for i in range(len(a)):
    if i%2 == 1 and a[i].isupper() == False:
            cnt += 1
    elif i%2 == 0 and a[i].isupper() == True:
            cnt +=1

if cnt == len(a):
    print("개구리문장")
else:
    print("일반문장")