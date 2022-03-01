#include<stdio.h>
int main()
{
	int t,n,a[100],i,b,c,k;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d",&n);
	    for(i=0;i<n;i++)
	    {
	        scanf("%d",&a[i]);
	    }
	    b=0;
	    for(i=0;i<n-1;i++)
	    {
	        b=b^a[i];
	    }
	    c=1;
	    for(k=2;k<=n;k++)
	    {
	        c=c^k;
	    }
	    printf("%d",b^c);    
	}
	return 0;
}
