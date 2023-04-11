def sortByCost(dict):
    # Sort dictionary by value in descending order to dictionary
    desc = {}
    for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        desc[key] = value
    return desc

def deletePath(path, goal):
    tempPath = []
    tempPath.append(goal)
    for i in range(len(path)):
        if goal == list(path.keys())[i]:
            current = list(path.values())[i]
            tempPath.append(current)
            while (current != list(path.keys())[0]):
                for j in range(len(path)):
                    if current == list(path.keys())[j]:
                        current = list(path.values())[j]
                        tempPath.append(current)
    tempPath.reverse()
    return tempPath

def ucs(matrix, start, goal, node):
    queue = {}
    path = {}
    cost = {}
    queue.update({start: -1})
    path[start] = [-1]
    cost[-1] = -1
    while queue:
        queue = sortByCost(queue)
        current = queue.popitem()
        currentPoint = current[0]
        currentCost = current[1]
        # print("sedang dicek : ",currentPoint)
        for i in range(len(matrix)):
            if matrix[node.index(currentPoint)][i] != 0:
                if node[i] not in path:
                    queue.update({node[i]: matrix[node.index(currentPoint)][i]})
                    # print("dimasukkan ke antrian untuk dicek :", queue)
                    path.update({node[i]: currentPoint})
                    # print("dimasukkan ke path :", path)
                    cost.update({matrix[node.index(currentPoint)][i] : currentCost})
        if currentPoint == goal:
            break
    path = deletePath(path, goal)
    cost = deletePath(cost, currentCost)
    cost.remove(cost[0])
    return path, cost
