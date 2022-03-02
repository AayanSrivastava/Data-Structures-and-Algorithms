#include<stdio.h>
#include<stdlib.h>

struct Node
{
    int data;
    struct Node * next;
}*head,*tail;

void create(int A[],int n)
{
    int i;
    struct Node *t;
    head=(struct Node *)malloc(sizeof(struct Node));
    head->data=A[0];
    head->next=NULL;
    tail=head;

    for(i=1;i<n;i++)
    {
        t=(struct Node *)malloc(sizeof(struct Node));
        t->data=A[i];
        t->next=NULL;
        tail->next=t;
        tail=t;
    }
}

//Deletion at head\
Need 1 extra pointer to store head node and then move head to next node
//And then free the head node that is t
void delete(struct Node *p)
{
    struct Node *t;
    t=head;
    head=head->next;
    free(t);
}

//Deletion at any
// Needs 2 extra pointer to store previous and current node
//store Null initially in prev and head in current
//Now Traverse till position making prev as current and current to next node
//now point prev to current's next and free current
void deleteany(struct Node *p,int pos)
{
    struct Node *prev,*current;
    int i;
    prev=NULL;
    current=head;
    if (pos==1)
    {
        head=head->next;
        free(current);
    }
    else
    {
        for(i=0;i<pos-1;i++)
        {
        prev=current;
        current=current->next;
        }
        prev->next=current->next;
        free(current);
    }
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
    int a[100],i,n;
    printf("Enter the size of Array ");
    scanf("%d",&n);
    printf("Enter the elements of Array ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    create(a,n);
    // delete(head);
    deleteany(head,1);
    display(head);
    deleteany(head,4);
    display(head);
    
}
