# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def create_graph(n):
    graph = []
    for i in range(n):
        number_edges = random.randint(1, n - 1)
        graph.append([])
        l = 0
        while l < number_edges:
            vertex = random.randint(0, n - 1)
            if vertex != i and vertex not in graph[i]:
                graph[i].append(vertex)
                l += 1
    return graph


def dfs(graph, start, visited=[]):
    visited.append(start)
    for el in graph[start]:
        if el not in visited:
            dfs(graph, el, visited)
    return visited


count = int(input('Введите количество вершин: '))
input_point = int(input('Введите точку входа: '))

my_graph = create_graph(count)
print('Граф', *my_graph, sep='\n')
print('Обход графа: ', dfs(my_graph, input_point))
