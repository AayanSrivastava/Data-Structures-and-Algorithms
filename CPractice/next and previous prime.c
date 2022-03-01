#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include<stdbool.h>
int nextprime(int);
int prevprime(int);
bool isprime(int);
int main() {
    long long int n,s,d;
    scanf("%lld",&n);
    s=nextprime(n);
    d=prevprime(n);
    if(abs(s-n)==abs(d-n))
        printf("%lld",(s-n));
    if(abs(s-n)<abs(d-n))
        printf("%lld",(s-n));
    else
        printf("%lld",(d-n));
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
int nextprime(int n)
{
    while(n!=0)
    {
        if(isprime(n))
            return n;
        else
            n++;
    }
    return 0;
}
int prevprime(int n)
{
    while(n!=0)
    {
        if(isprime(n))
            return n;
        else
            n--;
    }
    return 0;
}
