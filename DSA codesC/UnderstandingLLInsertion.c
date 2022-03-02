#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node * next;
}*head,*tail;


//insertion at head
void insert(struct Node *p,int k)
{
    struct Node *t;
    t=(struct Node *)malloc(sizeof(struct Node));
    t->data=k;
    t->next=head;
    head=t;
}

//insertion at tail
void inserttail(struct Node *p,int k)
{
    struct Node *t;
    t=(struct Node *)malloc(sizeof(struct Node));
    t->data=k;
    tail->next=t;
    t->next=NULL;
    tail=t;
}

//insert at any
void insertany(struct Node *p,int k,int x)
{
    int i;
    struct Node *t;
    t=(struct Node *)malloc(sizeof(struct Node));
    t->data=k;
    for(i=0;i<x-1;i++)
    {
        p=p->next;
    }
    printf("%d\n",p->data);
    t->next=p->next;
    p->next=t;
}

//Insertion in sorted List

void sortedinsertion(struct Node *p,int k)
{
    struct Node *t,*prev,*current;
    t=(struct Node *)malloc(sizeof(struct Node ));
    t->data=k;
    prev=head;
    current=head;
    while(current->data<=k)
    {
        prev=current;
        current=current->next;
    }
    t->next=prev->next;
    prev->next=t;
}

void display(struct Node *p)
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
    struct Node *t;
    t=(struct Node *)malloc(sizeof(struct Node));
    t->data=10;
    t->next=NULL;
    head=t;
    tail=t;
    insert(head,3);
    insert(head,2);
    insert(head,1);
    inserttail(tail,4);
    inserttail(tail,5);
    // insertany(head,4,4);
    // insertany(head,4,2);
    display(head);
    printf("%d\n",head->data);
    printf("%d\n",tail->data);
    sortedinsertion(head,4);
    display(head);
}
