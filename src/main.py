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
    getUCS(matrix, matrixDist, node, start, goal, point)

    # A*
    getAStar(matrix, matrixDist, node, start, goal, point)
