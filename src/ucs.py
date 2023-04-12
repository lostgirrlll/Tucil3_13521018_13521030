from visualisasi import *
from inputFile import *
# sort by a cost value
def sortByCost(dict):
    sorted_tuples = sorted(dict.items(), key=lambda x:-list(x[1].values())[0], reverse=False)
    sorted_dict = {t[0]:t[1] for t in sorted_tuples}
    return sorted_dict

# Uniform Cost Search
def ucs(matrix, start, goal, node):
    visited = []
    queue = {}
    path = []
    queue.update({(0, start) : {'': 0}})
    path.append(start)
    visited.append(start)
    j = 0
    while queue:
        queue = sortByCost(queue)
        path = queue.popitem()
        currNode = path[0][1]
        visited.append(currNode)
        currPath = list(path[1].keys())[0]
        currCost = list(path[1].values())[0]
        for i in range(len(matrix)):
            if matrix[node.index(currNode)][i] != 0:
                if node[i] not in visited:
                    queue.update({(j, node[i]) : {currPath + "," + node[i] : currCost + matrix[node.index(currNode)][i]}})
        j += 1
        if currNode == goal:
            break
    cost = list(path[1].values())[0]
    path = (start + list(path[1].keys())[0]).split(',')
    return path, cost

def getUCS(matrix, matrixDist, node, start, goal, point):
    art("UCS")
    pathUCS, costUCS = ucs(matrix, start, goal, node)
    if (start not in pathUCS or goal not in pathUCS):
        print("\t Tidak ada jalur yang dapat ditempuh.")
    else:
        print("\t Path : ", end="")
        strpath = ""
        for i in range(len(pathUCS) - 1):
            strpath = strpath + pathUCS[i] + " -> "
            print(pathUCS[i], end=" -> ")
        print(goal)
        print("\t Jarak : ", costUCS)
        print("\t Menampilkan Graph...")
        # membuat cost untuk graph
        cost = []
        for i in range(len(pathUCS)):
            cost.append(matrixDist[node.index(pathUCS[i])][node.index(goal)])
        # membuat matrix yang menghubungkan path
        mat = matrixPath(pathUCS, node, cost)
        showGraph(createGraph(node, 0, matrix, "initial"), arrKoordinat(node, point), createGraph(node, pathUCS, mat, "ucs_aStar"), "ucs", strpath + goal, costUCS)