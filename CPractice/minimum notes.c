#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int x,n,i,a[10],d=0,s=0,c[2001]={0};
    scanf("%d%d",&x,&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        c[a[i]]++;
    }
    if(x>=2000 && c[2000]>0)
    {
        d+=x/2000;
        x-=d*2000;
        s+=d;
    }
    d=0;
    if(x>=500 && c[500]>0)
    {
        d+=x/500;
        x-=d*500;
        s+=d;
    }
    d=0;
    if(x>=200 && c[200]>0)
    {
        d+=x/200;
        x-=d*200;
        s+=d;
    }
    d=0;
    if(x>=100 && c[100]>0)
    {
        d+=x/100;
        x-=d*100;
        s+=d;       
    }
    d=0;
    if(x>=50 && c[50]>0)
    {
        d+=x/50;
        x-=d*50;
        s+=d;
    }
    d=0;
    if(x>=20 && c[20]>0)
    {
        d+=x/20;
        x-=d*20;
        s+=d;
    }
    d=0;
    if(x>=10 && c[10]>0)
    {
        d+=x/10;
        x-=d*10;
        s+=d;
    }
    d=0;
    if(x>=5 && c[5]>0)
    {
        d+=x/5;
        x-=d*5;
        s+=d;
    }
    d=0;
    if(x>=2 && c[2]>0)
    {
        d+=x/2;
        x-=d*2;
        s+=d;
    }
    d=0;
    if(x>=1 && c[1]>0)
    {
        d+=x/1;
        x-=d*1;
        s+=d;
    }
    printf("%d",s);
}
