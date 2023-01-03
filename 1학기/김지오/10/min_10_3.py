n= int(input())
m= input()

def main(p, q):
    kfc(p, q)

def kfc(p, q):
    a = chicken(p)
    b = coke(q)
    print(f'{a}{b}')

def chicken(p):
    return p+10


def coke(q):
    return q


main(n, m)
