# 190516, 렌즈 1개와 물체 1개에 대한 렌즈 방정식을 계산하는 프로그램
# Minimum Viable Product
print('렌즈의 종류는 무엇인가요?(오목, 볼록 중 골라 주세요.)')
tp = str(input())
print('렌즈의 초점거리(절댓값)는 얼마인가요?')
focus = int(input())
print('렌즈는 물체로부터 얼마나 떨어져있나요?(물체가 왼쪽, 렌즈가 오른쪽에 있는 경우)')
l = int(input())
sign = 1
if tp == '오목':
    sign == -1
else :
    sign = 1
inb = (1/focus) - (1/l)
lim = round(l + (1/inb),2)
m = -1/(inb*l)
if m<0 :
    print('물체의 상은 물체로부터',lim,'만큼 떨어져있으며, 배율은',-m, '입니다. 상은 도립(뒤집어져있음) 입니다.')
elif m>0 :
    print('물체의 상은 물체로부터',lim,'만큼 떨어져있으며, 배율은',m, '입니다. 상은 정립(똑바로 서있음)입니다.') 


