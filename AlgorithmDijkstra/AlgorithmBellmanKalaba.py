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

def matrix2algForm(matrix):

    n = len(matrix)

    resMatrix = matrix.copy()

    for i in range(n):
        for j in range(n):
            if i != j and not resMatrix[i][j]:
                resMatrix[i][j] = float('-inf')

    # resMatrix = [[float('inf')] * n] * n
    #
    # for i in range(n):
    #     for j in range(n):
    #         if i == j or matrix[i][j]:
    #             resMatrix[i][j] = matrix[i][j]

    return resMatrix

class BellmanKalabaDraw:

    def __init__(self, matrix):
        self.G = nx.DiGraph()
        self.m = np.matrix(matrix)

        self.G = nx.from_numpy_matrix(self.m, create_using=nx.DiGraph(directed=True))
        self.G.edges(data=True)
        # self.G = nx.relabel_nodes(self.G, {0: 1, 1: 2, 2: 3, 3: 4, 4: 5})
        self.setColor();

    def setColor(self, red_edges=[]):

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


    def BellmanKalabaAlg(self, matrix):

        algMatrix = matrix2algForm(matrix)
        n = len(matrix)
        v = [[0] * n]

        minWayResult = [[] * n]

        for i in range(n - 1):
            v[0][i] = algMatrix[i][n - 1]
            minWayResult.append([i])
        k = 0

        while not k or v[k] != v[k - 1]:
            k += 1
            v += [[0] * n]
            for i in range(n - 1):
                # v[k][i] = max([algMatrix[i][j] + v[k - 1][j] for j in range(n)])
                maxIndexJ = 0
                maxVal = 0
                for j in range(n):
                    maxVal = algMatrix[i][maxIndexJ] + v[k - 1][maxIndexJ]
                    if algMatrix[i][j] + v[k - 1][j] > maxVal:
                        maxIndexJ = j
                v[k][i] = maxVal
                if maxIndexJ not in minWayResult[maxIndexJ]:
                    minWayResult[maxIndexJ] += [i]
                # minWayResult[maxV] = (minWayResult[k] or [n - 1]) + [maxV]

        for i in minWayResult:
            print(i)
        return v




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
    matrix = [[0, 3, 9, 6, 0, 11, 0],
              [0, 0, 0, 5, 7, 0, 0],
              [0, 0, 0, 4, 0, 8, 0],
              [0, 0, 0, 0, 8, 3, 9],
              [0, 0, 0, 0, 0, 0, 11],
              [0, 0, 0, 0, 0, 0, 6],
              [0, 0, 0, 0, 0, 0, 0]]
    bellmanKalabaObj = BellmanKalabaDraw(matrix)
    res = bellmanKalabaObj.BellmanKalabaAlg(matrix)

    for i in res:
        print(i)


if __name__ == "__main__":
    test()