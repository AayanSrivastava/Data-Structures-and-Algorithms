#include<stdio.h>
int main()
{
	int k,n,i,j;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
	for(j=1;j<=i-1;j++)
	{
		printf(" ");
	}
	for(k=1;k<=n;k++)
	{
		printf("*");
	}
	printf("\n");
}
}
