#include<stdio.h>
int main()
{
	int y,n,a[100],i,j,f[21]={0};
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<20;j++)
		{
			if(a[i]==j)
			f[j]=f[j]+1;
		}
	}
	y=(n/3);
	for(j=0;j<20;j++)
	{
		if(f[j]>y)
		{
		printf("%d",j);
		break;
		}
	}
}
