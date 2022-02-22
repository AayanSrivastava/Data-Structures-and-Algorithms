#include<stdio.h>
#include<stdlib.h>
//INSERTION AT LAST

// struct ArrayADT
// {
//     int *a;
//     int size;
//     int x;
// };

// int main()
// {
//     struct ArrayADT *ar;
//     int i;
//     ar->a=(int *)malloc(ar->size*sizeof(int));
//     printf("Enter the size of array ");
//     scanf("%d",&ar->size);
//     printf("Enter the elements of array ");
//     for(i=0;i<ar->size;i++)
//     {
//         scanf("%d",&ar->a[i]);
//     }
//     printf("Enter the elements to insert");
//     scanf("%d",&ar->x);
//     ar->a[ar->size]=ar->x;
//     ar->size++;
//     for(i=0;i<ar->size;i++)
//     {
//         printf("%d ",ar->a[i]);
//     }
// }

//INSERTION AT ITH POS.

struct ArrayADT
{
    int *a;
    int size;
    int x;
    int p;
};

int main()
{
    struct ArrayADT *ar;
    int i;
    ar->a=(int *)malloc(ar->size*sizeof(int));
    printf("Enter the size of array ");
    scanf("%d",&ar->size);
    printf("Enter the elements of array ");
    for(i=0;i<ar->size;i++)
    {
        scanf("%d",&ar->a[i]);
    }
    printf("Enter the elements to insert");
    scanf("%d",&ar->x);
    printf("Enter the position to insert");
    scanf("%d",&ar->p);
    for(i=ar->size;i>ar->p;i--)
    {
        ar->a[i]=ar->a[i-1];
    }
    ar->a[ar->p-1]=ar->x;
    ar->size++;
    for(i=0;i<ar->size;i++)
    {
        printf("%d ",ar->a[i]);
    }
}