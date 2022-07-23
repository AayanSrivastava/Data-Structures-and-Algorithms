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

struct node* removeElements(struct node* head, int val){
    struct node *f1=head;
    while(head && head->val==val)
    {
        head=head->next;    
    }
    f1=head;
    while(f1 && f1->next)
    {
        if(f1->next->val==val)
            f1->next=f1->next->next;
        else
            f1=f1->next;
    }
    return head;
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