from collections import deque
import sys
from time import perf_counter
from math import pi , acos , sin , cos
from heapq import heapify, heappop, heappush
import tkinter as tk
from turtle import st

with open("rrNodes.txt")as f:
    node_list = [line.strip().split() for line in f]

with open("rrEdges.txt") as f2:
    edge_list = [line.strip().split() for line in f2]

with open("rrNodeCity.txt") as f3:
    city_list = [line.strip().split() for line in f3]

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   if node1 == node2:
    return 0
   y1, x1 = node1
   y2, x2 = node2


   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

node_dict = dict()
edge_dict = dict()
weighted_graph = dict()
city_dict = dict()


for node_data in node_list:
    node_dict[node_data[0]] = [float(node_data[1]), float(node_data[2])]
    edge_dict[node_data[0]] = list()
    weighted_graph[node_data[0]] = list()

for city_data in city_list:
    if len(city_data) > 2:
        city_dict[city_data[1] + " " + city_data[2]] = city_data[0]
    else:
        city_dict[city_data[1]] = city_data[0]

for edge_data in edge_list:
    edge_dict[edge_data[0]].append(edge_data[1])
    edge_dict[edge_data[1]].append(edge_data[0])

start = perf_counter()
for node_id in node_dict.keys():
    for edge_data in edge_dict[node_id]:
        weighted_graph[node_id].append((calcd(node_dict[node_id], node_dict[edge_data]),edge_data))

print("Time to create data structure: %s" % (perf_counter() - start) )

edge_drawings = dict()
def convert_to_pixels(coord_pair):
     y = (coord_pair[0] * 13.5 - 25)
     x = (coord_pair[1] * -1 * 11 - 650)
     return (800-x, 800-y)


def create_routes(canvas):
    for node in edge_dict:
        for connected_node in edge_dict[node]:
            line = canvas.create_line([convert_to_pixels(node_dict[node]),convert_to_pixels(node_dict[connected_node])], tag='grid_line')
            edge_drawings[(node,connected_node)]=line

def color_red(canvas, line):
	canvas.itemconfig(line, fill="red") #changes color of one line to red

def correct_route_greening(canvas, end, path):
    for index in range(len(path)-1):
        canvas.itemconfig(edge_drawings[path[index], path[index+1]], fill = "blue")
        canvas.itemconfig(edge_drawings[path[index+1], path[index]], fill = "blue")

root2 = tk.Tk() #creates the frame
canvas2 = tk.Canvas(root2, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
create_routes(canvas2)
canvas2.pack(expand=True) #packing widgets places them on the board


def dijkstra(start, end):
    counter = 0
    starting_node = city_dict[start]
    ending_node = city_dict[end]
    closed = set()
    fringe = list()
    fringe.append((0, (0, starting_node), [starting_node,]))
    heapify(fringe)
    while fringe: 
        depth, node_tuple, path = heappop(fringe)
        distance, node = node_tuple
        if node == ending_node:
            correct_route_greening(canvas2, node, path)
            root2.update()
            return depth
        if node not in closed: 
            closed.add(node)
            for child in weighted_graph[node]:
                if child[1] not in closed:
                    child_path = path.copy()
                    child_path.append(child[1])
                    heappush(fringe, (depth + child[0], (child), child_path))
                    counter = counter + 1
                    color_red(canvas2, edge_drawings[(node, child[1])])
                    color_red(canvas2, edge_drawings[(child[1], node)])
                    if counter % 2000 == 0:
                        root2.update()

#dijkstra("Phoenix", "Atlanta")                      
print(dijkstra(sys.argv[1], sys.argv[2]))
root2.mainloop()


root = tk.Tk() #creates the frame
canvas = tk.Canvas(root, height=800, width=800, bg='white') #creates a canvas widget, which can be used for drawing lines and shapes
create_routes(canvas)
canvas.pack(expand=True) #packing widgets places them on the board


def a_str(start,end):
    starting_node = city_dict[start]
    ending_node = city_dict[end]
    counter = 0 
    closed = set()
    fringe = list()
    fringe.append((calcd(node_dict[starting_node], node_dict[ending_node]), 0, (0, starting_node), [starting_node,]))
    heapify(fringe)
    while fringe: 
        depth, actual_distance, node_tuple, path = heappop(fringe)
        distance, node = node_tuple
        if node == ending_node:
            correct_route_greening(canvas, node, path)
            root.update()
            return actual_distance
        if node not in closed:
          closed.add(node)
          for child in weighted_graph[node]:
                if child[1] not in closed:
                    child_path = path.copy()
                    child_path.append(child[1])
                    heappush(fringe, (actual_distance + child[0] + calcd(node_dict[child[1]], node_dict[ending_node]), actual_distance + child[0], (child), child_path))
                    counter = counter + 1
                    color_red(canvas, edge_drawings[(node, child[1])])
                    color_red(canvas, edge_drawings[(child[1], node)])
                    if counter % 1000 == 0:
                        root.update()
#a_str("Leon", "Tucson")
a_str(sys.argv[1], sys.argv[2])
root.mainloop()

#start = perf_counter()
#print("Dijkstra: %s in %s" % (dijkstra(sys.argv[1], sys.argv[2]), perf_counter() - start))
#start = perf_counter()
#print("A*: %s in %s" % (a_str(sys.argv[1], sys.argv[2]), perf_counter() - start))
