#include<stdio.h>
//#include<stdlib.h>
int main()
{
	int *p,i,n,a[100];
	scanf("%d",&n);
	//p=(int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++);
	{
		scanf("%d",&a[i]);
	}
	p=a;
	for(i=0;i<n;i++);
	{
		printf("%d",*(p+i));
		p++;
	}
}
