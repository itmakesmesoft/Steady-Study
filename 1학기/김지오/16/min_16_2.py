t = [['A', 'B', 'K', 'T'],
     ['K', 'F', 'C', 'F'],
     ['B', 'B', 'Q', 'Q'],
     ['T', 'P', 'Z', 'F']]

a, b = map(str, input().split())

cnt = 0
for i in range(4):
    for j in range(4):
        if t[i][j] == a or t[i][j]==b:
            cnt +=1

print(cnt)