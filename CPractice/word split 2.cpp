#include <stdio.h>
#include <string.h>

int main()
{
    int t,i;
    scanf("%d",&t);
   for (i=1;i<=t;i++)
    {
        char s[1000];
        int l,c=0,temp,i ;
        scanf("%s",s);
        l=strlen(s);
        for(i=0;i<(l/2);i++)
        {
            temp =l/2;
            if(l%2==1)
               {
                temp =temp+ 1;
               }
            for(int j=temp;j<l;j++)
            {
                if(s[i]==s[j])
                {
                    c++;
                    s[j]='.';
                    break;
                }
            }
        }
        if(c==l/2)
            printf("YES\n");
        else
            printf("NO\n");
    }
    return 0;
}

