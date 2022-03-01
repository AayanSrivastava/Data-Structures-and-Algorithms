#include<stdio.h>
#include<math.h>
#include<stdbool.h>
bool isprime(int);
int main()
{
	int n,t;
	scanf("%d",&t);
	while(t--)
	{
	scanf("%d",&n);
	if(isprime(n))
	printf("prime\n");
	else
	printf("Not prime\n");
	}
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
