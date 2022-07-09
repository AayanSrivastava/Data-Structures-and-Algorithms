#include<stdio.h>
int main()
{
    int t,e,g,f,p;
    long long d,n,k;
    scanf("%d",&t);
    while(t--)
    {
        g=0,e=0,f=0;
    scanf("%lld",&n);
    k=n;
    while(k>0)
    {
        d=k%10;
        if(d==0)
        e++;
        else
        {
        if((k%d)==0)
        g++;
        else 
        f++;
        }
        k=k/10;
    }
    p=f+e;
    if(n>1000000)
    printf("%d\n",p);
    else
    printf("%d\n",g);
    }
    return 0;
}2
