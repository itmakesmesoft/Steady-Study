arr = [[0 for _ in range(5)] for _ in range(5)]
n, ltr = map(str, input().split())
n1 = int(n)
for i in range(5):
    for j in range(5):
        arr[n1-1][j] = chr(ord(ltr)+4-j)
        print(arr[i][j], end='')
    print()
