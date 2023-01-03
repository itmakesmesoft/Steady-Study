a= list(map(str,input().split()))
b = []
for i in range(len(a)):
    b.append(chr(ord(a[i])+1))

print(*b)


