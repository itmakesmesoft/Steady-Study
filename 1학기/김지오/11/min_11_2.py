m, n = map(int, input().split())

def Sum1(a, b):
    return a+b

def comp(a, b):
    return a-b

def print1(a, b):
    print(f'합:{Sum1(a,b)}')
    print(f'차:{comp(a,b)}')

Sum1(m, n)
comp(m, n)
print1(m, n)
