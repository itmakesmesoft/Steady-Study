a1= list(map(str, input()))
a2= list(map(str, input()))

cnt = 0
for i in range(len(a1)):
    if len(a1)== len(a2) and a1[i]==a2[len(a1)-1 -i]:
        cnt +=1

if cnt == len(a1):
    print("거울문장")
else:
    print("거울문장아님")