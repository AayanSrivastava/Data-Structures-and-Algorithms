#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main() {
    int ch;
    int n;
    float t,sq;
    int q,w,p=1;
    int num,f=1,g;
    int m,r=1,i;
    int x,y;
    scanf("%d",&ch);
    switch(ch)
    {
        case 1:
            scanf("%d",&n);
            sq=n/2;
            t=0;
            while(sq!=t)
            {
                t=sq;
                sq=(n/t+t)/2;
            }
            printf("%f",sq);
			break;
        case 2:
            scanf("%d%d",&q,&w);
            while(w!=0)
            {
                p*=q;
                w--;
            }
            printf("%d",p);
            break;
        case 3:
            scanf("%d",&num);
            for(g=1;g<=num;g++)
            {
                f*=g;
            }
            printf("%d",f);
            break;
        case 4:
            scanf("%d",&m);
            for(i=1;i<=m;i++)
            {
                r=r*2;
            }
            printf("%d",r);
            break;
        case 5:
            scanf("%d%d",&x,&y);
            int logg(int x,int y)
            {
                return (x>y-1) ? 1+logg(x/y,y) : 0;
            }
            printf("%d",(logg(x,y)));
            break;
    }
    return 0;
}

