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
        dist = {i: i + 1 for i in range(len(matrix))}
        self.G = nx.relabel_nodes(self.G, dist)
        self.setColor();

    def setColor(self, ways = []):
        red_edges = [(ways[i + 1], ways[i]) for i in range(len(ways) - 1)]
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

        minWayResult = [[]] * n

        for i in range(n - 1):
            v[0][i] = algMatrix[i][n - 1]
            minWayResult[i] = [n] + ([i + 1] if matrix[i][n - 1] > 0 else [])
        k = 0

        while not k or v[k] != v[k - 1]:
            k += 1
            v += [[0] * n]
            for i in range(n - 1):
                #v[k][i] = max([algMatrix[i][j] + v[k - 1][j] for j in range(n)])
                max_t = 0
                max_j = 0
                for j in range(n):
                    t = algMatrix[i][j] + v[k - 1][j]
                    if (t > max_t):
                        max_t = t
                        max_j = j
                v[k][i] = max_t
                minWayResult[i] = minWayResult[max_j] + ([max_j + 1] if (max_j + 1 ) not in minWayResult[max_j] else [])

        return minWayResult, v




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
    matrix = [[0, 4, 15, 8, 0, 0, 0],
              [0, 0, 5, 0, 0, 0, 0],
              [0, 0, 0, 0, 9, 0, 7],
              [0, 0, 0, 0, 10, 6, 0],
              [0, 0, 0, 0, 0, 7, 16],
              [0, 0, 0, 0, 0, 0, 6],
              [0, 0, 0, 0, 0, 0, 0]]
    bellmanKalabaObj = BellmanKalabaDraw(matrix)
    ways, res = bellmanKalabaObj.BellmanKalabaAlg(matrix)

    for i in range(len(ways)):
        bellmanKalabaObj.setColor(ways[i])
    for i in ways:
        print(i)
    for i in res:
        print(i)


if __name__ == "__main__":
    test()