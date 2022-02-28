#include<stdio.h>
int main()
{
	int k=0,max=0,n,l=0,a[100],c,i,j,d[100];
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);	
	}
	for(i=0;i<n;i++)
	{
		c=0;
	for(j=i;j<n;j++)
	{	
		c+=a[j];
		if(c>max)
		{
			l++;
		max=c;
		d[k++]=a[j];
		}
	}
	}
	for(k=0;k<l;k++)
	{
		printf("%d ",d[k]);	
	}
}
