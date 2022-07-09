#include<stdio.h>
int main()
{
	int i,a[100],n,t,j,p;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
		for(i=0;i<n-1;i++)
		{
			p=i;
			for(j=i+1;j<n;j++)
			{
				if(a[p]>a[j])
				p=j;
			}
			if(p!=i)
			{
				t=a[i];
				a[i]=a[p];
				a[p]=t;
			}
		}
		for(i=0;i<n;i++)
		{
			printf("%d ",a[i]);
		}
		return 0;
}
