#include<stdio.h>
#include<stdlib.h>

struct stack
{
    int top;
    int size;
    int *s;
};

void create(struct stack *st)
{
    printf("Enter the size of stack ");
    scanf("%d",&st->size);
    st->top=-1;
    st->s=(int*)malloc(st->size*sizeof(int));
}

void display(struct stack *st)
{
    int i;
    for(i=st->top;i>=0;i--)
    {
        printf("%d ",st->s[i]);
    }
}

void push(struct stack *st,int x)
{
    if(st->top==st->size-1)
    printf("Stack Overflow");
    else
    {
        st->top++;
        st->s[st->top]=x;
    }
}

int pop(struct stack *st)
{
    int x=-1;
    if(st->top==-1)
    printf("Stack Underflow");
    else
    {
        x=st->s[st->top--];
    }
    return x;
}

int isfull(struct stack *st)
{
    if(st->top==st->size-1)
    return 1;
}

int isEmpty(struct stack *st)
{
    if(st->top==-1)
    return 1;
}

int peek(struct stack *st,int index)
{
    int x=-1;
    if(st->top-index+1<0)
        printf("Invalid Index ");
    x=st->s[st->top-index+1];
    return x;
}
int stacktop(struct stack st)
{
    int x=-1;
    if(st.top==-1)
        printf("stack is Empty");
    else
        x=st.s[st.top];
    return x;
}

int main()
{
    struct stack st;
    create(&st);
    push(&st,10);
    push(&st,20);
    push(&st,30);
    push(&st,40);
    printf("%d\n",pop(&st));
    printf("%d\n",peek(&st,2));
    printf("%d\n",stacktop(st));
    display(&st);

}