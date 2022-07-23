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

struct node* removeNthFromEnd(struct node* head, int n){
    int i;
    struct node *start=(struct node *)malloc(sizeof(struct node));
    start->next=head;
    struct node *fast=start,*slow=start;
    for(i=1;i<=n;i++)
        fast=fast->next;
    while(fast->next)
    {
        fast=fast->next;
        slow=slow->next;
    }
    slow->next=slow->next->next;
    return start->next;
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
    printf("\n");
    create(a,n);
    removeElements(first,6);
    display(first);
    return 0;
}