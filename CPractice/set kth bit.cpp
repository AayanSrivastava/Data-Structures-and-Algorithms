#include <stdio.h>
#include <math.h>
int main() {
	int t,n,k,i,d[33],s;
	scanf("%d",&t);
	while(t--)
	{
	    s=0;
	    scanf("%d %d",&n,&k);
	    while(n>0)
	    {
	    for(i=0;i<32;i++)
	    {
	        d[i]=n%2;
	        n=n/2;
	    }
	    }
	    for(i=0;i<32;i++)
	    {
	        if(d[k]==0)
	        d[k]=1;
	    }
	    for(i=31;i>=0;i--)
	    {
	        s=s+pow(2,i);
	    }
	    printf("%d\n",s);
	    }
	return 0;
}
