import os
import sys
import math



class Geometric_Shape():
    # member variables
    
    
    # constructor
    def __init__(self, name, num_edges, num_vertices, height, width, area):
        self.name = name
        self.num_edges = num_edges
        self.num_vertices = num_vertices
        self.height = 10
        self.width = 20
        self.area = 0


    
    # member method
    def Area_Shape(self):
        if(self.num_edges == 4):
            self.area = self.height * self.width
            return self.area



class Rectangle(Geometric_Shape):
    def __init__(self, name = "Rectangle", num_edges = 4, num_vertices = 4):
        self.name = name
        self.num_edges = num_edges
        self.num_vertices = num_vertices

    def init_edge_lenths(self, height,width):
        self.height = height
        self.width = width



sample_square = Rectangle(name = "Square")
print("shape : %s"%sample_square.name)
print("number of edges: %s"%sample_square.num_edges)
print("number of vertices: %s"%sample_square.num_vertices)


sample_square.init_edge_lenths(20,20)
print("height of the square: %s"%sample_square.height)
print("width of the square: %s"%sample_square.width)
print("area of the square: %s"%sample_square.Area_Shape())


    
