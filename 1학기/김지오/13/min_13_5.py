a = list(input())

def main(k):
    KFC(k)

def KFC(k):
    upper_count = 0
    lower_count = 0
    for i in range(len(k)):
        if k[i].isupper() ==True:
            upper_count +=1
        else:
            lower_count +=1

    print(f'대문자{upper_count}개')
    print(f'소문자{lower_count}개')

main(a)