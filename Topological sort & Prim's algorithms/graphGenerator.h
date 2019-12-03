#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
#include <ctime>
#include <iostream>

using namespace std;

typedef struct ILGraph ILGraph;
typedef struct VertexListElem VertexListElem;

VertexListElem *addElementToList(VertexListElem *root, ILGraph *value, int weight);
VertexListElem *removeFromList(VertexListElem *root, ILGraph *value);
bool edgeExists(VertexListElem *tmp, ILGraph *searchedElem);

ILGraph **shuffleGraph(ILGraph **graph, int size);
ILGraph **generateGraph(int size, float density);
ILGraph **deleteRandEdges(ILGraph **graph, int size, float density);

int **generateGraphMatrix(ILGraph **graph, int size);
void printGraph(ILGraph **graph, int size);

struct VertexListElem //edge
{
	ILGraph *vertex; //vertex that this edge points at
	int weight;		 //weight of this edge

	VertexListElem *next; //next edge on the list
};

struct ILGraph //vertex
{
	int value;			  //value of this vertex
	int in;				  //obvious
	int out;			  //so it is
	VertexListElem *list; //list of edges coming out of this vertex
};

VertexListElem *addElementToList(VertexListElem *start, ILGraph *value, int weight)
{
	VertexListElem *newElement = (VertexListElem *)malloc(sizeof(VertexListElem));
    newElement->next = NULL;
	newElement->vertex = value;
	newElement->weight = weight;

	if (!start)
	{
		start = newElement;
		return newElement;
	}

	if (value->value < start->vertex->value)
	{
		newElement->next = start;
		start = newElement;
		return newElement;
	}
	if(value->value == start->vertex->value)
	{
		return start;
	}
	VertexListElem *lastElement = start;
	VertexListElem *currentElement = start->next;
	while (currentElement != NULL)
	{
        if(value->value == currentElement->vertex->value)
	    {
            currentElement->weight = weight;
		    return start;
	    }
		if (currentElement->vertex->value > value->value)
		{
			newElement->next = currentElement;
			lastElement->next = newElement;
			break;
		}
		lastElement = currentElement;
		currentElement = currentElement->next;
	}
    if(lastElement->next == NULL) {
        lastElement->next = newElement;
    }
	return start;
};

VertexListElem *removeFromList(VertexListElem *root, ILGraph *value)
{
	VertexListElem *search = root;
	VertexListElem *tmp;
    if(root == NULL) {
        return NULL;
    }
	if (root->vertex == value)
	{
		tmp = root->next;
		free(root);
		return tmp;
	}

	while (search->next != NULL && search->next->vertex != value)
	{
		search = search->next;
	}
	if (search->next == NULL)
	{
		return root;
	}

	if (search->next->vertex == value)
	{
		tmp = search->next->next;
		free(search->next);
		search->next = tmp;
	}

	return root;
}

ILGraph **shuffleGraph(ILGraph **graph, int size)
{
	ILGraph *tmp;
	int randomElement;

	for (int i = 0; i < size; i++)
	{
		tmp = graph[i];
		randomElement = rand() % size;
		graph[i] = graph[randomElement];
		graph[randomElement] = tmp;
	}
	return graph;
}

ILGraph **generateGraph(int size, float density)
{
	ILGraph **graph = (ILGraph **)malloc(size * sizeof(ILGraph *));

	for (int i = 0; i < size; i++)
	{
		graph[i] = (ILGraph *)malloc(sizeof(ILGraph));
	}

	for (int i = 0; i < size; i++)
	{
		graph[i]->value = i + 1;
		graph[i]->in = 0;
		graph[i]->out = 0;
	}

	graph = shuffleGraph(graph, size);

	for (int i = 0; i < size; i++)
	{
		for (int j = i; j < size; j++)
		{
			if (i != j)
			{
				graph[i]->list = addElementToList(graph[i]->list, graph[j], rand() % 1000 + 1);
				graph[j]->in++;
				graph[i]->out++;
			}
		}
	}
	graph = deleteRandEdges(graph, size, density);
	return graph;
}

ILGraph **deleteRandEdges(ILGraph **graph, int size, float density)
{
	int edgesToDelete = ((size * (size - 1)) / 2);
	// cout << "edgesToDelete * density: " << (int)(edgesToDelete * density) << endl;

	edgesToDelete *= 1 - density;
	//cout << "edgesToDelete: " << edgesToDelete << endl;

	int edgeFrom, edgeTo;

	for (int i = 0; i < edgesToDelete; i++)
	{
		do
		{
			edgeFrom = rand() % size;
			edgeTo = rand() % size;
		} while (
			edgeFrom == edgeTo || graph[edgeFrom]->out <= 1 || graph[edgeTo]->in <= 1 || (!edgeExists(graph[edgeFrom]->list, graph[edgeTo]))

		);
		// ILGraph *tmp1 = graph[edgeFrom];
		// ILGraph *tmp2 = graph[edgeTo];
		graph[edgeFrom]->list = removeFromList(graph[edgeFrom]->list, graph[edgeTo]);
		graph[edgeFrom]->in--;
		graph[edgeTo]->out--;
	}

	return graph;
}

ILGraph **sortGraph(ILGraph **graph, int size)
{
	ILGraph **sortedGraph = (ILGraph **)malloc(size * sizeof(ILGraph *));
	for (int i = 0; i < size; i++)
	{
		sortedGraph[graph[i]->value - 1] = graph[i];
	}
	return sortedGraph;
}
int **generateGraphMatrix(ILGraph **graph, int size)
{
	ILGraph **sortedGraph = sortGraph(graph, size);
	VertexListElem *listElement;
	int vertexNumber;
	int **matrix = (int **)malloc(size * sizeof(int *));
	for (int i = 0; i < size; i++)
	{
		matrix[i] = (int *)malloc(size * sizeof(int));
		for (int j = 0; j < size; j++)
		{
			matrix[i][j] = 0;
		}
		listElement = sortedGraph[i]->list;
		while (listElement != NULL)
		{
			vertexNumber = listElement->vertex->value - 1;
			matrix[i][vertexNumber] = listElement->weight;
			listElement = listElement->next;
		}
	}

	return matrix;
}
int counter = 0;
void printGraph(ILGraph **graph, int size)
{
	for (int i = 0; i < size; i++)
	{
		cout << "Vertex nr. " << i << ": " << graph[i]->value << endl;
		cout << "\tPrinting edges" << endl;
		VertexListElem *search = graph[i]->list;
		while (search != NULL)
		{
			cout << "\t\t" << search->vertex->value << "\t" << search->weight << endl;
			counter++;
			search = search->next;
		}
	}
	cout << "Number of edges: " << counter << endl;
}
void printGraphMatrix(int** graph, int SIZE)
{
    for (int i = 0; i < SIZE; i++)
    {
        for (int k = 0; k < SIZE; k++)
        {
            cout << graph[i][k] << "\t";
        }
        cout << endl;
    }
}

bool edgeExists(VertexListElem *tmp, ILGraph *searchedElem)
{
	VertexListElem *list = tmp;
	while (list != NULL)
	{
		if (list->vertex == searchedElem)
		{
			return true;
		}
		list = list->next;
	}
	return false;
}

void removeList(VertexListElem *list)
{
	VertexListElem *tmpList;
	while (list != NULL)
	{
		tmpList = list->next;
		free(list);
		list = tmpList;
	}
}
void removeGraph(ILGraph **graph, int size)
{
	for (int i = 0; i < size; i++)
	{
		removeList(graph[i]->list);
		free(graph[i]);
	}
	free(graph);
}
void removeMatrix(int **matrix, int size)
{
	for (int i = 0; i < size; i++)
	{

		free(matrix[i]);
	}
	free(matrix);
}

ILGraph **deleteUndirectedRandEdges(ILGraph **graph, int size, float density)
{
    int edgesToDelete = ((size * (size - 1)) / 2);
    cout << "edgesToDelete * density: " << (int)(edgesToDelete * density) << endl;

    edgesToDelete *= 1 - density;
    //cout << "edgesToDelete: " << edgesToDelete << endl;

    int edgeFrom, edgeTo;

    for (int i = 0; i < edgesToDelete; i++)
    {
        do
        {
            edgeFrom = rand() % size;
            edgeTo = rand() % size;
        } while (
			edgeFrom == edgeTo || graph[edgeFrom]->out <= 1 || graph[edgeTo]->in <= 1 || (!edgeExists(graph[edgeFrom]->list, graph[edgeTo])) ||  (!edgeExists(graph[edgeTo]->list, graph[edgeFrom]))
            //            || !edgeExists(graph[edgeFrom]->list, graph[edgeTo])
        );
        // ILGraph *tmp1 = graph[edgeFrom];
        // ILGraph *tmp2 = graph[edgeTo];
        graph[edgeFrom]->list = removeFromList(graph[edgeFrom]->list, graph[edgeTo]);
        graph[edgeFrom]->in--;
        graph[edgeTo]->out--;

        graph[edgeTo]->list = removeFromList(graph[edgeTo]->list, graph[edgeFrom]);
        graph[edgeTo]->in--;
        graph[edgeFrom]->out--;
    }

    return graph;
}

ILGraph **generateUndirectedGraph(int size, float density)
{
    ILGraph **graph = (ILGraph **)malloc(size * sizeof(ILGraph *));

    for (int i = 0; i < size; i++)
    {
        graph[i] = (ILGraph *)malloc(sizeof(ILGraph));
        graph[i]->list = NULL;
        graph[i]->value = i + 1;
        graph[i]->in = 0;
        graph[i]->out = 0;
    }

    graph = shuffleGraph(graph, size);

	// VertexListElem *list;
    int weight;
    for (int i = 0; i < size; i++)
    {
        // list = graph[i]->list;
        // while(list != NULL) {
        //     list->vertex->list = addElementToList(list->vertex->list, graph[i], list->weight);
        //     list = list->next;
        // }
        for (int j = i; j < size; j++)
        {
            if (i != j)
            {
                weight =  rand() % 1000 + 1;
                graph[i]->list = addElementToList(graph[i]->list, graph[j], weight);
                graph[j]->in++;
                graph[i]->out++;
                graph[j]->list = addElementToList(graph[j]->list, graph[i], weight);
                graph[i]->in++;
                graph[j]->out++;
            }
        }
    }
    graph = deleteUndirectedRandEdges(graph, size, density);

    return graph;
}