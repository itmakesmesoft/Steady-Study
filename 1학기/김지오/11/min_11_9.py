a = input()
b = []
for i in range(len(a)):
    b.append(a[i])

big = ''
small = ''

for i in range(len(b)):
    if b[i].isupper() == True:
        big += b[i]
    elif b[i].islower() == True:
        small+= b[i]

print(f'big={big}')
print(f'small={small}')