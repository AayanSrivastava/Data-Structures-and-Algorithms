#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n,a[100],i,f[10]={0},j,*p;
	scanf("%d",&n);
	p=(int*)malloc(n*sizeof(int));
	for(i=0;i<n;i++)
	{
		scanf("%d",*(p+i));
	}
	p=a;
	for(i=0;i<n;i++)
	{
		f[*(p+i)]++;
	}
	for(i=0;i<10;i++)
	{
		printf("%d ",f[i]);
	}
}                                                                                                                                                                                                                                                                            
