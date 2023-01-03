n = [3, 4, 2, 5, 7, 9]
a, b = map(int, input().split())
n[a], n[b] = n[b], n[a]

for i in range(len(n)):
    print(n[i], end= ' ')
