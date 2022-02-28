#include<stdio.h>
int merge(int[],int[],int,int,int[]);
int main()
{
	int i,a1[100],a2[100],a3[100],n1,n2;
	printf("Enter the no. of elements in first array ");
	scanf("%d",&n1);
	printf("Enter the no. of elements in second array ");
	scanf("%d",&n2);
	printf("Enter the elements in first array ");
	for(i=0;i<n1;i++)
	{
	scanf("%d",&a1[i]);
	}
	printf("Enter the elements in second array ");
	for(i=0;i<n2;i++)
	{
	scanf("%d",&a2[i]);
	}
	merge(a1,a2,n1,n2,a3);
	for(i=0;i<n1+n2;i++)
	{
		printf("%d ",a3[i]);
	}
}
int merge(int a1[],int a2[],int n1,int n2,int a3[])
{
	int i=0,j=0,k=0;
	while(i<n1 && j<n2)
	{
		if(a1[i]<a2[j])
		a3[k++]=a1[i++];
		else
		a3[k++]=a2[j++];
	}
	while(i<n1)
		a3[k++]=a1[i++];
	while(j<n2)
		a3[k++]=a2[j++];
}
