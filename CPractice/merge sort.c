#include<stdio.h>
void merge(int [],int,int,int);
void mergesort(int [],int,int);
void merge(int a[],int beg,int mid,int end)
{
    int i,j,k,n1,n2;
    n1=mid-beg+1;
    n2=end-mid;
    int a1[n1],a2[n2];
    for(i=0;i<n1;i++)
        a1[i]=a[beg+i];
    for(j=0;j<n2;j++)
        a2[j]=a[mid+1+j];
    i=0,j=0,k=beg;
    while(i<n1 && j<n2)
    {
        if(a1[i]<=a2[j])
        {
            a[k]=a1[i];
            i++;
        }
        else
        {
            a[k]=a2[j];
            j++;
        }
        k++;
    }
    while(i<n1)
    {
        a[k]=a1[i];
        i++;
        k++;
    }
    while(j<n2)
    {
        a[k]=a2[j];
        j++;
        k++;
    }
}
void mergesort(int a[],int beg,int end)
{
    if(beg<end)
    {
        int mid=(beg+end)/2;
        mergesort(a,beg,mid);
        mergesort(a,mid+1,end);
        merge(a,beg,mid,end);
    }
}
int main()
{
    int n,a[100],i,j,p;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    mergesort(a,0,n-1);
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n"); 
}
