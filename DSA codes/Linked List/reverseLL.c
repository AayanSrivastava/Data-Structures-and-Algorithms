#include<stdio.h>
#include<stdlib.h>

struct ListNode{
    int val;
    struct ListNode* next;
}*first=NULL;

void create(int a[],int n)
{
    int i;
    struct ListNode *last;
    first=(struct ListNode *)malloc(sizeof(struct ListNode));
    first->val=a[0];
    first->next=NULL;
    last=first;

    for(i=1;i<n;i++)
    {
        struct ListNode *t;
        t=(struct ListNode *)malloc(sizeof(struct ListNode));
        t->val=a[i];
        t->next=NULL;
        last->next=t;
        last=t;
    }
}

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *p1=head,*p=head,*q=NULL,*r=NULL;
    while (p!=NULL)
    {
        r=q;
        q=p;
        p=p->next;
        q->next=r;
    }
    p1=q;
    return p1;
}
void display(struct ListNode *p)
{
    p=first;
    while(p)
    {
        printf("%d",p->val);
        p=p->next;
    }
}
int main()
{
    int a[]={1,2,3,4,5};
    create(a,5);
    reverseList(first);
    display(first);
}