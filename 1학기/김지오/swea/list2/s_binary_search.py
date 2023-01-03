T = int(input())



def findpage(page_i_want):
    start = 1
    end = P
    cnt = 0

    while True:
        mid = (start+end)//2
        if mid==page_i_want:
            cnt+=1
            return cnt

        elif mid>page_i_want:
            cnt+=1
            end = mid
            continue

        elif mid<page_i_want:
            cnt+=1
            start = mid
            continue

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    if findpage(A)<findpage(B):
        print(f'#{tc} A')
    elif findpage(A)==findpage(B):
        print(f'#{tc} 0')
    else:
        print(f'#{tc} B')


