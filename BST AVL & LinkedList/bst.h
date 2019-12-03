#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

typedef struct tree Tree;

struct tree
{
    int value;
    Tree *left;
    Tree *right;
};

Tree *insertTreeElement(Tree *root, int value)
{
    if(!root)
    {
        root = (Tree*)malloc(sizeof(Tree));
        root->value = value;
        root->left = NULL;
        root->right = NULL;
        return root;
    }

    if(root->value > value)
    {
        root->left = insertTreeElement(root->left, value);
    }
    else if(root->value < value)
    {
        root->right = insertTreeElement(root->right, value);
    }

    return root;
}

Tree *searchTree(Tree *root, int value)
{
    Tree *ptr;
    ptr = root;
    while(ptr)
    {
        if(value > ptr->value)
        {   
                ptr = ptr->right;
        }
        else if(value < ptr->value)
        {
                ptr = ptr->left;
        }
        else
        {
            break;
        }
    }

    return ptr;
}

void inorder(Tree *root, vector<int> *inorderTimes)
{
    if(!inorderTimes) {
        inorderTimes = new vector<int>();
    }
    if(root != NULL)
    {
        inorder(root->left, inorderTimes);
        //inorderTimes.push_back(root->value);
        inorderTimes->push_back(root->value);
        inorder(root->right, inorderTimes);
    }
}

int *getArray(vector<int> *toConvert) {
    int* firstElementPtr = &(*toConvert)[0];
    return firstElementPtr;
}

void postorder(Tree *root, vector<int> *postorderTimes)
{
    if(!postorderTimes) {
        postorderTimes = new vector<int>();
    }

    if(root != NULL)
    {
        postorder(root->left, postorderTimes);
        postorder(root->right, postorderTimes);
        //printf(" %d", root->value);
        postorderTimes->push_back(root->value);
    }
}

void preorder(Tree *root, vector<int> *preorderTimes)
{
    if(!preorderTimes) {
        preorderTimes = new vector<int>();
    }

    if(root != NULL)
    {
        //printf(" %d", root->value);
        preorderTimes->push_back(root->value);
        preorder(root->left, preorderTimes);
        preorder(root->right, preorderTimes);
    }
}

int findHeight(Tree *root)
{
    if(!root)
    {
        return 0;
    }

    int leftHeight = findHeight(root->left);
    int rightHeight = findHeight(root->right);

    if(leftHeight > rightHeight)
    {
        return leftHeight + 1;
    }
    else
    {
        return rightHeight + 1;
    }
}

void deleteTree(Tree *root)
{
    if(root != NULL)
    {
        deleteTree(root->left);
        deleteTree(root->right);
        free(root);
    }
}

Tree *createBSTTree(int numbers[], int size)
{
    Tree *tree = insertTreeElement(NULL, numbers[0]);
    for(int i = 1; i < size; i++)
    {
        tree = insertTreeElement(tree, numbers[i]);
    }
    return tree;
}
