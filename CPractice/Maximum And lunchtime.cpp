#include <stdio.h>

int main(void) {
	int t,n,k,a[100000],i,j,s,c,max,min,r,d[33];
	scanf("%d",&t);
	while(t--)
	{
	    max=0,min=100000,s=0,c=0;
	    scanf("%d%d",&n,&k);
	    for(i=0;i<n;i++)
	    {
	        scanf("%d",&a[i]);
	    }
	    for(j=1;j<1000;j++)
	    {
	        while(j>0)
	        {
	       for(i=0;i<32;i++)
	        {
	            d[i]=j%2;
	            j=j/2;
	        }
	        }
	        for(i=0;i<32;i++)
	        {
	            if(d[i]==1)
	            c++;
	        }
	        if(c==k)
	        {
	        for(i=0;i<n;i++)
	        {
	        s=s+(j&a[i]);
	        }
	        r=a[j];
	        if(s>max && r<min)
	        max=s,min=r;
	    }
	    }
	    printf("%d\n",r);
	}
	return 0;
}
