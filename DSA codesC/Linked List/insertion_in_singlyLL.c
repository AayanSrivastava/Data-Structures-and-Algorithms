#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
}*first=NULL;

void insert(struct node *p,int x,int pos)
{
    int i;
    struct node *t;
    t=(struct node*)malloc(sizeof(struct node));
    t->data=x;
    if (pos==0)
    {
        if(p==NULL)
        {
            t->next=NULL;
            first=t;
        }
        else
        {
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
    while(p!=NULL)
    {
        printf("%d ",p->data);
        p=p->next;
    }
}
int main()
{
    insert(first,2,0);
    insert(first,3,0);
    insert(first,4,0);
    insert(first,1,2);
    display(first);
}