#include<stdio.h>
int main()
{
	int d,n,a[100],i,min;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	min=100000;
	for(i=0;i<n;i++)
	{
		d=a[i]^a[i++];
		printf("%d\n",d);
		if(d<min)
		min=d;
	}
	printf("%d",min);
}
