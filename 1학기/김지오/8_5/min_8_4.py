list_2 = []
first, second, third = map(str, input().split())

for i in range(17):
    if i>=0 and i<7:
        list_2.append(first)
    elif i >=7 and i<13:
        list_2.append(second)
    else:
        list_2.append(third)
# print(list_2)

for j in range(16, -1, -1):
    print(list_2[j], end='')