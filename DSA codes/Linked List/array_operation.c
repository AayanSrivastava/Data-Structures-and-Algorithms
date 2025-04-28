#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>



// struct Array
// {
//     int a[10];
//     int size;
// };

// void display(struct Array a)
// {
//     int i;
//     for(i=0;i<a.size;i++)
//     {
//         printf("%d ",a.a[i]);
//     }
// }
// int main()
// {
//     struct Array ar; // we can initialize here too {{1,2,3,4,5},5};
//     int i;
//     scanf("%d",&ar.size);
//     for(i=0;i<ar.size;i++)
//     {
//         scanf("%d",&ar.a[i]);
//     }

//     display(ar);
// }

struct Array
{
    int *a;
    int size;
    int x;
};
// void merge(struct Array a)
// void union(struct Array a,struct Array b,int n,int m)
// {
//     int i,j;
//     struct Array *ar3;
//     ar3.a=(int *)malloc(5*sizeof(int));
//     for(i=0;i<n;i++)
//     {
//         ar3.
//     }

// }
// void intersection()
// void difference()
// void symmetric_difference()

// void reverse(struct Array *a)
// {
//     int i,k=0;
//     int *ar3;
//     ar3=(int *)malloc(a->size*sizeof(int));
//     for(i=a->size-1;i>=0;i--)
//     {
//         ar3[k++]=a->a[i];
//     }
//     for(i=0;i<a->size;i++)
//     {
//         a->a[i]=ar3[i];
//     }
// }
int linearsearch(struct Array *a,int key1)
{
    int i;
    for(i=0;i<a->size;i++)
    {
        if(key1==a->a[i])
        return i;
    }
    return -1;
}
bool issorted(struct Array *a)
{
    int i;
    for(i=0;i<a->size;i++)
    {
        if(a->a[i]>a->a[i+1])
        return false;
    }
    return true;
}
void display(struct Array a)
{
    int i;
    for(i=0;i<a.size;i++)
    {
        printf("%d ",a.a[i]);
    }
}
int main()
{
    struct Array ar1,ar2;
    struct Array *ar3;
    int i;
    printf("Enter the size of 1st array ");
    scanf("%d",&ar1.size);
    printf("Enter the elements of 1st array ");
    ar1.a=(int *)malloc(sizeof(int));
    for(i=0;i<ar1.size;i++)
    {
        scanf("%d",&ar1.a[i]);
    }

    // printf("Enter the size of 2nd array ");
    // scanf("%d",&ar2.size);
    // printf("Enter the elements of 2nd array ");
    // ar2.a=(int *)malloc(sizeof(int));
    // for(i=0;i<ar2.size;i++)
    // {
    //     scanf("%d",&ar2.a[i]);
    // }
    // printf("enter the element to search ");
    // scanf("%d",&ar1.x);
    // printf("%d",issorted(&ar1)); 
    // printf("\n%d",linearsearch(&ar1,ar1.x));
    // reverse(&ar1);
    // display(ar1);
}