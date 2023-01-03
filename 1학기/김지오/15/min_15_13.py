a = [['D','A','T','A','W'],
     ['B','B','Q','K']]

n = int(input())

if n%2 == 1:
    for i in range(len(a[0])-1):
        for j in range(i, len(a[0])):
            if ord(a[0][i])> ord(a[0][j]):
                a[0][i],a[0][j] = a[0][j],a[0][i]

if n%2 == 0:
    for i in range(len(a[1])-1):
        for j in range(i, len(a[1])):
            if ord(a[1][i])> ord(a[1][j]):
                a[1][i],a[1][j] = a[1][j],a[1][i]




for i in range(2):
    for j in range(len(a[i])):
        print(a[i][j], end='')
    print()

