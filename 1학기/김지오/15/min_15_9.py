a = "BBQWORLD"
b = "KFCAPPLE"
c = "LOT"
l1 = [a, b, c]
n = input()

cnt = 0
for i in range(3):
    for j in range(len(l1[i])):
        if l1[i][j] == n:
            cnt += 1

print(cnt)