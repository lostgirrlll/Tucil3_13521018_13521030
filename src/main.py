from inputFile import *
from visualisasi import *
from aStar import *
from ucs import *
from apiMap import *

if __name__ == "__main__":
    art("SHORT PATH")
    node, point, matrix, matrixDist = inputValid()
    print("\t Menampilkan Graph...")
    showGraph(createGraph(node, 0, matrix, "initial"), arrKoordinat(node, point), 0, "initial", 0, 0)
    art("line")
    print("\t Area :")
    for i in range(len(node)):
        print("\t -", node[i])
    start = str(input("\t Masukkan titik awal : "))
    goal = str(input("\t Masukkan titik tujuan : "))
    while (start not in node or goal not in node or start == goal):
        if (start == goal and start in node and goal in node):
            print("\t Titik tidak valid. Titik awal tidak boleh sama dengan titik tujuan.")
        else:
            print("\t Titik tidak valid. Masukkan titik yang ada di area.")
        start = str(input("\t Masukkan titik awal : "))
        goal = str(input("\t Masukkan titik tujuan : "))

    art("UCS")
    path, cost = ucs(matrix, start, goal, node)
    if (start not in path or goal not in path):
        print("\t Tidak ada jalur yang dapat ditempuh.")
    else:
        print("\t Path : ", end="")
        strpath = ""
        for i in range(len(path) - 1):
            strpath = strpath + path[i] + " -> "
            print(path[i], end=" -> ")
        print(goal)
        print("\t Jarak : ", sum(cost))
        print("\t Menampilkan Graph...")
        mat = matrixPath(path, node, cost)
        # print(matrixPath(path, node, cost))
        showGraph(createGraph(node, 0, matrix, "initial"), arrKoordinat(node, point), createGraph(node, path, mat, "ucs_aStar"), "ucs", strpath + goal, sum(cost))

    art("A*")
    pathA, costA = aStar(node, matrix, matrixDist, start, goal)
    for i in range(len(pathA)):
        pathA[i] = node[pathA[i][1]]
    print("\t Path : ", end="")
    strpathA = ""
    for i in range(len(pathA)):
        if (i == len(pathA) - 1):
            strpathA = strpathA + pathA[i]
            print(pathA[i])
        else:
            strpathA = strpathA + pathA[i] + " -> "
            print(pathA[i], end=" -> ")
    print("\t Jarak : ", costA)
    print("\t Menampilkan Graph...")

    cost = []
    for i in range(len(pathA)):
        cost.append(matrixDist[node.index(pathA[i])][node.index(goal)])

    mat = matrixPath(pathA, node, cost)
    showGraph(createGraph(node, 0, matrix, "initial"), arrKoordinat(node, point), createGraph(node, pathA, mat, "ucs_aStar"), "aStar", strpathA + goal, costA)
    printGraph(node, point, pathA, matrix)
