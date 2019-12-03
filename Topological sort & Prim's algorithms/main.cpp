#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <fstream>
#include <chrono>
#include <ctime>
#include <algorithm>
#include <functional>
#ifndef GENERATOR
#define GENERATOR
#include "graphGenerator.h"
#endif
#ifndef TOPOLOGICAL_SORT
#define TOPOLOGICAL_SORT
#include "topologicalSort.h"
#endif
#include "primAlg.h"
#include "matrixPrimAlg.h"
using namespace std;
// using namespace std::chrono;

int *mktable(FILE *f, int SIZE)
{
    int tmp;
    int *numbers = (int *)malloc(sizeof(int) * SIZE);

    for (int i = 0; i < SIZE; i++)
    {
        fscanf(f, "%d", &tmp);
        numbers[i] = tmp;
    }
    return numbers;
}

void writeToFile(double timeToSave)
{
    FILE *fp = fopen("results.txt", "w+");
    fprintf(fp, "%f\n", timeToSave);
    fclose(fp);
}

void appendResultsToFile(string fileName, chrono::duration<double> result)
{
    ofstream file;
    file.open(fileName, ios_base::app);
    if (file.is_open())
    {
        file << to_string(result.count()) + "\n";
        file.close();
    }
    else
    {
        cout << "Error while saving to " + fileName << endl;
    }
}

void appendHeightsToFile(string fileName, int height)
{
    ofstream file;
    file.open(fileName, ios_base::app);
    if (file.is_open())
    {
        file << to_string(height) + "\n";
        file.close();
    }
    else
    {
        cout << "Error while saving to " + fileName << endl;
    }
}

void cleanResultFiles(string files[], int SIZE)
{
    if (!files)
        return;
    for (int i = 0; i < SIZE; i++)
    {
        ofstream file;
        file.open(files[i], ios::out | ios::trunc);
        if (file.is_open())
            file.close();
        else
            cout << "error while cleaning file " + files[i] << endl;
    }
}




int main()
{
    srand(time(NULL));
    string files[] = {
        "results/prim/30Graph.txt",
        "results/prim/30Matrix.txt",
        "results/prim/70Graph.txt",
        "results/prim/70Matrix.txt",
        "results/TS/60Graph.txt",
        "results/TS/60Matrix.txt",
    };
    cleanResultFiles(files, 8);
    std::chrono::time_point<std::chrono::high_resolution_clock> start, end;
    std::chrono::duration<double> usedTime;
    //int SIZE;
    float DENSITY;
    ILGraph **graph;
    int **matrix;
    processedElem* ts_graph;
    vector<int> ts_matrix;
    vector<edge *> minimalTree;
    vector<matrix_edge*> minimalMatrixTree;

    for(int SIZE = 10; SIZE <= 150; SIZE = SIZE + 10)
    {
        DENSITY = 0.6;
        graph = generateGraph(SIZE, DENSITY);

        matrix = generateGraphMatrix(graph, SIZE);

        // printGraph(graph, SIZE);
        // printMatrix(matrix, SIZE);

        start = std::chrono::high_resolution_clock::now();
        
        ts_graph = TS_main(graph, SIZE); //Tylko dla Density 0.6
        
        end = std::chrono::high_resolution_clock::now();
        usedTime = end - start;
        appendResultsToFile("results/TS/60Graph.txt", usedTime);
        

        start = std::chrono::high_resolution_clock::now();
        
        ts_matrix = matrixTS(matrix, SIZE); //Tylko dla Density 0.6

        end = std::chrono::high_resolution_clock::now();
        usedTime = end - start;
        appendResultsToFile("results/TS/60Matrix.txt", usedTime);
        

        // printTS(ts_graph);
        // cout<<"========="<<endl;
        // printTSMatrix(ts_matrix);

        removeMatrix(matrix, SIZE);
        removeGraph(graph, SIZE);

        DENSITY = 0.3;
        graph = generateUndirectedGraph(SIZE, DENSITY);
        matrix = generateGraphMatrix(graph, SIZE);

        // printGraph(graph, SIZE);
        // printGraphMatrix(matrix, SIZE);

        start = std::chrono::high_resolution_clock::now();
        
        minimalTree = Prim(graph, SIZE); //Tylko dla Density 0.3 i 0.7

        end = std::chrono::high_resolution_clock::now();
        usedTime = end - start;
        appendResultsToFile("results/prim/30Graph.txt", usedTime);
        
        start = std::chrono::high_resolution_clock::now();

        minimalMatrixTree = matrixPrim(matrix, SIZE); //Tylko dla Density 0.3 i 0.7

        end = std::chrono::high_resolution_clock::now();
        usedTime = end - start;
        appendResultsToFile("results/prim/30Matrix.txt", usedTime);

    //////

        removeMatrix(matrix, SIZE);
        removeGraph(graph, SIZE);

        DENSITY = 0.7;
        graph = generateUndirectedGraph(SIZE, DENSITY);
        matrix = generateGraphMatrix(graph, SIZE);

        // printGraph(graph, SIZE);
        // printGraphMatrix(matrix, SIZE);

        start = std::chrono::high_resolution_clock::now();
        
        minimalTree = Prim(graph, SIZE); //Tylko dla Density 0.3 i 0.7

        end = std::chrono::high_resolution_clock::now();
        usedTime = end - start;
        appendResultsToFile("results/prim/70Graph.txt", usedTime);
        
        start = std::chrono::high_resolution_clock::now();

        minimalMatrixTree = matrixPrim(matrix, SIZE); //Tylko dla Density 0.3 i 0.7

        end = std::chrono::high_resolution_clock::now();
        usedTime = end - start;
        appendResultsToFile("results/prim/70Matrix.txt", usedTime);

        removeMatrix(matrix, SIZE);
        removeGraph(graph, SIZE);
        // cout<<"========="<<endl;
        // printPrim(minimalTree);
        // cout<<"========="<<endl;
        // printPrimMatrix(minimalMatrixTree);
    }
    


    return 0;
}
