#include<stdio.h>
#include<stdlib.h>
int main()
{	
	int n,k,l[100],t[10],i,s=0,d=0,p,max=0;
	scanf("%d%d",&n,&k);
	for(i=0;i<n;i++)
	{
		scanf("%d%d",&l[i],&t[i]);
	}
	for(i=0;i<n;i++)
	{
		if(t[i]==0)
		s=s+l[i];
		else
		d++;
	}
	p=abs(k-d);
	while(k--)
	{
		for(i=0;i<n;i++)
		{
			if(t[i]==1)
			{
		if(l[i]>max)
		max=l[i];
		l[i]=l[i]-l[i];
		}
	}
		s=s+max;
	}
	printf("%d",s);
}