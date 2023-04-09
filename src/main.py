from inputFile import *
from visualisasi import *

node, matrix = inputValid()

printList(node)
printMatrix(matrix)
createGraph(node, matrix)
showGraph(createGraph(node, matrix))

node1, point, matrix1 = inputKoordinat()
printList(node1)
printMatrix(matrix1)
createGraph(node1, matrix1)
showGraph(createGraph(node1, matrix1))