arr = [list(input()) for _ in range(2)]
# print(arr)

cnt = 0
shorter = 0
a =0
if len(arr[0])>len(arr[1]):
    a = len(arr[0])-len(arr[1])
    shorter = 1
else:
# elif len(arr[0])<len(arr[1]):
    a = len(arr[1])-len(arr[0])
    shorter = 0

for j in range(len(arr[shorter])):
    if arr[0][j] != arr[1][j]:
        cnt +=1

print(cnt+a)
