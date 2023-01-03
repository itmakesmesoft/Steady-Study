a = [list(map(str, input())) for _ in range(5)]

max_len = 0
maxi = ''
for i in range(5):
    if len(a[i])>max_len:
        max_len = len(a[i])
        maxi = a[i]

for i in range(max_len):
    print(maxi[i], end ='')