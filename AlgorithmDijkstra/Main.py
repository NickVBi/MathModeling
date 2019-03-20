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
        self.G = nx.relabel_nodes(self.G, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5})
        self.setColor();

    def setColor(self, red_edges = []):

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


    def DijkstraAlg(self, countNode, startNode, matrix):

        nodes = matrix2dictionary(matrix)
        l = [float('inf')] * len(matrix)
        _l = [False] * len(matrix)
        l[startNode] = 0
        _l[startNode] = True

        minWayResult = [[]] * countNode

        for node in nodes.keys():
            minIndex = node
            for j, weight in nodes[node].items():
                l[j] = min(l[j], l[node] + weight)
                if node == minIndex or l[j] < l[minIndex]:
                    minIndex = j
                minWayResult[j] = (minWayResult[node] or [startNode + 1]) + [j + 1]
            _l[minIndex] = True

        return minWayResult, l


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


                        red_enge.append((i + 1, j + 1))
                        self.setColor(red_enge)
        return weightResult, minWayResult
        # valid = [True]*N
        # weight = [100000]*N
        # weight[S] = 0
        # red_enge = []
        # for i in range(N):
        #     min_weight = 1000001
        #     ID_min_weight = -1
        #     for i in range(len(weight)):
        #         if valid[i] and weight[i] < min_weight :
        #             min_weight = weight[i]
        #             ID_min_weight = i
        #     for i in range(N):
        #         if matrix[ID_min_weight][i] != 0 and weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
        #             weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        #             red_enge.append((ID_min_weight + 1, i + 1))
        #             self.setColor(red_enge)
        #     valid[ID_min_weight] = False
        # return weight


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
    n = 5
    s = 0
    matrix = [[0, 4, 7, 12, 0],
                [0, 0, 2, 8, 5],
                [0, 0, 0, 0, 2],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]]
    dijkstraObj = DijkstraDraw(matrix)
    res = dijkstraObj.DijkstraAlg(n, s, matrix)
    print(res)
    # print(ways)

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