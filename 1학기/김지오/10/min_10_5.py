n = int(input())

l1 = [[9, 6, 3],
      [8, 5, 2],
      [7, 4, 1]]
l2 = [[7, 8, 9],
      [4, 5, 6],
      [1, 2, 3]]
l3 = [[10, 13, 16],
      [11, 14, 17],
      [12, 15, 18]]

if n%5 ==1:
    for i in range(3):
        for j in range(3):
            print(l1[i][j], end = ' ')
        print()

elif n%5 ==2:
    for i in range(3):
        for j in range(3):
            print(l2[i][j], end = ' ')
        print()

else:
    for i in range(3):
        for j in range(3):
            print(l3[i][j], end = ' ')
        print()
