arr = list(map(str, input()))
find1 = input()
find2 = input()
find3 = input()

def main(n1, n2, n3):
    findMe(n1)
    findMe(n2)
    findMe(n3)

def findMe(k):
    global arr
    cnt = 0
    for i in range(len(arr)):
        if k== arr[i]:
            cnt +=1
    print(f'{k}={cnt}')

main(find1, find2, find3)