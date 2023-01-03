s, t = map(int, input().split())

def main(a, b):
    if int(a/b) % 2 == 0:
        even(int(a/b))
    else:
        odd(int(a/b))
    printData(a+b)

def even(a1):
    m = (a1)*2
    printData(m)

def odd(a2):
    n = (a2)-10
    printData(n)

def printData(k):
    print(k)


main(s,t)