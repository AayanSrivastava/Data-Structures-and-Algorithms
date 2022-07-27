from  datetime import date
s=input()
s=list(s)
y=s[:4]
m=s[5:7]
d=s[8:]
y=int(''.join(y))
m=int(''.join(m))
d=int(''.join(d))
weeks={1:'MONDAY',2:'TUESDAY',3:'WEDNESDAY',4:'THURSDAY',5:'FRIDAY',6:'SATURDAY',7:'SUNDAY'}
w=date.isoweekday(date(y,m,d))
print(weeks[w])