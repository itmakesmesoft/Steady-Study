s = input()
index1 = int(input())

for i in range(len(s)):
    if i == index1:
        s= s.replace(s[i], '')
    else:
        continue
print(s)