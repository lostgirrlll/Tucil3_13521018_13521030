import networkx as nx
import matplotlib.pyplot as plt

from inputFile import *

# membuat graph dari file inputFile.py
def createGraph(node, matrix):
    graph = nx.Graph()
    for i in range(len(node)):
        graph.add_node(node[i])
    for i in range(len(node)):
        for j in range(len(node)):
            if matrix[i][j] != 0:
                graph.add_edge(node[i], node[j], weight=matrix[i][j])
    return graph

# menampilkan graph
def showGraph(graph, arr):
    listpost = []
    position = nx.spring_layout(graph)
    position = arr
    listpost.append(position)
    nx.draw(graph, position, with_labels=True, node_color='green', node_size=300, edge_color='black', width=2, font_size=8)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, position, edge_labels=labels, font_size=8, label_pos=0.5, rotate=False, font_color='red', font_weight='bold')
    plt.show()
    return listpost
