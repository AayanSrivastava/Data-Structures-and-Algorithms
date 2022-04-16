#include<stdio.h>
#include<stdlib.h>

struct node
{
    char data;
    struct node *next;
}*top=NULL;

void push(char x)
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

char pop()
{
    char x;
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

int balanced_paranthesis(char *s)
{
    int i;
    for(i=0;s[i]!='\0';i++)
    {
        if(s[i]=='('|| s[i]=='{' || s[i]=='[')
            push(s[i]);
        if(s[i]==')'|| s[i]=='}' || s[i]==']')
            if(!isEmpty)
                pop();
    }
    if(isEmpty())
    return 1;
    else
    return 0;
}

int main()
{
    char s[100]="(2+3)/(3*4 % 6)";
    if(balanced_paranthesis(s))
    return 1;
    else
    return 0;
}