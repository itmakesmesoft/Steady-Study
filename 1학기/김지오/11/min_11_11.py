arr = [[1, 3, 6, 2],
       [4, 2, 4, 5],
       [6, 3, 7, 3],
       [1, 5, 4, 6]]

inp = int(input())
bigger_arr = []
for i in range(4):
    for j in range(4):
        if inp<arr[i][j]:
            bigger_arr.append(arr[i][j])

print(*bigger_arr)