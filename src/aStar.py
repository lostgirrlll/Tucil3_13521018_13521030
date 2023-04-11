from queue import PriorityQueue

def aStar(node, matrix, matrixDist):
    start, goal = nodeValid(node)
    mat = matrixDist[goal]
    queue = PriorityQueue()
    path = []
    if (start == goal):
        path.append(node[start])
        dist = 0
    else :
        child = 1
        found = False
        path.append(node[start])
        for i in range(len(node)):
            if (matrix[start][i] > 0):
                queue.put((matrix[start][i] + mat[i], i, child))
        temp = queue.get()
        gn = matrix[start][temp[1]]
        while not (found):
            if (node[temp[1]] in path):
                temp = queue.get()
                gn = matrix[start][temp[1]]
            else :
                child += 1
                if (temp[1] == goal):
                    found = True
                    dist = temp[0]
                    path.append(node[temp[1]])
                else :
                    start = temp[1]
                    path.append(node[start])
                    tempGn = gn
                    for i in range(len(node)):
                        gn = tempGn
                        if (matrix[start][i] > 0):
                            gn += matrix[start][i]
                            queue.put((gn + mat[i], i, child))
                    temp1 = temp
                    temp = queue.get()
                    gn = temp[0] - mat[temp[1]]
                    if (temp[2] == temp1[2]):
                        gn -= matrix[start][temp[1]]
    return path, dist
                    

    
def nodeValid(node):
    flag = False
    while (not flag):
        start = input("Masukkan titik awal : ")
        if start in node:
            flag = True
            idxStart = node.index(start)
        else :
            print("Titik tidak ditemukan.")
            flag = False
    flag = False
    while (not flag):
        goal = input("Masukkan titik tujuan : ")
        if goal in node:
            flag = True
            idxGoal = node.index(goal)
        else :
            print("Titik tidak ditemukan.")
            flag = False
    return idxStart, idxGoal
