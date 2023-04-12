from inputFile import *
from visualisasi import *
from aStar import *
from Graph import *

node, point, matrix, matrixDist = inputValid()
# printList(node)
# printList(point)
# printMatrix(matrix)
# printMatrix(matrixDist)
showGraph(createGraph(node, matrix), arrKoordinat(node, point))

start, goal = nodeValid(node)
path, dist = aStar(node, matrix, matrixDist, start, goal)
printPath(node, path)
print(dist)

for i in range(len(path)):
    path[i] = node[path[i][1]]

printGraph(node, point, path, matrix)