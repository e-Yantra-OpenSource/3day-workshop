import os
import sys
import math



class Geometric_Shape():
    # member variables
    
    
    # constructor
    def __init__(self, name, num_edges, num_vertices):
        self.name = name
        self.num_edges = num_edges
        self.num_vertices = num_vertices
        self._height = 25 # (protected)
        self._width = 100 # (protected)
        self.__area = 0 # (private)


    
    # member method
    def Area_Shape(self):
        if(self.num_edges == 3):
            self.__area = 0.5 * self._height * self._width
            print("area of the triangle: %s"%self.__area)



sample_triangle = Geometric_Shape(name = "Triangle",num_edges=3,num_vertices=3)
print("shape : %s"%sample_triangle.name)
print("number of edges: %s"%sample_triangle.num_edges)
print("number of vertices: %s"%sample_triangle.num_vertices)
print("height of the triangle: %s"%sample_triangle._height)
print("width of the triangle: %s"%sample_triangle._width)
sample_triangle.Area_Shape()



    
