#include<stdio.h>
#include<stdlib.h>
int main()
{
	int i,k,a[100],t,l;
	long n;
	scanf("%d",&l);
	while(l--)
	{
	scanf("%ld",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	scanf("%d",&k);
	k++;
	while(k--)
	{
	for(i=0;i<n;i++)
	{
		t=a[i];
		a[i]=a[n-1];
		a[n-1]=t;
	}
	}
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
	printf("\n");
	}
}
