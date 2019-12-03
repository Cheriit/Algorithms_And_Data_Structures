#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream> 
#include <fstream>
#include <chrono> 
#include <ctime> 
#include <algorithm>
#include <functional>
#include "avl.h"
#include "linkedList.h"
using namespace std::chrono;

int *mktable(FILE *f, int SIZE){
    int tmp;
    int *numbers = (int*)malloc(sizeof(int)*SIZE);

    for(int i=0;i<SIZE;i++)
    {
        fscanf(f, "%d", &tmp);
        numbers[i] = tmp;

    }
    return numbers;
}

void writeToFile(double timeToSave)
{
    FILE *fp = fopen("results.txt","w+");
    fprintf(fp,"%f\n",timeToSave);
    fclose(fp);
}



void appendResultsToFile(string fileName, duration<double> result) {
    ofstream file;
    file.open(fileName, ios_base::app);
    if(file.is_open()) {
        file << to_string(result.count()) + "\n";
        file.close();
    } else {
        cout << "Error while saving to " + fileName << endl;
    }
}

void appendHeightsToFile(string fileName, int height) {
    ofstream file;
    file.open(fileName, ios_base::app);
    if(file.is_open()) {
        file << to_string(height) + "\n";
        file.close();
    } else {
        cout << "Error while saving to " + fileName << endl;
    }
}

void cleanResultFiles(string files[], int SIZE) {
    if(!files)
        return;
    for(int i = 0; i < SIZE; i++) {
        ofstream file;
        file.open(files[i], ios::out | ios::trunc);
        if(file.is_open())
            file.close();
        else
            cout << "error while cleaning file " + files[i] << endl;
            
    }
}


int main()
{
    string files[] = {
        "results/bst/build.txt",
        "results/bst/search.txt",
        "results/bst/height.txt",
        "results/avl/height.txt",
        "results/bst/delete.txt",
        "results/list/build.txt",
        "results/list/search.txt",
        "results/list/delete.txt"
    };
    cleanResultFiles(files, 8);
    time_point<high_resolution_clock> start, end;
    duration<double> usedTime;
    int SIZE, treeHeight;
    Tree *workingTree, *workingAVLTree;
    ListElement *workingList;
    FILE* f = fopen("arrays.txt","r");
    for(int i=0;i<15;i++)
    {
        fscanf(f, "%d", &SIZE);
        int *array = mktable(f, SIZE);

        start = high_resolution_clock::now();
        workingTree=createBSTTree(array, SIZE);
        end = high_resolution_clock::now();

        usedTime = end - start;
        printf("Tworzenie drzewa nr: %d: %f \n",i+1,usedTime.count());
        appendResultsToFile("results/bst/build.txt", usedTime);
        

        start = high_resolution_clock::now();
        for(int i=0;i<SIZE;i++)
        {
            searchTree(workingTree, array[i]);
        }

        end = high_resolution_clock::now();
        usedTime = end - start;
        printf("Przeszukiwanie drzewa nr: %d: %f \n",i+1,usedTime.count());
        appendResultsToFile("results/bst/search.txt", usedTime);

        treeHeight=findHeight(workingTree);
        printf("Wysokosc drzewa BST nr: %d: %d \n",i+1,treeHeight);
        appendHeightsToFile("results/bst/height.txt", treeHeight);

        workingAVLTree=createAVLTree(workingTree, SIZE);
        treeHeight=findHeight(workingAVLTree);
        deleteTree(workingAVLTree);
        printf("Wysokosc drzewa AVL nr: %d: %d \n",i+1,treeHeight);
        appendHeightsToFile("results/avl/height.txt", treeHeight);

        start = high_resolution_clock::now();
        deleteTree(workingTree);
        end = high_resolution_clock::now();

        usedTime = end - start;
        printf("Usuwanie drzewa nr: %d: %f \n",i+1,usedTime.count());
        appendResultsToFile("results/bst/delete.txt", usedTime);

        start = high_resolution_clock::now();
        workingList=createLinkedList(array, SIZE);
        end = high_resolution_clock::now();

        usedTime = end - start;
        printf("Tworzenie Listy nr: %d: %f \n",i+1,usedTime.count());
        appendResultsToFile("results/list/build.txt", usedTime);

        start = high_resolution_clock::now();
        for(int i=0;i<SIZE;i++)
        {
            searchList(workingList, array[i]);
        }
        end = high_resolution_clock::now();

        usedTime = end - start;
        printf("Przeszukiwanie Listy nr: %d: %f \n",i+1,usedTime.count());
        appendResultsToFile("results/list/search.txt", usedTime);


        start = high_resolution_clock::now();
        deleteList(workingList);
        end = high_resolution_clock::now();

        usedTime = end - start;
        printf("Usuwanie Listy nr: %d: %f \n",i+1,usedTime.count());
        appendResultsToFile("results/list/delete.txt", usedTime);


    }

    return 0;
}
