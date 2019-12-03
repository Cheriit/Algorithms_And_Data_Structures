#include "bst.h"

void insertAVLElem(Tree *root, vector<int> inorderTimes, int beg, int end);

Tree *createAVLTree(Tree *workingTree, int size)
{
    //std::sort(numbers, numbers+size);
    vector<int> inorderTimes;
    inorder(workingTree, &inorderTimes);
    int x = size/2;

    Tree *tree = insertTreeElement(NULL, inorderTimes[x]);

    if(size>1)
    {
        insertAVLElem(tree, inorderTimes, 0, x-1);

        if(size>2)
        {
            insertAVLElem(tree, inorderTimes, x+1, size-1);

        }
    }
    return tree;
}

void insertAVLElem(Tree *root, vector<int> inorderTimes, int beg, int end)
{
    int x = (beg+end)/2;

    if(beg<=end)
    {

        insertTreeElement(root, inorderTimes[x]);

        if(beg<x)
        {
            insertAVLElem(root, inorderTimes, beg, x-1);
        }
        if(x<end)
        {
            insertAVLElem(root, inorderTimes, x+1, end);
        }
    }

}


// int main()
// {
//     int SIZE = 3;
//     int *numbers = (int*)malloc(sizeof(int)*SIZE);
//     numbers[0]=1;
//     numbers[1]=2;
//     numbers[2]=3;

//     Tree tree = *createAVLTree(numbers,SIZE);

//     return 0;
// }
