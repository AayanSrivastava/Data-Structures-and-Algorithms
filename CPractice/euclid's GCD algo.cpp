#include<stdio.h>
int main()
{
	int a,b,t,q,w;
	scanf("%d %d",&a,&b);
	q=a>b?a:b;
	w=a<b?a:b;
	while(w>0)
	{
		t=q/w;
		q=w;
		w=q%w;
	}
	printf("%d",t);
}
