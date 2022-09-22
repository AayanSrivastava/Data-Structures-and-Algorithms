t=int(input())
ar=[]
c=0
while t:
    s=input()
    ar.append(s)
    t-=1
for i in ar:
    al=i.rfind('a')
    bl=i.find('b')
    af=i.find('a')
    bf=i.rfind('b')
    if abs(al-bl)==1 and abs(af-bf)==1 and (i.count('a')+i.count('b'))==len(i):
        c+=1
print(c)