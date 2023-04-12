import plotly.graph_objects as go

def printGraph(node, point, path, matrix):
    pointY = []
    pointX = []
    for i in range(len(point)):
        pointX.append(point[i][0])
        pointY.append(point[i][1])
    
    pathX = []
    pathY = []
    for i in range(len(path)):
        idx = node.index(path[i])
        pathX.append(point[idx][0])
        pathY.append(point[idx][1])

    fig = go.Figure(go.Scattermapbox(
        lon = pointY,
        lat = pointX
        ))

    for i in range(len(matrix)):
        for j in range(0,i):
            if (matrix[i][j] > 0):
                adjacentX = []
                adjacentY = []
                adjacentX.append(point[j][0])
                adjacentY.append(point[j][1])
                adjacentX.append(point[i][0])
                adjacentY.append(point[i][1])
                fig.add_trace(go.Scattermapbox(
                    mode = "markers+lines",
                    lon = adjacentY,
                    lat = adjacentX,
                    marker = {'size': 10, 'color' : 'rgb(0, 255, 0)'}))

    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lon = pathY,
        lat = pathX,
        marker = {'size': 10, 'color' : 'rgb(255, 0, 0)'}))

    max_x, max_y = maxPoint(point)
    min_x, min_y = minPoint(point)

    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': min_y, 'lat': min_x},
            'style': "stamen-terrain",
            'center': {'lon': max_y, 'lat': max_x},
            'zoom': 16})

    fig.show()

def maxPoint(point):
    max_x = point[0][0]
    max_y = point[0][1]
    for i in range(len(point)):
        if (point[i][0] > max_x):
            max_x = point[i][0]
        if (point[i][1] > max_y):
            max_y = point[i][1]
    return max_x, max_y

def minPoint(point):
    min_x = point[0][0]
    min_y = point[0][1]
    for i in range(len(point)):
        if (point[i][0] < min_x):
            min_x = point[i][0]
        if (point[i][1] < min_y):
            min_y = point[i][1]
    return min_x, min_y