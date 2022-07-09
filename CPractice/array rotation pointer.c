#include<stdio.h>
#include<stdlib.h>
int main()
{
	int t,i,*a,n,ar[10],k;
	scanf("%d%d%d",&n,&k);
	for(i=0;i<n;i++)
	{
		scanf("%d",&ar[i]);
	}
	a=ar;
	while(k--)
	{
	for(i=0;i<n;i++)
	{	
    	t=*a;
		*a=*(a+i);
		*(a+i)=t;
	}
	}
	for(i=0;i<n;i++)
	{
		printf("%d ",*(a+i));
	}
}
