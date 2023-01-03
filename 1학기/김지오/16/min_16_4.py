A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(4):
    print(f'{A[i]+B[3-i]}', end = ' ')