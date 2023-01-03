a = 'StructPointer'
b= []
for i in range(len(a)):
    b.append(a[i])

findMe = input()

cnt = 0
for i in range(len(b)):
    if findMe== b[i]:
        cnt += 1

if cnt != 0:
    print('발견')
else:
    print('미발견')
