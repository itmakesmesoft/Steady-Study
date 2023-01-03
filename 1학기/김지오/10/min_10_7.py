n1, n2 = map(int, input().split())
n3, n4 = map(int, input().split())

def main(no1, no2, no3, no4):
    a = GOP(no1, no2)
    b = SUM(no3, no4)
    if a>b:
        print("GOP>SUM")
    elif a < b:
        print("GOP<SUM")
    else:
        print("GOP==SUM")



def GOP(m, n):
    return m*n

def SUM(p,q):
    return p+q


main(n1, n2, n3, n4)
