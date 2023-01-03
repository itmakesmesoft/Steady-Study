m, n = map(str, input().split())

def main(p,q):
    a = getChar(p,q)
    print(a)

def getChar(p,q):
    if chr(ord(p))>chr(ord(q)):
        return p
    else:
        return q

main(m,n)