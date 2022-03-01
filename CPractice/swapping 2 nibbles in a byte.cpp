#include<stdio.h>
#include<math.h>
int main()
{
	int t,n,i,d[33],r,s,s1;
	scanf("%d",&t);
	while(t--)
	{
	    s=0,s1=0;
	    scanf("%d",&n);
	    for(i=0;i<8;i++)
	    {
	        d[i]=n%2;
	        n=n/2;
	    }
	    for(i=0;i<8;i++)
	    {
	        if(d[i]==1)
	        {
	            if(i<4)
	            s=s+pow(2,(i+4));
	            else
	            s1=s1+pow(2,(i-4));
	        }
	    }
	    printf("%d\n",s+s1);
	    }
	return 0;
}
