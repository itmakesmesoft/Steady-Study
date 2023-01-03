a = [['A','D','F'],
     ['Q','W','E'],
     ['Z','X','C']]

def main():
    o = input()
    find(o)


def find(o):
    global a
    for i in range(3):
        for j in range(3):
            if a[i][j] == o:
                print(f'{i},{j}')

main()