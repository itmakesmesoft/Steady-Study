n = list(map(str, input().split()))

def checkChar(k):
    for i in range(len(k)):
        if k[i].isupper() == True:
            print('대', end='')
        else:
            print('소', end='')

checkChar(n)