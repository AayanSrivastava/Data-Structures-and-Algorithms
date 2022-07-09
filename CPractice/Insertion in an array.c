#include<stdio.h>
int main()
{
	int i,n,a[100],p,k;
	printf("Enter the no. of elements in array=");
	scanf("%d\n",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("Enter the position of array element to insert\n");
	scanf("%d",&p);
	printf("Enter the element to insert\n");
	scanf("%d",&k);
	if(p>n+1 || p<1)
	printf("insertion not possible");
	else
	{
	for(i=n-1;i>=p-1;i--)
	{
		a[i+1]=a[i];
	}
	a[p-1]=k;
	n++;
	}
	for(i=0;i<n;i++)
	{
	printf("%d ",a[i]);
	}
}
