from inputFile import *
from visualisasi import *
from aStar import *
from ucs import *
from apiMap import *

if __name__ == "__main__":
    art("SHORT PATH")   # menampilkan ascii art
    # validasi intup txt
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

    # UCS
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

    # A*
    art("A*")
    pathA, costA = aStar(node, matrix, matrixDist, start, goal)
    if (start not in pathA or goal not in pathA):
        print("\t Tidak ada jalur yang dapat ditempuh.")
    else:
        print("\t Path : ", end="")
        strpathA = ""
        for i in range(len(pathA)):
            if (i == len(pathA) - 1):
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
    
    # Menampilkan Maps
    printGraph(node, point, pathUCS, matrix)
    printGraph(node, point, pathA, matrix)
