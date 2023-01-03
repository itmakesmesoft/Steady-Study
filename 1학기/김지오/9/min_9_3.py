a = ['A', 'F', 'G', 'A', 'B', 'C']
m, n = map(str, input().split())

count1 = 0
count2 = 0
for i in range(len(a)):
    if a[i] == m:
        count1 +=1
    if a[i] == n:
        count2 +=1

if count1>0 and count2>0:
    print('와2개')
elif count1==0 and count2==0:
    print('우0개')
else:
    print('오1개')