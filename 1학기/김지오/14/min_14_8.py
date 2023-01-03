a = list(map(str, input()))
for i in range(len(a)-1):
    for j in range(i, len(a)):
        if ord(a[i]) > ord(a[j]):
            a[i], a[j] = a[j], a[i]

for k in range(len(a)):
    print(a[k], end = '')
