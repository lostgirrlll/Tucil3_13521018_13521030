from queue import PriorityQueue
import copy

def aStar(node, matrix, matrixDist, start, goal):
    start = node.index(start)
    goal = node.index(goal)
    mat = matrixDist[goal]
    queue = PriorityQueue()
    path = []
    listChild = []
    if (start == goal):
        path.append(0+mat[start], start, child, 0)
        dist = 0
    else :
        tempPath = []
        tempChild = []
        child = 0
        found = False
        temp = (0+mat[start], start, child, 0)
        listChild.append(temp[2])
        gn = matrix[start][temp[1]]
        while not (found):
            child += 1
            if (temp[1] == goal):
                found = True
                path.append(temp)
                dist = temp[3]
            else :
                start = temp[1]
                path.append(temp)
                tempGn = gn
                for i in range(len(node)):
                    gn = tempGn
                    if (matrix[start][i] > 0):
                        gn += matrix[start][i]
                        queue.put((gn + mat[i], i, child, gn))
                temp1 = copy.copy(temp)
                temp = queue.get()
                for i in range(len(path)):
                    if (temp[1] == path[i][1]):
                        temp = queue.get()
                gn = temp[3]
                gn = temp[3]
                tempChild1 = tempChild.copy()
                tempPath1 = tempPath.copy()
                idx = temp[2]
                if (len(tempChild1) != 0):
                    idx = tempChild[0]
                if (temp[2] <= temp1[2] or matrix[temp[1]][temp1[1]] == 0):
                    removeChild = []
                    removePath = []
                    tempChild = []
                    tempPath = []
                    for i in range(len(listChild)):
                        if (listChild[i] >= idx):
                            t = listChild[i]
                            removeChild.append(t)
                            tempChild.append(t)
                            tt = path[i]
                            removePath.append(tt)
                            tempPath.append(tt)
                    for i in range(len(removeChild)):
                        listChild.remove(removeChild[i])
                        path.remove(removePath[i])
                    if (len(tempChild1) != 0):
                        for k in range(len(tempChild1)):
                            listChild.append(tempChild1[k])
                        for l in range(len(tempPath1)):
                            path.append(tempPath1[l])
                listChild.append(temp[2])
                # print(temp[1])
                # print("path : ")
                # print(path)
                # print("tempPath : ")
                # print(tempPath)
    return path, dist
                    
def nodeValid(node):
    flag = False
    while (not flag):
        start = input("Masukkan titik awal : ")
        if start in node:
            flag = True
        else :
            print("Titik tidak ditemukan.")
            flag = False
    flag = False
    while (not flag):
        goal = input("Masukkan titik tujuan : ")
        if goal in node:
            flag = True
        else :
            print("Titik tidak ditemukan.")
            flag = False
    return start, goal

def printPath(node, path):
    for i in range(len(path)):
        if (i == len(path) - 1):
            print(node[path[i][1]])
        else :
            print(node[path[i][1]], end=" > ")