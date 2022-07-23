#include <stdio.h>
#include <stdlib.h>
 
struct node {
    int data;
    struct node* left;
    struct node* right;
};

struct node* create(struct node *root,int val)
{
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;
    if (root==NULL)
        root=temp;

    if(val <= root->data)
        create(root->left,val);
    if(val <= root->data)
        create(root->right,val);
}
void display(struct node* root)
{
    while(root!=NULL)
    {
        display(root->left);
        printf("%d ",root->data);
        display(root->right);
    }
}
int main()
{
    struct node* root;
    // =(struct node*)malloc(sizeof(struct node));
    // int ar[]={1,2,3,4,5};
    root=create(root,1);
    create(root,2);
    create(root,3);
    create(root,5);
    display(root);
    return 0;
}