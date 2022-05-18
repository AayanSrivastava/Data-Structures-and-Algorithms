#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
}*top=NULL;

void push(int x)
{
    struct node *t;
    t=(struct node *)malloc(sizeof(struct node));
    if(t==NULL)
        printf("Stack Overflow ");
    else
    {   
        t->data=x;
        t->next=top;
        top=t;
    }
}

int pop()
{
    int x=-1;
    if(top==NULL)
        printf("Stack is empty ");
    else
    {
        x=top->data;
        top=top->next;
    }
    return x;
}

int isEmpty()
{
    if(top==NULL)
        return 1;
    else
        return 0;
}
int isFull()
{
    struct node *t;
    t=(struct node *)malloc(sizeof(struct node));
    if(t==NULL)
        return 1;
    else
        return 0;
}

int peek(int pos)
{
    struct node *p;
    p=top;
    int x=-1,i;
    for(i=0;p && i<pos-1;i++)
    {
        p=p->next;
    }
    if(p)
        return p->data;
    else
        return -1;
}
int stacktop()
{
    int x=-1;
    if(top==NULL)
        return x;
    else
        x=top->data;
    return x;
}

void display()
{
    struct node *p;
    p=top;
    while(p)
    {
        printf("%d ",p->data);
        p=p->next;
    }
    printf("\n");
}
int main()
{
    push(1);
    push(2);
    push(3);
    push(4);
    display();
    printf("%d\n",pop());
    printf("%d\n",peek(2));
    printf("%d\n",stacktop());
    display();
}