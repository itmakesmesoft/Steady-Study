a, b = map(int, input().split())

while a <= b:
    for i in range(a, b+1):
        print(i, end = ' ')
    break
