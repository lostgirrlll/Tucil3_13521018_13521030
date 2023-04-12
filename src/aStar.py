from queue import PriorityQueue
import copy
from visualisasi import *
from inputFile import *
from apiMap import *

def aStar(node, matrix, matrixDist, start, goal):
    # mengubah nama node menjadi index
    start = node.index(start)
    goal = node.index(goal)
    # mengambil matrix distance yang berisi jarak garis lurus dari simpul goal
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
            # kondisi jika sudah sampai ke goal
            if (temp[1] == goal):
                found = True
                path.append(temp)
                dist = temp[3]
            else :
                # menginisialisasi node yang sedang dikunjungi
                curr = temp[1]
                path.append(temp)
                tempGn = gn
                # memasukkan node yang belum dikunjungi dan bertetangga dengan curr ke queue
                for i in range(len(node)):
                    gn = tempGn
                    if (matrix[curr][i] > 0):
                        gn += matrix[curr][i]
                        queue.put((gn + mat[i], i, child, gn))
                temp1 = copy.copy(temp)
                temp = queue.get()
                # mengganti node jika sudah pernah dikunjungi
                for i in range(len(path)):
                    if (temp[1] == path[i][1]):
                        temp = queue.get()
                gn = temp[3]
                tempChild1 = tempChild.copy()
                tempPath1 = tempPath.copy()
                idx = temp[2]
                if (len(tempChild1) != 0):
                    idx = tempChild[0]
                # mengecek kondisi backtracking
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
    return path, dist