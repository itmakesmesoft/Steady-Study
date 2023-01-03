n, m = map(int, input().split())
def main(a, b):
    bbq(a, b)


def bbq(a,b):
    print(f'합:{a+b}')
    print(f'차:{a-b}')
    print(f'곱:{a*b}')
    print(f'몫:{round(a/b)}')

main(n, m)