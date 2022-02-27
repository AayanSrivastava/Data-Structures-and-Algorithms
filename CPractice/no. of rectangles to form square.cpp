#include <stdio.h>
int main() {
    int t,l,b,i,j,q,w,y,min;
    scanf("%d",&t);
    while(t--)
    {
        y=0,min=10000;
        scanf("%d %d",&l,&b);
        for(i=0 ; i<=10000; i=i+l)
        {
             for(j=0 ; j<=10000; j=j+b)
             {
             	q=(l+i);
             	w=(b+j);
             	if(q==w)
             	{ 
             	printf("%d%d",q,w);
             	break;
				}
         	}
    	}
    }
    return 0;
}

