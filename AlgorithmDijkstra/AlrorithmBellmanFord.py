import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def matrix2dictionary(matrix):
    nodes = {}

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]:
                # nodes[(i, j)] = matrix[i][j]
                if i in nodes:
                    nodes[i][j] = matrix[i][j]
                else:
                    nodes[i] = {j: matrix[i][j]}
    return nodes


class BellmanFordDraw:

    def __init__(self, matrix):
        self.G = nx.DiGraph()
        self.m = np.matrix(matrix)

        self.G = nx.from_numpy_matrix(self.m, create_using=nx.DiGraph(directed=True))
        self.G.edges(data=True)
        dist = {i: i + 1 for i in range(len(matrix))}
        self.G = nx.relabel_nodes(self.G, dist)
        self.setColor();

    def setColor(self, ways = []):
        red_edges = [(ways[i], ways[i + 1]) for i in range(len(ways) - 1)]
        edge_labels = dict([((u, v,), d['weight'])
                            for u, v, d in self.G.edges(data=True)])
        edge_colors = ['black' if not edge in red_edges else 'red' for edge in self.G.edges()]

        pos = nx.shell_layout(self.G)
        nx.draw_networkx_edge_labels(self.G,
                                     pos,
                                     edge_labels=edge_labels)
        nx.draw(self.G,
                pos,
                with_labels=True,
                node_size=1500,
                edge_color=edge_colors)
        plt.show()

    def BellmanFordAlg(self, startNode, matrix):
        countNode = len(matrix)
        nodes = matrix2dictionary(matrix)
        l = [float('inf')] * len(matrix)
        _l = [False] * len(matrix)
        l[startNode] = 0
        _l[startNode] = True
        Q = [startNode]
        minWayResult = [[]] * countNode
        while Q:
            q = Q[0]
            Q.remove(q)
            if q not in nodes:
                continue
            for j, weight in nodes[q].items():
                if l[j] > l[q] + weight:
                    l[j] = l[q] + weight
                    if j in Q:
                        Q.remove(j)
                        Q.insert(0, j)
                    else:
                        Q.append(j)
                    minWayResult[j] = (minWayResult[q] or [startNode + 1]) + [j + 1]

        print()
        return l, minWayResult


        weightResult = [float('inf')] * countNode
        minWayResult = [[]] * countNode
        weightResult[startNode] = 0
        minWayResult[startNode] = 0
        checkedNode = [True] * countNode

        for i, node in enumerate(matrix):
            if checkedNode[i]:
                checkedNode[i] = False
                for j, weight in enumerate(node):
                    if checkedNode[j] and weight and weightResult[j] > weightResult[i] + weight:
                        weightResult[j] = weightResult[i] + weight
                        minWayResult[j] = (minWayResult[i] or [startNode + 1]) + [j + 1]
        return weightResult, minWayResult


def main():
    n = int(input("Number of node: "))
    s = int(input("Start node: "))
    e = int(input("Finish node: "))
    matrix = [[i].slice(',') for i in input("Weight matrix: ")]
    bellmanFordObj = BellmanFordDraw(matrix)
    res, ways = bellmanFordObj.BellmanFordAlg(n, s, matrix)
    if e is not None or e != s:
        print(res[e])
        print(ways[e])
    else:
        print(res)
        print(i for i in ways)

def test():
    n = 6
    s = 0
    e = 5
    matrix = [[0, 4, 0, 15, 8, 0, 0],
              [0, 0, 5, 0, 0, 0, 0],
              [0, 0, 0, 0, 9, 0, 7],
              [0, 0, 4, 0, 10, -6, 0],
              [0, 0, 5, 0, 0, 7, 16],
              [0, -18, 7, 0, 0, 0, 6],
              [0, 0, 0, 0, 0, 0, 0],
              ]
    bellmanFordObj = BellmanFordDraw(matrix)
    res, ways = bellmanFordObj.BellmanFordAlg(s, matrix)

    for i in range(1, len(ways)):
        bellmanFordObj.setColor(ways[i])
    print(res)
    print(ways)


if __name__ == "__main__":
    test()