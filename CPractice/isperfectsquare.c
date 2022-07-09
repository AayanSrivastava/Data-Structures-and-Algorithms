#include<stdio.h>
#include<math.h>
#include<stdbool.h>
bool isperfectsquare(int);
bool isfibonacci(int);
bool isprime(int n);
int main()
{
	int n,t;
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d",&n);
	if(isfibonacci(n) && isprime(n))
	printf("fibonacci-prime no.\n");
	else
	printf("Not a fibonacci-prime no.\n");
	}
}
bool isperfectsquare(int n)
{
	int s;
	s=sqrt(n);
	return (s*s==n);
}
bool isfibonacci(int n)
{
	return isperfectsquare(5*n*n+4)||isperfectsquare(5*n*n-4);
}
bool isprime(int n)
{
	int i;
    for(i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
        return 0;
    }
    return 1;
}
