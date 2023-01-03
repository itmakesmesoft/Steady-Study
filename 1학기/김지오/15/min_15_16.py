
a = input()

# 00 01 02
# 10 11 12
# 20 21 22

arr = [['' for _ in range(3)] for _ in range(3)]
# arr = [['']*3 for _ in range(3)]
cnt = 0
y =0

while y<3:
    x =0
    while x<3:
        if x<=y:
            arr[2-y][x] = chr(ord(a)+cnt)
            cnt +=1
        x+=1
    y+=1

for i in range(3):
    for j in range(3):
        print(arr[i][j], end='')
    print()