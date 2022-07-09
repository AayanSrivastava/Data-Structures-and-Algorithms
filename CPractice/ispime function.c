#include<stdio.h>
int isprime(int);
int main()
{
	int n,i;
	scanf("%d",&n);
	if(isprime(n))
	printf("Prime\n");
	else
	printf("Not Prime\n");
}
int isprime(int n)
{
	int i,c=0;
	for(i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
		c++;
	}
	if(c==0)
	return 1;
	else 
	return 0;
}
