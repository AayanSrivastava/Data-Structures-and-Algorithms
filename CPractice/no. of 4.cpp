#include<stdio.h>
int main()
{
	int n,c,i,d;
	long t[100000];
	scanf("%d",&n);
		for(i=0;i<n;i++)
		{
		scanf("%ld",&t[i]);
	}
	for(i=0;i<n;i++)
		{
			c=0;
		while(t[i]>0)
		{
			d=t[i]%10;
			if(d==4)
			c++;
			t[i]=t[i]/10;
		}
		printf("\n%d",c);
	}
}
