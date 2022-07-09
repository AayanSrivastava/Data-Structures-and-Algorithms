#include<stdio.h>
//#include<stdlib.h>
int main()
{
	int *p[100],i,n,a[100];
	scanf("%d",&n);
	//p=(int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++);
	{
		scanf("%d",&a[i]);
	}
	p[0]=&a[0];
	for(i=0;i<n;i++);
	{
		printf("%d",*(p+i));
		p[i]++;
	}
}
