#include<stdio.h>
#include<stdlib.h>

//DISPALYING ARRAY

// struct ArrayADT
// {
//     int *a;
//     int size;
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
//     for(i=0;i<ar->size;i++)
//     {
//         printf("%d ",ar->a[i]);
//     }
// }


//USING PASSING STRUCTURE TO A FUNCTION

struct ArrayADT
{
    int a[10];
    int size;
};
void display(struct ArrayADT ar)
{
    int i;
    for(i=0;i<ar.size;i++)
    {
        printf("%d",ar.a[i]);
    }
}
int main()
{
    struct ArrayADT ar={{1,2,3,4,5},5};
    display(ar);
}