#include<stdio.h>
#include<stdlib.h>

struct node {
    int data;
    struct node *next;
}*first=NULL;

void create(int A[],int n)
{
    int i;
    struct node *t,*last;
    first=(struct node *)malloc(sizeof(struct node));
    first->data=A[0];
    first->next=NULL;
    last=first;

    for(i=1;i<n;i++)
    {
        t=(struct node *)malloc(sizeof(struct node));
        t->data=A[i];
        t->next=NULL;
        last->next=t;
        last=t;
    }
}

int middleNode(struct node* head){
        struct node* first1;
        first1=head;
        int i,c=1;
        while(first1 && first1->next)
        {
            c++;
            first1=first1->next;
        }
        first1=head;
        for(i=0;i<c/2;i++)
        {
            first1=first1->next;
        }
    return first1->data;
}

int middlep(struct node* head)
{
    struct node* slow=head;
    struct node* fast=head;
    while (fast && fast->next)
    {
        slow=slow->next;
        fast=fast->next->next;
    }
    return slow->data;
}
void display(struct node *p)
{
    while(p!=NULL)
    {
        printf("%d ",p->data);
        p=p->next;
    }
    printf("\n");
}

int main()
{
    int *a,n,i,k;
    struct node *ad;
    printf("Enter the size of array ");
    scanf("%d",&n);
    a=(int*)malloc(n*sizeof(int));
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    create(a,n);
    printf("%d\n",middleNode(first));
    printf("%d\n",middlep(first));
    display(first);
}