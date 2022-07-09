#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
int c,i,t,u;
char s[100];
scanf("%d",&t);
while(t--)
{
	scanf("%s",s);
	u=atoi(s);
	for(i=0;s[i]!='\0';i++)
    {
    	if(s[i]!='0')
    	{
    		if(u%(int)s[i]==0)
    		c++;
    	}
    }
    printf("%d\n",c);
}
return 0;
}
