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
        self.tp = tp
        self.focus = focus
        self.l = l
total = Queue()
print('렌즈의 개수는 몇개인가요?')
n = int(input())
print('렌즈 1의 종류는 무엇인가요?(오목, 볼록 중 골라 주세요.)')
tp = str(input())
print('렌즈1의 초점거리(절댓값)는 얼마인가요?')
focus = int(input())
print('물체와 렌즈사이의 거리는 얼마인가요?')
l = int(input())
if tp == '볼록' and l == focus:
    print('해당 조건에서는 상이 생기지 않습니다. 렌즈의 초점거리나 물체와의 거리를 조절해 주세요')
    print('렌즈1의 초점거리(절댓값)는 얼마인가요?')
    focus = int(input())
    print('물체와 렌즈사이의 거리는 얼마인가요?')
    l = int(input())
a = lens(tp,focus,l)
total.enqueue(a)
for i in range (2,n + 1):
    print('렌즈',i,'의 종류는 무엇인가요?(오목, 볼록 중 골라 주세요.)')
    tp = str(input())
    print('렌즈',i,'의 초점거리(절댓값)는 얼마인가요?')
    focus = int(input())
    print('렌즈',i-1,'과 렌즈',i,'사이의 거리는 얼마인가요?')
    l = int(input())
    a = lens(tp,focus,l)
    total.enqueue(a)
fl = total.dequeue()
sign = 1
if fl.tp == '오목' :
    sign = -1 
a = fl.l
f = fl.focus
inb = sign/f - 1/a
b = 1/inb
B = round(b,2)
m = - 1 / inb / a
c=1
for i in range(1,n):
    fl = total.dequeue()
    sign = 1
    if fl.tp == '오목' :
        sign = -1
    a = fl.l - b
    f = fl.focus
    if sign ==1 and a==f:
        c=0
        break
    inb = sign/f - 1/a
    b = 1/inb
    B = round(b,2)
    m = m * (- 1 / inb / a)
    
if c ==1:
    M = round(m,2)
    flag = '도립(뒤집어져있음)'
    if m > 0:
        flag = '정립(똑바로 서있음)'
    print('상의 위치는',n,'번째 렌즈로부터',B,'의 거리에 있으며, 배율은',M,'배입니다. 상은',flag,'입니다.') 
else:
    print('해당 조건에서는 상이 생길수 없는 경우가 포함되어 있습니다.\n렌즈의 초점거리나 물체와 렌즈들 사이의 거리를 조절한 후 다시 실행해 보세요')
