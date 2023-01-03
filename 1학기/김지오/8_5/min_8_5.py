l1, l2, n = map(str, input().split())
n1 = int(n)
l11 = ord(l1)
l21 = ord(l2)

al = []
for i in range(l11, l21+1):
    al.append(chr(i))
    b = ''.join(al)

for n in range(n1):
    print(b)


