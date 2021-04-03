import plotly.graph_objects as go
from ArrayOfPoint import *

def printGraph(arrayPoint, path):
    # memasukan posisi x dan y tiap titik ke masing masing array
    array_y = []
    array_x = []
    for point in arrayPoint:
        array_x.append(point.x)
        array_y.append(point.y)
    
    # convert dari string jadi array tiap titik pada path
    array_path = []
    temp = ""
    for char in path:
        if char != " " and char != ">":
            temp = temp + char
        else:
            if temp != "":
                array_path.append(temp)
                temp = ""
    path_x = []
    path_y = []
    for namaPoint in array_path:
        path_x.append(arrayPoint.FindPoint(namaPoint).x)
        path_y.append(arrayPoint.FindPoint(namaPoint).y)
    
    print(array_x)
    print(array_y)
    print(path_x)
    print(path_y)
        
    fig = go.Figure(go.Scattermapbox(
        mode = "markers+lines",
        lon = array_y,
        lat = array_x,
        marker = {'size': 10}))

    fig.add_trace(go.Scattermapbox(
        mode = "markers+lines",
        lon = path_y,
        lat = path_x,
        marker = {'size': 10}))
    
    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': 10, 'lat': 10},
            'style': "stamen-terrain",
            'center': {'lon': -20, 'lat': -20},
            'zoom': 1})

    fig.show()