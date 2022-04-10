//function

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode *p=headA,*p1=headB;
    int n,c=0,d=0,i;
    while(p!=NULL)
    {
        c++;
        p=p->next;
    }
    while(p1!=NULL)
    {
        d++;
        p1=p1->next;
    }
    p=headA;
    p1=headB;
    if(c>d)
    {
        n=c-d;
        for(i=0;i<n;i++)
            p=p->next;
    }
    else
    {
        n=d-c;
        for(i=0;i<n;i++)
            p1=p1->next;
    }
    while(p!=NULL)
    {
        if(p==p1)
            return p;
        p=p->next;
        p1=p1->next;
    }
    return NULL;
}