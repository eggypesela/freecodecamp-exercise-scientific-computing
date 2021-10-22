#!/usr/bin/env python3
#created by Regina Citra Pesela (reginapasela@gmail.com)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        #create header that show width and height value of rectangle
        self.name = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        return self.name

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        #check if width or height is larger than 50, if yes return "Too big for picture"
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
         
        #create shape using "*"
        self.objectShape = str()
        for i in range(self.height):
            for j in range(self.width):
                self.objectShape += "*"
            self.objectShape += "\n"

        return self.objectShape

    def get_amount_inside(self, shape):
        #create variable for shape inside
        self.heightInside = shape.height
        self.widthInside = shape.width
        
        #count possible shape inside shape
        self.amountInside = round(self.width / self.widthInside) * round(self.height / self.heightInside)

        return self.amountInside 

class Square(Rectangle):
    def __init__(self, side):
        self.width, self.height = side, side
    
    def __str__(self):
        #create header that show width and height value of square
        self.name = "Square(side=" + str(self.width) + ")"
        return self.name
    
    def set_side(self, side):
        self.width = side
        self.height = side


#test
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))