#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
}*first=NULL;


void create(int A[],int n)
{
    int i;
    struct node *t,*last;
    first=(struct node *)malloc(sizeof(struct node));
    first->data=A[0];
    first->next=first;
    last=first;

    for(i=1;i<n;i++)
    {
        t=(struct node *)malloc(sizeof(struct node));
        t->data=A[i];
        t->next=last->next;
        last->next=t;
        last=t;
    }
}

void insert(struct node *p,int pos,int x)
{
    int i;
    struct node *t;
    t=(struct node *)malloc(sizeof(struct node));
    t->data=x;
    if (pos==0)
    {
        if (p==NULL)
        {
            t->next=t;
            first=t;
        }
        else
        {
            while(p->next!=first)
                p=p->next;
            p->next=t;
            t->next=first;
            first=t;
        }
    }
    else
    {
        for(i=0;i<pos-1;i++)
            p=p->next;
        t->next=p->next;
        p->next=t;
    }
}

void display(struct node *p)
{
    int flag=0;
    while(p!=first || flag==0)
    {
        flag=1;
        printf("%d ",p->data);
        p=p->next;
    }
    flag=0;
}

int main()
{
    int a[]={1,2,3,4,5};
    create(a,5);
    insert(first,2,2);
    display(first);
}