#include<stdio.h>
#include<math.h>
int isprime(int);
int main()
{
	int t,n,i,s;
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	if(isprime(n-i) && isprime(i))
	{	
	printf("%d %d\n",i,n-i);
	break;
	}
	if(i==n)
	printf("-1\n");
	}
	}		
}
int isprime(int n)
{
	int i,c=0;
	if(n>1)
	{
	for(i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
		return 0;
	}
	return 1;
	}
	else
	return 0;
}
