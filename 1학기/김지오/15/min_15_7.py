a = ['A','B','C','Z','E','T','Q']
# a=list('ABCZETQ')

blacklist = list(map(str, input()))

for i in range(5):
    cnt=0
    for j in range(7):
        if blacklist[i] == a[j]:
            cnt +=1
    if cnt == 1:
        print(f'{blacklist[i]}=마을사람')
    else:
        print(f'{blacklist[i]}=외부사람')
