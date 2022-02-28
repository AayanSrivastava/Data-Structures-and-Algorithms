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
int count(struct node *p)
{
    int c=0;
    while(p!=0)
    {
        c++;
        p=p->next;
    }
    return c;
}
int Rcount(struct node *p)
{
    int c=0;
    if(p==0)
        return 0;
    else
        return Rcount(p->next)+1;
}
int sum(struct node *p)
{
    int s=0;
    while(p!=NULL)
    {
        s+=p->data;
        p=p->next;
    }
    return s;
}
int Rsum(struct node *p)
{
    int s=0;
    if(p==0)
        return 0;
    else
        return Rsum(p->next)+p->data;
}
int maxx(struct node *p)
{
    int max=0;
    while(p!=NULL)
    {
        if(p->data>max)
            max=p->data;
        p=p->next;
    }
    return max;
}
int Rmaxx(struct node *p)
{
    int max=0;
    if(p==0)
        return 0;
    else
        if(Rmaxx(p->next)>p->data)
            return Rmaxx(p->next);
        else
            return p->data;
}
struct node* search(struct node *p,int k)
{
    while(p!=NULL)
    {
        if(p->data==k)
            return p;
        p=p->next;
    }
    return NULL;
}

struct node * Rsearch(struct node *p,int k)
{
    if(p==0)
        return NULL; 
    if (k==p->data) 
        return p;  
    return Rsearch(p->next,k);
}
void Rdisplay(struct node *p)
{
    if(p!=NULL)
    {
        printf("%d",p->data);
        Rdisplay(p->next);
    }
}

void display(struct node *p)
{
    while(p!=NULL)
    {
        printf("%d",p->data);
        p=p->next;
    }
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
    printf("Enter the element to search ");
    scanf("%d",&k);
    create(a,n);
    // ad=search(first,k);
    // printf("%d",(Rsearch(first,k))->data);
    // printf("%d",ad->data);
    // printf("%d",maxx(first));
    // printf("%d",Rmaxx(first));
    // printf("%d",count(first));
    // printf("%d\n",Rcount(first));
    // printf("%d",Rsum(first));
    // printf("%d",sum(first));
    // display(first);
    // Rdisplay(first);
}