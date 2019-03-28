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

def getNodeTo(nodes, index):
    return nodes[index].keys()

class DijkstraDraw:

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


    def DijkstraAlg(self, startNode, matrix):
        countNode = len(matrix)
        nodes = matrix2dictionary(matrix)
        l = [float('inf')] * countNode
        _l = [False] * countNode
        l[startNode] = 0
        _l[startNode] = True

        minWayResult = [[]] * countNode

        for node in nodes.keys():
            minIndex = node
            for j, weight in nodes[node].items():
                if l[node] + weight < l[j]:
                    l[j] = l[node] + weight
                    if l[j] < l[minIndex]:
                        minIndex = j
                    minWayResult[j] = (minWayResult[minIndex] or [startNode + 1]) + [j + 1]
            _l[minIndex] = True

        return minWayResult, l

        countNode = len(matrix)
        weightResult = [float('inf')] * countNode
        minWayResult = [[]] * countNode
        weightResult[startNode] = 0
        minWayResult[startNode] = 0
        checkedNode = [True] * countNode
        red_enge = []
        for i, node in enumerate(matrix):
            if checkedNode[i]:
                # idMinWeight = i
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
    dijkstraObj = DijkstraDraw(matrix)
    res, ways = dijkstraObj.DijkstraAlg(n, s, matrix)
    if e is not None or e != s:
        print(res[e])
        print(ways[e])
    else:
        print(res)
        print(i for i in ways)


def test():
    n = 6
    s = 0
    matrix = [[0, 7, 2, 0, 13, 0],
              [0, 0, 0, 0, 6, 0],
              [0, 2, 0, 1, 3, 11],
              [0, 0, 0, 0, 0, 5],
              [0, 0, 0, 3, 0, 5],
              [0, 0, 0, 0, 0, 0]
              ]
    dijkstraObj = DijkstraDraw(matrix)
    ways, res = dijkstraObj.DijkstraAlg(s, matrix)
    for i in range(1, len(ways)):
        dijkstraObj.setColor(ways[i])
    print(res)
    print(ways)

def testNode():
    matrix = [[0, 4, 7, 12, 0],
              [0, 0, 2, 8, 5],
              [0, 0, 0, 0, 2],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0]]
    nodes = matrix2dictionary(matrix)
    print(nodes)
    nd = getNodeTo(nodes, 0)
    print(nd)


if __name__ == "__main__":
    test()