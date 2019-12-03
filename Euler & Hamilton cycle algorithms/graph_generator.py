#!/usr/bin/python
import random
import time
import sys
import resource

class GraphMatrix:
    def set_density(self, density):
        size = len(self.matrix)
        density = (int(density*self.size))**2
        print("density " + str(density))
        for i in range(density):
            row = random.randrange(0, size)
            column = random.randrange(0, size)
            while self.matrix[row][column] == 0:
                row = random.randrange(0, size)
                column = random.randrange(0, size)

            
            self.matrix[row][column] = 0

    def get_random_vertex(self, available):
        return available[random.randrange(0, len(available))]

    def generate_cycle(self):
        available_vertices = []
        for i in range(len(self.matrix[0])):
            available_vertices.append(i)

        vertex_a = self.get_random_vertex(available_vertices)
        first_vertex = vertex_a
        while len(available_vertices) != 0:
            if len(available_vertices) == 1:
                vertex_b = first_vertex
            else:
                vertex_b = self.get_random_vertex(available_vertices)
                while vertex_a == vertex_b:
                    vertex_b = self.get_random_vertex(available_vertices)

            available_vertices.remove(vertex_a)
            
            self.add_edge(vertex_a, vertex_b)
            vertex_a = vertex_b

    def add_edge(self, vertex_a, vertex_b):
        self.matrix[vertex_a][vertex_b] = 1
        self.matrix[vertex_b][vertex_a] = 1
        self.number_of_edges += 1

    def get_number_of_edges(self):
        number_of_edges = 0
        for row in self.matrix:
            for element in row:
                if element != 0:
                    number_of_edges += 1

        return number_of_edges // 2

    def edge_exists(self, vertex_a, vertex_b):
        edge_to = self.matrix[vertex_a][vertex_b]
        edge_from = self.matrix[vertex_b][vertex_a]
        if edge_from > 0 and edge_to > 0:
            return True
        else:
            return False

    def generate_additional_edges(self):
        size = self.size
        size = (size * (size - 1)) / 2
        size *= self.density

        while size > self.number_of_edges:
            x = random.randrange(0, self.size)
            y = random.randrange(0, self.size)
            z = random.randrange(0, self.size)
            if x!=y and x!=z and y!=z and (not self.edge_exists(x,y)) and (not self.edge_exists(y,z)) and (not self.edge_exists(z,x)):
                self.add_edge(x,y)
                self.add_edge(y,z)
                self.add_edge(x,z)

    def find_first_unvisited_euler_vertex(self, vertex):
        for i in range(len(vertex)):
            if vertex[i] == 1:
                return i
        return -1

    def generate_euler_cycle(self, vertex):
        next_vertex = self.find_first_unvisited_euler_vertex(self.matrix[vertex])
        while next_vertex >= 0:
            self.matrix[vertex][next_vertex] = 2
            self.matrix[next_vertex][vertex] = 2
            self.generate_euler_cycle(next_vertex)
            next_vertex = self.find_first_unvisited_euler_vertex(self.matrix[vertex])
        self.euler_cycle.append(vertex)


    def repair_graph(self):
        for i in len(self.matrix):
            for j in len(i):
                if self.matrix[i][j] > 1:
                    self.matrix[i][j] = 1

    def __init__(self, size, density):
        self.hamilton_cycles = []
        self.size = size
        self.density = density
        self.number_of_edges = 0
        self.euler_cycle = []
        self.single_found = False

        matrix = []
        for i in range(size):
            matrix.append([])
            for j in range(size):
                matrix[i].append(0)
        
        self.matrix = matrix
        self.generate_cycle()
        self.generate_additional_edges()
        #self.set_density(density)

    def print_matrix(self):
        print("   "+str([i for i in range(self.size)]))
        i=0
        for row in self.matrix:
            print(str(i)+": "+str(row))
            i+=1

    def get_first_unvisited_neighbour(self, vertex, visited):
        for v in range(len(self.matrix[vertex])):
            if v not in visited and self.matrix[vertex][v] != 0:
                return v
        return -1

    def get_all_unvisited_neighbours(self, vertex, visited):
        unvisited = []
        for v in range(len(self.matrix[vertex])):
            if v not in visited and self.matrix[vertex][v] != 0:
                unvisited.append(v)
        return unvisited

    def hamilton_single_cycle(self, vertex, visited, source_vertex):
        visited.append(vertex)
        neighbours = self.get_all_unvisited_neighbours(vertex, visited)
        if self.single_found == False:

            for v in neighbours:
                self.hamilton_single_cycle(v, visited, source_vertex)
                if self.single_found == True:
                    return 0

            if self.contains_all_vertices(visited) and self.matrix[vertex][source_vertex] != 0:
                self.hamilton_cycle_single = visited.copy()
                self.single_found = True
                visited.remove(vertex)

            else:
                visited.remove(vertex)

    def hamilton(self, vertex, visited,source_vertex):
        visited.append(vertex)
        neighbours = self.get_all_unvisited_neighbours(vertex, visited)
        #next_vertex = self.get_first_unvisited_neighbour(vertex, visited)

        # while next_vertex >= 0:
        #     self.hamilton(next_vertex, visited, source_vertex)
        #     next_vertex = self.get_first_unvisited_neighbour(vertex, visited)
        for v in neighbours:
            self.hamilton(v, visited, source_vertex)
            
        if self.contains_all_vertices(visited) and self.matrix[vertex][source_vertex] != 0:
            #print(visited)
            self.hamilton_cycles.append(visited.copy())
            visited.remove(vertex)

        else:
            visited.remove(vertex)

    def generate_hamiltian_cycle(self, source_vertex):
        visited = []
        self.hamilton(source_vertex,visited,source_vertex)
        #self.hamilton_cycle = visited

    def generate_hamiltian_single_cycle(self, source_vertex):
        visited = []
        self.hamilton_single_cycle(source_vertex, visited, source_vertex)

    def contains_all_vertices(self, visited):
        for v in range(len(self.matrix[0])):
            if v not in visited:
                return False
        
        return True


times = []
# resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
# sys.setrecursionlimit(10**6)
# for i in range(50, 200, 10):
#     graph = GraphMatrix(i, 0.3)
#     start_time = time.time()
#     graph.generate_euler_cycle(0)
#     stop_time = time.time()
#     times.append(stop_time - start_time)

# print("Euler 30%: " + str(times))

# times.clear()
# for i in range(50, 200, 10):
#     graph = GraphMatrix(i, 0.7)
#     start_time = time.time()
#     graph.generate_euler_cycle(0)
#     stop_time = time.time()
#     times.append(stop_time - start_time)

# print("Euler 70%: " + str(times))
# times.clear()
# for i in range(50, 200, 10):
#     graph = GraphMatrix(i, 0.7)
#     start_time = time.time()
#     graph.generate_hamiltian_single_cycle(0)
#     stop_time = time.time()
#     times.append(stop_time - start_time)

# print("Hamilton 70%: " + str(times))
# times.clear()

for i in range(160, 200, 10):
    graph = GraphMatrix(i, 0.3)
    print("Generating " + str(i) + " vertices cycles")
    start_time = time.time()
    graph.generate_hamiltian_single_cycle(0)
    stop_time = time.time()
    times.append(stop_time - start_time)

print("Hamilton 30%: " + str(times))
times.clear()

# for i in range(6, 17):
#     graph = GraphMatrix(i, 0.5)
#     print("Generating " + str(i) + " vertices cycles")
#     start_time = time.time()
#     graph.generate_hamiltian_cycle(0)
#     stop_time = time.time()
#     times.append(stop_time - start_time)

# print("Hamilton ALL 50%: " + str(times))
# #graph.print_matrix()
# graph.generate_euler_cycle(0)
# #print("Euler: " + str(graph.euler_cycle))
# print("Hamilton: " + str(graph.hamilton_cycles))
