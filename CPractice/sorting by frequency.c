#include<stdio.h>
int main()
{
	int t,n,a[61],f[61]={0},p,i,j;
	scanf("%d",&t);
	while(t--)
	{
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
        }
        for(i=0;i<n;i++)
        {
        for(j=0;j<n;j++)
        {
            if(a[j]>a[j+1])
            {
                p=a[j];
                a[j]=a[j+1];
                a[j+1]=p;
            }
        }
        }
        for(i=0;i<n;i++)
        {
            f[a[i]]++;
        }
        for(i=0;i<n;i++)
        {
        for(j=0;j<n;j++)
        {
            if(f[j]<f[j+1])
            {
                p=f[j];
                f[j]=f[j+1];
                f[j+1]=p;
            }
        }
        }
        for(i=1;i<10;i++)
        {
        	printf("%d ",f[i]);
		}
		printf("\n");
        for(i=1;i<=n;i++)
        {
        	printf("%d ",a[i]);
		}
		}
	return 0;
}
