from inputFile import *
from visualisasi import *

node, matrix = inputValid()

printList(node)
printMatrix(matrix)
createGraph(node, matrix)
showGraph(createGraph(node, matrix))