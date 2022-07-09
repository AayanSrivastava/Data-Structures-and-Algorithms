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

// struct ArrayADT
// {
//     int *a;
//     int size;
//     int x;
//     int p;
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
//     printf("Enter the position to insert");
//     scanf("%d",&ar->p);
//     for(i=ar->size;i>ar->p;i--)
//     {
//         ar->a[i]=ar->a[i-1];
//     }
//     ar->a[ar->p]=ar->x;
//     ar->size++;
//     for(i=0;i<ar->size;i++)
//     {
//         printf("%d ",ar->a[i]);
//     }
// }

// //DELETE AT LAST

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
//     ar->a[ar->size]=ar->a[ar->size-1];
//     ar->size--;
//     for(i=0;i<ar->size;i++)
//     {
//         printf("%d ",ar->a[i]);
//     }
// }

//DELETE AT ANY

// struct ArrayADT
// {
//     int *a;
//     int size;
//     int pos;
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
//     printf("Enter the pasition of element to delete ");
//     scanf("%d",&ar->pos);
//     for(i=ar->pos;i<ar->size;i++)
//     {
//         ar->a[i]=ar->a[i+1];
//     }
//     ar->size--;
//     for(i=0;i<ar->size;i++)
//     {
//         printf("%d ",ar->a[i]);
//     }
// }

//PASSING STRUCTURE TO A FUNCTION

//INSERTION AT any pos

struct ArrayADT
{
    int a[10];
    int size;
    int x;
    int pos;
};

void insert(struct ArrayADT *ar)
{
    int i;
    if(ar->pos>=0 && ar->pos < ar->size)
    {
        for(i=ar->size;i>ar->pos;i--)
        {
            ar->a[i]=ar->a[i-1];
        }
        ar->a[ar->pos]=ar->x;
        ar->size++;
    }
}
void display(struct ArrayADT ar)
{
    int i;
    for(i=0;i<ar.size;i++)
    {
        printf("%d ",ar.a[i]);
    }
}
int main()
{
    struct ArrayADT ar;
    int i;
    printf("Enter the size of array ");
    scanf("%d",&ar.size);
    printf("Enter the elements of array ");
    for(i=0;i<ar.size;i++)
    {
        scanf("%d",&ar.a[i]);
    }
    printf("Enter the element to insert ");
    scanf("%d",&ar.x);
    printf("Enter the position to insert ");
    scanf("%d",&ar.pos);
    printf("Enter the elements of array ");
    insert(&ar);
    display(ar);
}