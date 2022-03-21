#include<stdio.h>
#include<stdlib.h>

struct node
{
    int val;
    struct node *next;
}*first=NULL;


void create(int A[],int n)
{
    int i;
    struct node *t,*last;
    first=(struct node *)malloc(sizeof(struct node));
    first->val=A[0];
    first->next=NULL;
    last=first;

    for(i=1;i<n;i++)
    {
        t=(struct node *)malloc(sizeof(struct node));
        t->val=A[i];
        t->next=NULL;
        last->next=t;
        last=t;
    }
}

struct node *detectCycle(struct node *head) {
    int c=0;
    struct node* fast=head,*slow=head;
    while(slow && fast && fast->next)
    {
        fast=fast->next->next;
        c++;
        slow=slow->next;
        if (fast==slow)
            return c;
    }
    return -1;
}

void display(struct node *p)
{
    while(p!=NULL)
    {
        printf("%d ",p->val);
        p=p->next;
    }
}

int main()
{
    int n,i,*a;
    printf("Enter the size of array ");
    scanf("%d",&n);
    a=(int*)malloc(n*sizeof(int));
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    create(a,n);
    swapPairs(first);
    display(first);
    return 0;
}