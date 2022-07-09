#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int findStringCode (char *);
int sum(char *);
int ar[100],l=0;
int findStringCode (char* input1)
{
	int i,j=0;
	char newst[100];
	for(i=0;input1[i]!='\0';i++)
	{
	if(input1[i]!=' ')
	{
		newst[j++]=input1[i];
	}
	else
	{
		j=0;
		sum(newst);
	}
	return 0;
}

int sum(char *s)
{
	int i,sum=0,f[100]={0};
	for(i=0;s[i]!='\0';i++)
	{
		if(s[i]>='A' && s[i]<='Z')
		s[i]=s[i]-32;
	}
	for(i=0;i<strlen(s);i++)
	{
		sum+=abs(f[s[i]-65]-f[s[cstrlen(s)-1-i]-65]);
	}
	ar[l++]=sum;
}

int main()
{
	int i;
	char input1[100];
	scanf("%s",input1);
	findStringCode(input1);
	for(i=0;i<l;i++)
	{
		printf("%d ",ar[i]);
	}
	return 0;
}
