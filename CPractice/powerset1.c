#include<stdio.h>
#include<math.h>
int main()
{
	int n;
	char s[100];
	scanf("%d",&n);
	scanf("%s",s);
	power(s,n);
}
int power(char s[],int n)
{
	int ps,i,j;
	ps=pow(2,n);
	printf("{");
	for(i=0;i<ps;i++)
	{
		printf("{");
	for(j=0;j<n;j++)
	{
		if(i & (1<<j))
		printf(" %c ",s[j]);
	}
	printf("},");
	}
	printf("}");
}
