# n, k = map(int, input().split())
#
# coin = [int(input()) for _ in range(n)]
# coin.sort(reverse=True)
# cnt = 0
# while k != 0:
#     for i in coin:
#         if k - i >= 0:
#             k -= i
#             cnt += 1
#             break
#
# print(cnt)


# N, K = map(int, input().split())
# coin_lst = list()
# for i in range(N):
#     coin_lst.append(int(input()))
#
# count = 0
# for i in reversed(range(N)):
#     count += K // coin_lst[i]     # 카운트 값에 K를 동전으로 나눈 몫을 더해줌
#     K = K % coin_lst[i]           # K는 동전으로 나눈 나머지로 계속 반복
#
# print(count)

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
cnt = 0
for i in range(n):
    cnt += k // coin[i]
    k = k % coin[i]
print(cnt)