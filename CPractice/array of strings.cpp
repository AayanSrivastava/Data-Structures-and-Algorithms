#include<stdio.h>
#include<string.h>
int main()
{
	int i,j;
	char s[4][50],t[50],g[50];
	for(i=0;i<4;i++)
	{
	gets(s[i]);
	}
	for(i=0;i<3;i++)
	{
		for(j=0;j<3-i;j++)
		{
			if(strcmp(s[j],s[j+1])>0)
			{
				strcpy(g,s[j]);
				strcpy(s[j],s[j+1]);
				strcpy(s[j+1],g);
			}
		}
	}
	for(i=0;i<4;i++)
	{
		for(j=i+1;j<4;j++)
		{
			if(strcmp(s[i],s[j])>0)
			{
				strcpy(t,s[i]);
				strcpy(s[i],s[j]);
				strcpy(s[j],t);
			}
		}
	}
	for(int i=0;i<4;i++)
	{
		puts(s[i]);
	}
	return 0;
}
