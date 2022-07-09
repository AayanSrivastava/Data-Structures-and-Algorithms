#include<stdio.h>
int main()
{
	int h,k,c,i,j,t,p,q,min,min1;
	unsigned long long n,a[1000000];
	scanf("%d",&q);
	while(q--)
	{
	h=0,min=100000,min1=100000;
	scanf("%llu%d",&n,&k);
	for(i=0;i<n;i++)
	{
		scanf("%llu",&a[i]);	
	}
	for(i=0;i<n;i++)
	{
		c=0;
	for(j=i;j<n;j++)
	{
		c+=a[j];
		t=i,p=j;
		if((c==k) && (t<min && p<min1))
		{
	    h++;
		min=t,min1=p;
		break;
		}
	}
	}
	if(h==0)
	printf("-1\n");
	else
	printf("%d %d\n",min+1,min1+1);
	}
}
