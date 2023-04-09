import os
import numpy as np
from scipy.linalg import issymmetric

def inputValid():
    flag = False
    while (flag == False):
        filename = input("Masukkan nama file : ")
        filepath = os.path.join('..\\Tucil3_13521018_13521030\\test', filename)
        # check file exist in folder or not
        if not os.path.isfile(filepath):
            print("File tidak ditemukan.")
            flag = False
        else :
            with open(filepath, 'r') as f:
                line = f.readline()
                node = [str(x) for x in line.strip().split(', ')]
                count = len(node)
                if count < 8:
                    print("Input file minimum memiliki 8 node.")
                    flag = False
                else :
                    matrix = []
                    for i in range(count):
                        line = f.readline()
                        row = line.strip().split()
                        if len(row) != count:
                            print("Matriks tidak persegi.")
                            flag = False
                            break
                        else :
                            row = [int(value) for value in row]
                            if any(value < 0 for value in row):
                                print("Nilai matriks tidak boleh negative.")
                                flag = False
                                break
                            else :
                                matrix.append(row)
                                flag = True
                    if (flag == True):
                        matrix = np.array(matrix)
                        if isSymmetric(matrix, len(matrix)):
                            print("Input file valid.")
                            flag = True
                        else :
                            print("Matriks tidak simetris.")
                            flag = False      
    return node, matrix

def isSymmetric(mat, N):
    for i in range(N):
        for j in range(N):
            if (mat[i][j] != mat[j][i]):
                return False
    return True

def printList(list):
    for i in range(len(list)):
        print(list[i])

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()