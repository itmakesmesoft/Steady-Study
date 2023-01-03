arr = ['D','A','T','A','P','O','W','E','R']
a, b = map(int, input().split())
arr2 = ['' for _ in range(9)]

for i in range(b-a+1):
    arr2[i] = arr[a+i]
    print(arr2[i], end = '')