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
def showGraph(graph, arr, finalGraph, string, path, cost):
    position = nx.spring_layout(graph)
    position = arr
    if (string == "initial"):
        nx.draw(graph, position, with_labels=True, node_color='green', node_size=300, edge_color='grey', width=2, font_size=8)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, position, edge_labels=labels, font_size=8, label_pos=0.5, rotate=False, font_color='black', font_weight='bold')
        fig = plt.gcf()
        fig.suptitle('Initial Graph', fontsize=16, fontweight='bold')
    elif (string == "ucs"):
        # print(finalGraph.edges)
        # print(finalGraph)
        edge_colors = ['red' if edge in finalGraph.edges else 'grey' for edge in graph.edges()]
        nx.draw(graph, position, with_labels=True, node_color='green', node_size=300, edge_color=edge_colors, width=2, font_size=8)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, position, edge_labels=labels, font_size=8, label_pos=0.5, rotate=False, font_color='black', font_weight='bold')
        for i in range(len(finalGraph.nodes)):
            nx.draw_networkx_nodes(finalGraph, position, nodelist=[list(finalGraph.nodes)[i]], node_color='blue', node_size=500)
        fig = plt.gcf()
        fig.suptitle('UCS Graph', fontsize=16, fontweight='bold')
        fig.text(0.02, 0.05, 'Path: ' + str(path), fontsize=5, fontweight='bold', color='black', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
        fig.text(0.02, 0.02, 'Cost: ' + str(cost), fontsize=5, fontweight='bold', color='black', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))
    elif (string == "a*"):
        edge_colors = ['red' if edge in finalGraph.edges else 'grey' for edge in graph.edges()]
        nx.draw(graph, position, with_labels=True, node_color='green', node_size=300, edge_color=edge_colors, width=2, font_size=8)
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, position, edge_labels=labels, font_size=8, label_pos=0.5, rotate=False, font_color='black', font_weight='bold')
        for i in range(len(finalGraph.nodes)):
            nx.draw_networkx_nodes(finalGraph, position, nodelist=[list(finalGraph.nodes)[i]], node_color='blue', node_size=500)
        fig = plt.gcf()
        fig.suptitle('A* Graph', fontsize=16, fontweight='bold')
        fig.text(0.01, 0.01, 'Path: ' + str(path) + ' Cost: ' + str(cost), fontsize=8)
    plt.show()