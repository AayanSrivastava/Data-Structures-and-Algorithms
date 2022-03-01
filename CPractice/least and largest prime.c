#include<stdio.h>
int leastprimefact(int);
int largestprimefact(int);
int main()
{
    int t,n,num,num1;
	scanf("%d",&t);
	while(t--)
	{	    
		scanf("%d",&n);
	    num = leastprimefact(n);
	    num1 = largestprimefact(n);
	    printf("least= %d\nlargest= %d",num,num1);
	}
}
int leastprimefact(int n)
{
	int i=2,min=10000;
	while(n>1)
	{
	if(n%i==0 && i<min)
	{
	min=i;
	n=n/i;
	}
	else
	i++;
	}
	return min;
}
int largestprimefact(int n)
{
	int i=2,max=0;
	while(n>1)
	{
	if(n%i==0 && i>max)
	{
	max=i;
	n=n/i;
	}
	else
	i++;
	}
	return max;
}
