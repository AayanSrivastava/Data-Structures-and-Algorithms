#include<stdio.h>
#include<string.h>
int main()
{
	int t,l,i,c;
	char s[100];
	scanf("%d",&t);
	while(t--)
	{
		c=0;
	 	scanf("%s",&s);
	 	l=strlen(s);
		 for(i=0;s[i]!='\0';i++)
		{
			if(s[i]>=48 && s[i]<57)
			c++;
	 	}
	 	if(c==l)
		printf("%s\n",s);
		else
		printf("-1\n");
	}
		return 0;
	}
