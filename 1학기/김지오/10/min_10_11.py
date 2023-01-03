a =[]
for _ in range(4):
     a.append(list(map(int, input().split())))


for i in range(4):
     for j in range(4):
          if a[i][j] == 0:
               a[i][j] = '!'
          elif a[i][j]%2 == 0:
               a[i][j] = '#'
          else:
               a[i][j] = '@'

for i in range(4):
     for j in range(4):
          print(a[i][j], end ='')
     print()