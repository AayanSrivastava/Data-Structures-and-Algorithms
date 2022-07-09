#include<stdio.h>
int main()
{
	int i,k;
	char s[100];
	scanf("%s",s);
	for(i=0;s[i];i++)
	{
		if(s[i]=='.')
		{
		for(k=strlen(s)+2;k>i;k--)
		{
			s[k]=s[k-2];
		}
		}
	}
	printf("%s",s);
}

