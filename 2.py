'''Define a class named Shape and its subclass Square. The Square class has
an init function which takes a length as argument. Both classes have a area
function which can print the area of the shape where Shape's area is 0
by default.
'''
class Shape:
    def __init__(self):
        self.area= 0
    def Area(self):
        print(self.area)

class Square(Shape):
    def __init__(self, length):
        self.length= length
        self.area= 0
    def Area(self):
        area = self.length * self.length
        return area