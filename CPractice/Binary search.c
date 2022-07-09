#include<stdio.h>
int main()
{
	int  i,beg,end,mid,n,a[100],x;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	printf("Enter the no. u want to search=");
	scanf("%d",&x);
	beg=0,end=n-1;
	while(beg<=end)
	{
		mid=(beg+end)/2;
		if(x==a[mid])
		{
		printf("Search successfull %d is at %d",x,mid+1);
		break;
		}
		else if(x>a[mid])
		beg=mid+1;
		else
		end=mid-1;
	}
	if(beg>end)
	printf("%d is not present in the array",x);
}
