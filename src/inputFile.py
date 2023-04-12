import os
import numpy as np
from scipy.linalg import issymmetric

def inputValid():
    flag = False
    while (flag == False):
        filename = input("\t Masukkan nama file : ")
        filepath = os.path.join('..\\Tucil3_13521018_13521030\\test', filename)        
        # Check if file exists
        if not os.path.isfile(filepath):
            print("\t File tidak ditemukan.")
            flag = False
        else :
            # Read file
            with open(filepath, 'r') as f:
                matrix = []
                line = f.readline()
                row = line.strip().split()
                row = [int(value) for value in row]
                length = len(row)
                # Check if file has minimum 8 nodes
                if length < 8:
                    print("\t Input file minimum memiliki 8 node.")
                    flag = False
                else :
                    if any(value < 0 for value in row):
                        print("\t Nilai matriks tidak boleh negatif.")
                        flag = False
                        break
                    else :
                        # Append row to matrix
                        matrix.append(row)
                        for i in range(length-1):
                            line = f.readline()
                            row = line.strip().split()
                            row = [int(value) for value in row]
                            # Check if matrix has negative value
                            if any(value < 0 for value in row):
                                print("\t Nilai matriks tidak boleh negatif.")
                                flag = False
                                break
                            else :
                                # Append row to matrix
                                matrix.append(row)
                                flag = True
                        # Check if matrix is symmetric
                        if (flag == True):
                            matrix = np.array(matrix)
                            if not isSymmetric(matrix, len(matrix)):
                                print("\t Matriks tidak simetris.")
                                flag = False
                                continue
                            else :
                                print("\t Input file valid.")
                                # Convert line to list of node and list of coordinates
                                node = []
                                point = []
                                for i in range(length):
                                    line = f.readline()
                                    row = line.strip().split(', ')
                                    node.append(row[0])
                                    point.append([float(row[1]), float(row[2])])
                                # Convert matrix of adjacent to matrix of distances
                                matrixDist = [[0 for x in range(length)] for y in range(length)]
                                for j in range(length):
                                    for k in range(length):
                                        # Calculate distance between two nodes
                                        distance = ((point[j][0] - point[k][0])**2 + (point[j][1] - point[k][1])**2)**0.5
                                        distance = distance*100000
                                        distance = round(distance,2)
                                        matrixDist[j][k] = distance
                                flag = True
    for i in range (len(matrix)):
        for j in range (len(matrix)):
            if matrix[i][j] == 1:
                matrix[i][j] = matrixDist[i][j]
    return node, point, matrix, matrixDist

# Check if matrix is symmetric
def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True

# Print list
def printList(list):
    for i in range(len(list)):
        print(list[i])

# Print matrix
def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()

# get node : point dictionary
def arrKoordinat(node, point):
    arr = {}
    length = len(node)
    for i in range(length):
        arr[node[i]] = point[i]
    return arr

# matrix of path
def matrixPath(path, node, cost):
    mat = [[0 for i in range(len(node))] for j in range(len(node))]
    for i in range(len(path)-1):
        mat[node.index(path[i])][node.index(path[i+1])] = cost[i]
        mat[node.index(path[i+1])][node.index(path[i])] = cost[i]
    return mat