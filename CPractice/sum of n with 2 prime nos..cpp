#include<stdio.h> 
int nextprime(int);
int isprime(int);               
int main()
{
	int i,n;
	scanf("%d",&n);
	for(i=2;i<n-i;i=nextprime(i))
	{
		if(isprime(n-i))
		{
			printf("%d %d\n",i,n-i);
			
		}
	}
}
int nextprime(int i)
{
	int j;
	for(j=2;j<i;j++)
	{
		if(i%j==0)
			break;
	i++;		
	return i;
	}
}
int isprime(int i)
{
	int j;
	for(j=2;j<i;j++)
	{
		if(i%j==0)
			break;
	if(i==i)			
	return i;
	}
}
