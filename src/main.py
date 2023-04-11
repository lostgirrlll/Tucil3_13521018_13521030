from inputFile import *
from visualisasi import *
from aStar import *

node, point, matrix, matrixDist = inputValid()
# printList(node)
# printList(point)
# printMatrix(matrix)
# printMatrix(matrixDist)
createGraph(node, matrix)

showGraph(createGraph(node, matrix), arrKoordinat(node, point))

path, dist = aStar(node, matrix, matrixDist)
printList(path)
print(dist)