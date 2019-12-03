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

typedef struct edge edge;
typedef struct matrix_edge matrix_edge;
struct edge
{
    ILGraph *in;
    ILGraph *out;
    int weight;
};

bool isOnList(ILGraph *vertex, vector<edge *> &visited)
{
    for (int i = 0; i < visited.size(); i++)
    {
        if (visited[i]->out == vertex)
        {
            return true;
        }
    }
    return false;
}

void addEdges(vector<edge *> &accesibleEdges, ILGraph *vertex)
{
    VertexListElem *list = vertex->list;
    while (list != NULL)
    {
        edge *edgeToAdd = (edge *)malloc(sizeof(edge));
        edgeToAdd->in = list->vertex;
        edgeToAdd->out = vertex;
        edgeToAdd->weight = list->weight;
        accesibleEdges.push_back(edgeToAdd);

        list = list->next;
    }
}

bool isEdgeUseless(edge *edgeToCheck, vector<ILGraph *> usedVertices)
{
    for (int j = 0; j < usedVertices.size(); j++)
    {
        if (usedVertices[j]->value == edgeToCheck->in->value)
        {
            return true;
        }
    }
    return false;
}
bool isEdgeDoubbled(edge *edgeToCheck, vector<edge *> usedEdges)
{
    for (int j = 0; j < usedEdges.size(); j++)
    {
        if (usedEdges[j]->in->value == edgeToCheck->in->value)
        {
            return true;
        }
    }
    return false;
}



void removeUnnecessaryEdges(vector<edge *> &accesibleEdges, vector<ILGraph *> &usedVertices, vector<edge *> &usedEdges)
{
    // edge *tmp;
    for (int i = 0; i < accesibleEdges.size(); i++)
    {
        if (isEdgeUseless(accesibleEdges[i], usedVertices) || isEdgeDoubbled(accesibleEdges[i], usedEdges))
        {
            // tmp = accesibleEdges[i];

            for (int j = i; j < accesibleEdges.size() - 1; j++)
            {
                accesibleEdges[j] = accesibleEdges[j + 1];
            }
            //free(tmp);
            accesibleEdges.pop_back();
            i--;
        }
    }
}

int findMinimumWeightID(vector<edge *> accesibleEdges)
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


vector<edge *> Prim(ILGraph **graph, int size)
{
    vector<ILGraph *> treeVertices;
    vector<edge *> treeEdges;
    vector<edge *> accesibleEdges;
    int minWeightId;

    treeVertices.push_back(graph[0]);
    addEdges(accesibleEdges, graph[0]);

    while (treeEdges.size() < size - 1)
    {
        if (accesibleEdges.size() == 0)
        {
            return treeEdges;
        }
        minWeightId = findMinimumWeightID(accesibleEdges);
        treeEdges.push_back(accesibleEdges[minWeightId]);

        treeVertices.push_back(accesibleEdges[minWeightId]->in);
        addEdges(accesibleEdges, accesibleEdges[minWeightId]->in);
        removeUnnecessaryEdges(accesibleEdges, treeVertices, treeEdges);
    }

    return treeEdges;
}

void printPrim(vector<edge *> minimalTree)
{
    for (vector<edge *>::size_type i = 0; i < minimalTree.size(); i++)
    {
        cout << "Edge\tVertex out: " << minimalTree.at(i)->out->value << "\tVertex in: " << minimalTree.at(i)->in->value << "\tWeight: " << minimalTree.at(i)->weight << endl;
    }
}