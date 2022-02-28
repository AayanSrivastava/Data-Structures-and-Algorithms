#include<stdio.h>
void insertion(int,int []);
void printarray(int,int []);
int main()
{
	int i,n,a[100];
	printf("Enter the no. of elements in array=");
	scanf("%d\n",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	insertion(n,a);
	printarray(n,a);
}
void insertion(int n,int a[])
{
	int i,j,t;
	for(i=1;i<n;i++)
	{
		t=a[i];
		j=i-1;
	while(j>=0 && a[j]>t)
	{
		a[j+1]=a[j];
		j=j-1;
	}
	a[j+1]=t;	
	}
}
void printarray(int n,int a[])
{
	int i;
	for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
}
