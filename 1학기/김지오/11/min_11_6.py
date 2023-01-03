a = [3, 4, 1, 3, 2, 7, 3]
n = int(input())
number1 = 0
flag=0
while number1<7:
    if n == a[number1]:
        flag=1
        break
    number1 += 1
if flag==1:
    print('발견')
else:
    print('미발견')