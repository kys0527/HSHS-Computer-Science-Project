#기본적인 큐
class Queue :
    def __init__(self) :
        self.items = []
    def enqueue(self, item) :
        self.items.insert(0,item)
    def dequeue(self) :
        return self.items.pop()
    def peek(self) :
        return self.items[0]
    def isEmpty(self) :
        return self.items == []
    def size(self) :
        return len(self.items)

class lens :
    def __init__(self, tp, focus, l):
        lens.tp = tp
        lens.focus = focus
        lens.l = l
        
total = Queue()
#구현할 렌즈의 정보 받기
n = int(input("렌즈의 개수는 몇개인가요?"))
for i in range(1, n + 1):
    tp = str(input("렌즈',i,'의 종류는 무엇인가요?(오목, 볼록 중 골라 주세요.)"))
    focus = int(input("렌즈',i,'의 초점거리(절댓값)는 얼마인가요?"))
    l = int(input("렌즈',i-1,'과 렌즈',i,'사이의 거리는 얼마인가요?(렌즈 0 은 물체 입니다.)"))
    a = lens(tp,focus,l)
    total.enqueue(a)
fl = total.dequeue()
sign = 1
if fl.tp == '오목' :
    sign = -1
a = fl.l
f = fl.focus
inb = sign/f - 1/a
b = round(1/inb,2)
m = round(-1/(inb*l),2)
for i in range(2,n+1):
    sign = 1
    if fl.tp == '오목' :
        sign = -1
    fl = total.dequeue()
    a = fl.l - b
    f = fl.focus
    inb = sign/f - 1/a
    b = round(1/inb,2)
    m = m * round(-1/(inb*l),2)
M = round(m,2)
flag = '도립(뒤집어져있음)'
if m > 0:
    flag = '정립(똑바로 서있음)'
print('상의 위치는',n,'번째 렌즈로부터',b,'의 거리에 있으며, 배율은',M,'배입니다. 상은',flag,'입니다.') 
