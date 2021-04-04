import plotly.graph_objects as go
from ArrayOfPoint import *

def printGraph(arrayPoint, path, matrix):
    # memasukan posisi x dan y tiap titik ke masing masing array
    array_y = []
    array_x = []
    for point in arrayPoint.mem:
        array_x.append(point.x)
        array_y.append(point.y)
    
    # convert dari string jadi array tiap titik pada path
    array_path = []
    temp = ""
    if (path != "You have arrived at your destination"):
        for char in path:
            if char != " " and char != ">":
                temp = temp + char
            else:
                if temp != "":
                    array_path.append(temp)
                    temp = ""
        array_path.append(temp)
    
    path_x = []
    path_y = []
    if (array_path != []):
        for namaPoint in array_path:
            path_x.append(arrayPoint.FindPoint(namaPoint).x)
            path_y.append(arrayPoint.FindPoint(namaPoint).y)

    fig = go.Figure(go.Scattermapbox(
        lon = array_y,
        lat = array_x
        ))

    for i in range(1, matrix.matrix_size):
        for j in range(1, i):
            if (matrix.matrix_adj[i][j] == "1"):
                tetangga_x = []
                tetangga_y = []
                tetangga_x.append(arrayPoint.FindPoint(matrix.matrix_adj[0][j]).x)
                tetangga_y.append(arrayPoint.FindPoint(matrix.matrix_adj[0][j]).y)
                tetangga_x.append(arrayPoint.FindPoint(matrix.matrix_adj[i][0]).x)
                tetangga_y.append(arrayPoint.FindPoint(matrix.matrix_adj[i][0]).y)
                fig.add_trace(go.Scattermapbox(
                    mode = "markers+lines",
                    lon = tetangga_y,
                    lat = tetangga_x,
                    # mode = 'markers',
                    # marker = dict(
                    #     size = 2,
                    #     color = 'rgb(255,0,0)',
                    #     line = dict(
                    #         width = 3,
                    #         color = 'rgba(68,68,68,0)'
                    # )    
                    # ))
                    marker = {'size': 10, 'color' : 'rgb(0, 255, 0)'}))

    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lon = path_y,
        lat = path_x,
        marker = {'size': 10, 'color' : 'rgb(255, 0, 0)'}))

    maxPoint = arrayPoint.GetMaxPoint()
    minPoint = arrayPoint.GetMinPoint()

    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': minPoint.y, 'lat': minPoint.x},
            'style': "stamen-terrain",
            'center': {'lon': maxPoint.y, 'lat': maxPoint.x},
            'zoom': 16})

    fig.show()