arr = ['M','I','N','Q','U','E','S','T']
m = input()
n = input()
q = input()

def main(a,b,c):
    length(a)
    length(b)
    length(c)

def length(k):
    global arr
    for i in range(len(arr)):
        if arr[i]==k:
            print(f'{k}={i}')

main(m, n, q)