struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *head;
    head=(struct ListNode *)malloc(sizeof(struct ListNode));
    struct ListNode *p=head;
    if (list1 == NULL && list2 == NULL)
        return NULL;
    
    while(list1 && list2)
    {
        if(list1->val<list2->val)
        {   
            p->next=list1;
            list1=list1->next;
        }
        else
        {
            p->next=list2;
            list2=list2->next;
        }
        p=p->next;
    }
    if (list1) {
        p->next = list1;
    }
    if (list2) {
        p->next = list2;
    }
    return head->next;
}