def main():
    a = [3, 5, 1, 2, 7]
    b = list(map(int, input().split()))
    CompareGo(a, b)


def CompareGo(a, b):
    if a == b:
        print('두배열은완전같음')
    else:
        print('두배열은같지않음')


main()