# sor by a cost value
def sortByCost(dict):
    sorted_tuples = sorted(dict.items(), key=lambda x:-list(x[1].values())[0], reverse=False)
    sorted_dict = {t[0]:t[1] for t in sorted_tuples}
    return sorted_dict

def ucs(matrix, start, goal, node):
    visited = []
    queue = {}
    path = []
    # currPath = []
    queue.update({(0, start) : {'': 0}})
    path.append(start)
    visited.append(start)
    j = 0
    while queue:
        queue = sortByCost(queue)
        # print("Sort by cost : ", queue)
        path = queue.popitem()
        # print("path :", path)
        currNode = path[0][1]
        visited.append(currNode)
        # print("visited :", visited)
        # print("dikunjungi :", currNode)
        currPath = list(path[1].keys())[0]
        # print("currpath :", currPath)
        currCost = list(path[1].values())[0]
        # print("currcost :", currCost)
    # queue = {node: {[path] : cost}}
        for i in range(len(matrix)):
            if matrix[node.index(currNode)][i] != 0:
                if node[i] not in visited:
                    # print("dimasukkan ke queue :", node[i])
                    # visited.append(node[i])
                    # print("visited :", visited)
                    queue.update({(j, node[i]) : {currPath + "," + node[i] : currCost + matrix[node.index(currNode)][i]}})
                    # print("queue :", queue)
        j += 1
        # print("----------------------------------------------------------------")
        if currNode == goal:
            break
    cost = list(path[1].values())[0]
    path = (start + list(path[1].keys())[0]).split(',')
    return path, cost