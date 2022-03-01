#include<stdio.h>
int main()
{
	int t,n,a[100],i,s,min,max,j;
	scanf("%d",&t);
	while(t--)
	{
	    min=100000,max=-100000;
	    scanf("%d",&n);
	    for(i=0;i<n;i++)
	    {
	        scanf("%d",&a[i]);
	    }
	    for(i=0;i<n;i++)
	    {
	        for(j=i+1;j<n;j++)
	        {
	            s=0;
	        s=(a[i]+a[j]);
	        if(s>0 && s<min)
	        min=s;
	        else if(s<0 && s>max)
	        {
	        max=s;
	        min=s;
	        }
	        }
	    }
	    printf("%d\n",min);
	}
	return 0;
}
