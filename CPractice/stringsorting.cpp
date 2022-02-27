#include<stdio.h>
#include<string.h>
int main()
{
int i,j,n;
scanf("%d",&n);
char ar[n][20],s[n][50],t[20],*p,*q;
for(i=0;i<n;i++)
{
    scanf("%s %s",&ar[i],&s[i]);
}
for(i=0;i<n-1;i++)
{
    for(j=0;j<n-1-i;j++)
{
    if(strcmp(ar[j],ar[j+1])>0)
    {
        strcpy(t,ar[j]);
        strcpy(ar[j],ar[j+1]);
        strcpy(ar[j+1],t);
    }
}
}
for(i=0;i<n;i++)
{
	p=(strstr(s[i],"gmail"));
	q=(strstr(s[i],"@"));
	if(p && q)
    printf("%s\n",ar[i]);
}
}
