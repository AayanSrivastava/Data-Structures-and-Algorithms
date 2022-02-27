#include<stdio.h>
#include<string.h>

int main()
{
	int t,i,j,k,l,e;
	char s[1000];
	scanf("%d",&e);
	while(e>0)
	{
	gets(s);
	l=strlen(s);
	for(i=0;i<l;i++)
	{
		for(j=i+1;j<l;j++)
		{
		if(s[i]==s[j])
		{
		for(k=j;k<l;k++)
		{
			s[k]=s[k+1];
		}
		l--;
		j--;
		}
		}
		}
		printf("%s\n",s);
	}
	return 0;
}
