#include<stdio.h>
int main()
{
	int n,i,j,k=1;
	scanf("%d",&n);
	for(i=1;i<=n;i=i+2)
	{
	for(j=i;j<=n*n;j++)
	{
		printf("%d ",j);
	}
	printf("\n");
}
}
