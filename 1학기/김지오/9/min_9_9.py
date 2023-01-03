l = [['F','E','W'],
     ['D','C','A']]

t= input()
def main(s):
    findCh(s)

def findCh(s):
     global l
     cnt = 0
     for i in range(2):
          for j in range(3):
               if s == l[i][j]:
                    cnt +=1

     if cnt>0:
          print('발견')
     else:
          print('미발견')

main(t)