#include<stdio.h>
#include<stdlib.h>

struct BSTnode{
    int data;
    struct BSTnode* left;
    struct BSTnode* right;
};

int min_max(struct BSTnode* root)
{
    if(root == NULL)
    return NULL;
    while(root->left !=NULL)
    {
        root=root->left;
    }
    return root->data;
}

void add(struct BSTnode* root,int data)
{
    struct BSTnode* root;
    root=(struct BstNode*)malloc(sizeof(struct BSTnode));
    root->data=data;
    root->left=NULL;
    root->right=NULL;
}
void display(struct BSTnode* root)
{
    while(root)
    {
        printf("%d ",root->data);
        root=root->left;
    }
}
int main()
{
    add(root,5);
    add(root,3);
    add(root,6);
    display(root);
}