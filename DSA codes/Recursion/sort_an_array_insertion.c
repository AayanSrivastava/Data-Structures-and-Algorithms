#include<stdio.h>
void insert(int a[],int t)
{
    int len= sizeof(a)/sizeof(a[0]);
    if (len==0 || a[len-1]<=t)
    {
        a[len-1]=t;
        return;
    }
    int val=a[len-1];
    len--;
    insert(a,t);
    return;
}
int sort(int a[],int n)
{
    if(n==1)
    return;

    int t=a[n-1];
    n--;
    sort(a,n-1);
    insert(a,t);
}
int main()
{
    int arr[]={3,5,2,7,1,6};
    int n=6,i;
    sort(arr,n);
    for(i=0;i<n;i++)
    {
        printf("%d ",arr[i]);
    }
}