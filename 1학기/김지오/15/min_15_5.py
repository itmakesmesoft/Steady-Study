n1= list(map(str, input()))
n2= list(map(str, input()))
n3= list(map(str, input()))
n4= list(map(str, input()))

a = [n1, n2, n3, n4]
b = []

for i in range(4):
    b.append(len(a[i]))


for i in range(3):
    for j in range(i, 4):
        if b[i]>b[j]:
            b[i],b[j] = b[j], b[i]

for k in range(4):
    print(b[k], end = ' ')