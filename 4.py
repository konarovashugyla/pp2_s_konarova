'''
Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
'''
from math  import hypot as h
class Point():
    def __init__(self, x, y ):
        self.x = x
        self.y = y
    def show(self):
        print( f'x = {self.x}, y = {self.y}')
    def move( self):
        x, y = y, x
    def dist(self):
        distance = h( self.x - self.y, self.y - self.x)
        print(distance)

        