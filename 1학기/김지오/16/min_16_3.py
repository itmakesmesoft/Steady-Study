a = list(input())
b = int(input())
a.insert(b, "A")

result = ''
for i in a:
    result += i
print(result)