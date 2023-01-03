a = list(map(int, input().split()))

MAX = 0
MIN = 9999
for i in range(len(a)):
    if a[i]>MAX:
        MAX = a[i]
    if a[i]<MIN:
        MIN  = a[i]

print(f'MAX={MAX}')
print(f'MIN={MIN}')