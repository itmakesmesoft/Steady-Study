inp = int(input())

def main(k):
    countdown(k)

def countdown(k):
    if k == 0:
        return
    print(k, end = ' ')
    countdown(k-1)

main(inp)