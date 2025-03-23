arr=[11,14,16,10,9,8,24,5,4,3]
sum1=0
for i in arr:
    while i>0:
        sum1+=i%10
        i=i//10
f1=sum1%10
f2=sum(arr)%10
print(f1-f2)