g = [3, 2, 6, 2, 4, 1, 4, 2, 6, 5]
target = int(input())
def main(k):
    KFC(target)


def KFC(target):
    global g
    cnt = 0
    for i in range(len(g)):
        if g[i] == target:
            cnt +=1

    if cnt>0:
        print("값이 존재합니다")
    else:
        print("값이 없습니다")

main(target)