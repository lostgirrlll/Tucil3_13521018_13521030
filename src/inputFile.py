import os
import numpy as np
from scipy.linalg import issymmetric

# Check if input file is valid
def inputValid():
    flag = False
    while (flag == False):
        filename = input("Masukkan nama file : ")
        filepath = os.path.join('..\\Tucil3_13521018_13521030\\test', filename)        
        # Check if file exists
        if not os.path.isfile(filepath):
            print("File tidak ditemukan.")
            flag = False
        else :
            # Read file
            with open(filepath, 'r') as f:
                line = f.readline()
                node = [str(x) for x in line.strip().split(', ')]
                count = len(node)
                # Check if file has minimum 8 nodes
                if count < 8:
                    print("Input file minimum memiliki 8 node.")
                    flag = False
                else :
                    matrix = []
                    for i in range(count):
                        line = f.readline()
                        row = line.strip().split()
                        # Check if matrix is square
                        if len(row) != count:
                            print("Matriks tidak persegi.")
                            flag = False
                            break
                        else :
                            row = [int(value) for value in row]
                            # Check if matrix has negative value
                            if any(value < 0 for value in row):
                                print("Nilai matriks tidak boleh negative.")
                                flag = False
                                break
                            else :
                                # Append row to matrix
                                matrix.append(row)
                                flag = True
                    # Check if matrix is symmetric
                    if (flag == True):
                        matrix = np.array(matrix)
                        if isSymmetric(matrix, len(matrix)):
                            print("Input file valid.")
                            flag = True
                        else :
                            print("Matriks tidak simetris.")
                            flag = False      
    return node, matrix

def inputKoordinat():
    flag = False
    while (flag == False):
        filename = input("Masukkan nama file : ")
        filepath = os.path.join('..\\Tucil3_13521018_13521030\\test', filename)        
        # Check if file exists
        if not os.path.isfile(filepath):
            print("File tidak ditemukan.")
            flag = False
        else :
            # Read file
            with open(filepath, 'r') as f:
                line = f.readline()
                count = int(line.strip())
                # Check if file has minimum 8 nodes
                if count < 8:
                    print("Input file minimum memiliki 8 node.")
                    flag = False
                else :
                    # Convert line to list of node an matrix of coordinates
                    node = []
                    point = []
                    for i in range(count):
                        line = f.readline()
                        row = line.strip().split(', ')
                        node.append(row[0])
                        point.append([float(row[1]), float(row[2])])
                    # Convert matrix of adjacent to matrix of distances
                    matrix = []
                    for j in range(count):
                        line = f.readline()
                        row = line.strip().split()
                        row = [float(value) for value in row]
                        # Check if matrix value is 1
                        for k in range(count):
                            if row[k] == 1:
                                # Calculate distance between two nodes
                                distance = ((point[j][0] - point[k][0])**2 + (point[j][1] - point[k][1])**2)**0.5
                                distance = distance*100000
                                distance = round(distance,2)
                                row[k] = distance
                        matrix.append(row)
                    flag = True
    return node, point, matrix


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