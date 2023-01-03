# def input1():
#     return int(input())
#
#
# def main():
#     a = input1()
#     b = input1()
#     c = input1()
#     print(calc(a, b, c))
a, b, c = map(int, input().split())

def calc(m, n, p):
    return m + n + p


print(calc(a, b, c))

#파이썬으로 못푼다
