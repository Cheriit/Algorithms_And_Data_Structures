#include <vector>
#ifndef GENERATOR
#define GENERATOR
#include "graphGenerator.h"
#endif
#include <string>

#ifndef ALGORITHM
#define ALGORITHM
#include <algorithm>
#endif

typedef struct processedElem processedElem;

struct processedElem
{
    ILGraph *elem;
    processedElem *next;
};

int firstUnvisitedNeighbour(int **matrix, int vertex, int size, bool *visited);

processedElem *shift(processedElem *list, ILGraph *vertex)
{
    processedElem *newElement = (processedElem *)malloc(sizeof(processedElem));
    newElement->next = list;
    newElement->elem = vertex;
    return newElement;
}

processedElem *join(processedElem *list1, processedElem *list2)
{
    if (list1 == NULL)
    {
        return list2;
    }
    if (list2 == NULL)
    {
        return list1;
    }
    processedElem *tmp = list1;
    while (tmp->next != NULL)
    {
        tmp = tmp->next;
    }
    tmp->next = list2;
    return list1;
}

bool isVisited(ILGraph *vertex, vector<ILGraph *> visited)
{
    for (int i = 0; i < visited.size(); i++)
    {
        if (visited[i] == vertex)
        {
            return true;
        }
    }
    return false;
}

processedElem *TS(ILGraph *vertex, vector<ILGraph *> &visited)
{
    processedElem *processed = NULL;
    VertexListElem *list = vertex->list;
    visited.push_back(vertex);
    while (list != NULL)
    {
        if (!isVisited(list->vertex, visited))
        {
            processed = join(TS(list->vertex, visited), processed);
        }
        list=list->next;
    }
    processedElem *result = shift(processed, vertex);
    return result;
}

processedElem *TS_main(ILGraph **graph, int size)
{
    vector<ILGraph *> visited;
    processedElem *processedList = NULL;
    processedElem *tmp = NULL;
    for (int i = 0; i < size; i++)
    {
        
        if (!isVisited(graph[i], visited))
        {
            tmp = TS(graph[i], visited);
            join(tmp, processedList);
        }
    }
    return tmp;
}

void printMatrix(int **matrix, int size) {
    for(int i = 0; i < size; i++ ){
        for(int j = 0; j < size; j++ ){
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }
}

vector<int> matrixTS(int **matrix, int size) {
    vector<int> stack;
    vector<int> path;
    
    bool *visited = (bool*)malloc(size * sizeof(bool));
    for(int i = 0; i < size; i++) {
        visited[i] = false;
    }

    int lastVertex = 0;
    visited[0] = true;
    path.push_back(lastVertex);

    while(stack.size() < size) {
        while(true) {
            int tmp = firstUnvisitedNeighbour(matrix, lastVertex, size, visited);
            if(tmp > -1) {
                lastVertex = tmp;
                path.push_back(lastVertex);
            } else {
                if(std::find(stack.begin(), stack.end(), lastVertex) != stack.end()) {
                    for(int i = 0; i < size; i++) {
                        if(visited[i] == false) {
                            lastVertex = i;
                            visited[i] = true;
                            path.push_back(lastVertex);
                            break;
                        }
                    }
                } else {
                    stack.push_back(lastVertex);
                    if(!path.empty()) {
                        path.pop_back();
                    }
                }
                break;       
            }
        }
        if(!path.empty()) {
            lastVertex = path.back();
        }
    }

    return stack;
}

int firstUnvisitedNeighbour(int **matrix, int vertex, int size, bool *visited) {
    int neighbour = -1;
    for(int i = 0; i < size; i++) {
        if(matrix[vertex][i] > 0 && visited[i] == false) {
            visited[i] = true;
            neighbour = i;
            break;
        }
    }

    return neighbour;
}

void printTS(processedElem* start)
{
    cout << "Topological sort: " << endl;
    processedElem* list= start;
    while(list!=NULL)
    {
        cout << list->elem->value << " > ";        
        list = list->next;
    }
    cout<<endl;

}

void printTSMatrix(vector<int> ts)
{
    cout << "Topological sort matrix: " << endl;
    for (vector<int>::size_type i = 0; i < ts.size(); i++)
    {
        cout << ts.at(i) << " > ";
    }
    cout<<endl;

}
