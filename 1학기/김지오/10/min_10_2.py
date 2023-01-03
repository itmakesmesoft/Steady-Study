# n = int(input())
#
# arr=[]
# if n%2 ==0:
#     for i in range(4):
#         arr.append([])
#         for j in range(4):
#             arr[i].append(0)
#             if i==j:
#                 arr[i][j] = i+1
#
#
# if n%2 !=0:
#     for i in range(4):
#         arr.append([])
#         for j in range(4):
#             arr[i].append(0)
#             if i == 3-j:
#                 arr[i][j] = i+1
#
# for i in range(4):
#     for j in range(4):
#         print(arr[i][j], end=' ')
#     print()

arr = [[0]*4 for _ in range(4)]
print(arr)