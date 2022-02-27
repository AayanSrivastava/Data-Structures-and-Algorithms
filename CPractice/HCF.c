#include<stdio.h>
int main()
{
	int a,b,h,t;
	scanf("%d %d",&a,&b);
	t=a<b?a:b;
	for(h=t;h>=1;h--)
	{
		if(a%h==0 && b%h==0)
		{
		printf("%d",h);
		break;
		}
	}
}