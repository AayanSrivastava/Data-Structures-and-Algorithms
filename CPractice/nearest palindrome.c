#include<stdio.h>
#include<stdlib.h>
int palindromem(unsigned long long);
int palindromep(unsigned long long);
int main()
{
	int t;
	unsigned long long n,sp,sm;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%llu",&n);
	    sm=palindromem(n);
	    sp=palindromep(n);
	    if(abs(n-sm)<=abs(n-sp))
	    printf("%llu\n",sm);
	    else
	    printf("%llu\n",sp);
	}
}
int palindromem(unsigned long long n)
{
	int y,d,s;
	while(n)
	{
		s=0;
		y=n;
		while(y>0)
		{
			d=y%10;
			s=s*10+d;
			y=y/10;
		}
		if(s==n)
		return n;
	n=n-1;
	}
}
int palindromep(unsigned long long n)
{
	int y,d,s;
	while(n)
	{
		s=0;
		y=n;
		while(y>0)
		{
			d=y%10;
			s=s*10+d;
			y=y/10;
		}
		if(s==n)
		return n;
	n=n+1;
	}
}
