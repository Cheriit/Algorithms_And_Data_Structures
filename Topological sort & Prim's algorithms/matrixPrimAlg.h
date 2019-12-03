#include <vector>
#ifndef GENERATOR
#define GENERATOR
#include "graphGenerator.h"
#endif
#ifndef TOPOLOGICAL_SORT
#define TOPOLOGICAL_SORT
#include "topologicalSort.h"
#endif
#include <string>
#include <algorithm>

typedef struct matrix_edge matrix_edge;

struct matrix_edge {
    int in;
    int out;
    int weight;
};

void mtrAddEdges(vector<matrix_edge *> &accesibleEdges, int *vertex, int size, int value);
vector<matrix_edge *> matrixPrim(int **graph, int size);
int mtrFindMinimumWeightID(vector<matrix_edge *> accesibleEdges);
bool mtrIsEdgeUseless(matrix_edge *edgeToCheck, vector<int> usedVertices);
void mtrRemoveUnnecessaryEdges(vector<matrix_edge *> &accesibleEdges, vector<int> &usedVertices, vector<matrix_edge*> &usedEdges);

vector<matrix_edge *> matrixPrim(int **graph, int size)
{
    vector<int> treeVertices;
    vector<matrix_edge *> treeEdges;
    vector<matrix_edge *> accesibleEdges;
    int minWeightId;

    treeVertices.push_back(0);
    mtrAddEdges(accesibleEdges, graph[0], size, 0);

    while (treeEdges.size() < size - 1)
    {
        if (accesibleEdges.size() == 0)
        {
            return treeEdges;
        }
        minWeightId = mtrFindMinimumWeightID(accesibleEdges);
        treeEdges.push_back(accesibleEdges[minWeightId]);

        treeVertices.push_back(accesibleEdges[minWeightId]->in);
        mtrAddEdges(accesibleEdges, graph[accesibleEdges[minWeightId]->in], size, accesibleEdges[minWeightId]->in);
        mtrRemoveUnnecessaryEdges(accesibleEdges, treeVertices, treeEdges);
    }
}

int mtrFindMinimumWeightID(vector<matrix_edge *> accesibleEdges)
{
    int minID = 0, minWeight = accesibleEdges[0]->weight;
    for (int i = 1; i < accesibleEdges.size(); i++)
    {
        if (minWeight > accesibleEdges[i]->weight)
        {
            minID = i;
            minWeight = accesibleEdges[i]->weight;
        }
    }
    return minID;
}

void mtrAddEdges(vector<matrix_edge *> &accesibleEdges, int *vertex, int size, int value)
{
    for(int i = 0; i < size; i++) {
        if(vertex[i] > 0) {
            matrix_edge *edgeToAdd = (matrix_edge*)malloc(sizeof(matrix_edge));
            edgeToAdd->in = i;
            edgeToAdd->out = value;
            edgeToAdd->weight = vertex[i];

            accesibleEdges.push_back(edgeToAdd);
        }
    }
}

bool mtrIsEdgeUseless(matrix_edge *edgeToCheck, vector<int> usedVertices)
{
    for (int j = 0; j < usedVertices.size(); j++)
    {
        if (usedVertices[j] == edgeToCheck->in)
        {
            return true;
        }
    }
    return false;
}

bool mtrIsEdgeDoubbled(matrix_edge *edgeToCheck, vector<matrix_edge *> usedEdges)
{
    for (int j = 0; j < usedEdges.size(); j++)
    {
        if (usedEdges[j]->in == edgeToCheck->in)
        {
            return true;
        }
       
    }
    return false;
}



void mtrRemoveUnnecessaryEdges(vector<matrix_edge *> &accesibleEdges, vector<int> &usedVertices, vector<matrix_edge*> &usedEdges)
{
    // matrix_edge *tmp;
    for (int i = 0; i < accesibleEdges.size(); i++)
    {
        if (mtrIsEdgeUseless(accesibleEdges[i], usedVertices) || mtrIsEdgeDoubbled(accesibleEdges[i], usedEdges))
        {
            // tmp = accesibleEdges[i];

            for (int j = i; j < accesibleEdges.size() - 1; j++)
            {
                accesibleEdges[j] = accesibleEdges[j + 1];
            }
            // free(tmp);
            accesibleEdges.pop_back();
            i--;
        }
    }
}


void printPrimMatrix(vector<matrix_edge *> minimalMatrixTree)
{
    for (vector<matrix_edge *>::size_type i = 0; i < minimalMatrixTree.size(); i++)
    {
        cout << "Edge\tVertex out: " << minimalMatrixTree.at(i)->out << "\tVertex in: " << minimalMatrixTree.at(i)->in << "\tWeight: " << minimalMatrixTree.at(i)->weight << endl;
    }
}