hrs=input('enter hour')
h=float(hrs)
rate=input('enter rate')
r=float(rate)
if h<=40:
    pay=r*h
    print(pay)
else:
    pay=40*r+(h-40)*r*1.5
    print(pay)
