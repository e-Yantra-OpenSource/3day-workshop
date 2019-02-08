import os
import sys
import math

class Geometric_Shape:
    # member variables
    height = 10
    width = 20
    area = 0
    
    # constructor
    def __init__(self, name = "Line", num_edges = 1, num_vertices = 2):
        self.name = name
        self.num_edges = num_edges
        self.num_vertices = num_vertices
    
    # member method
    def Area_Shape(width, height):
        area = height * width
        return area

shape_rectangle = Geometric_Shape(name = "Rectangle",num_edges = 4,num_vertices = 4)
print(shape_rectangle)
print(shape_rectangle.name)
print(shape_rectangle.num_edges)
print(shape_rectangle.num_vertices)
