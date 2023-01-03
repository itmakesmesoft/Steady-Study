a = [[0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0]
     ]

p, q = map(str, input().split())

for i in range(3):
     for j in range(6):
          if j<4:
               a[i][j] = p
          else:
               a[i][j] = q
          print(a[i][j], end='')
     print()