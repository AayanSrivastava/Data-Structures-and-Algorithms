#include<stdio.h>
#include<math.h>
int main()
{
	int n,i=2;
	scanf("%d",&n);
	while(sqrt(n)>1)
	{
	if(n%i==0)
	{
	printf("%d ",i);
	n=n/i;
	}
	else
	i++;
	}
}
