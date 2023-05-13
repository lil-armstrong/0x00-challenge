#!/usr/bin/env python3
''' Squate module '''

class Square:
    ''' Square class '''
    width = 0
    height = 0
    
    def __init__(self, *args, **kwargs):
        ''' Square instance initialization'''
        if len(kwargs) > 0:
            for key, value in kwargs.items(): 
                 setattr(self, key, value)
        else:
            self.width = args[0]
            self.height = args[1]
    
    @property
    def area(self):
        """Area of the square"""
        return self.width * self.width
    
    @property
    def perimeter(self):
        """Perimeter of the square"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        ''' Syring repr of square'''
        return f"Square({self.width}, {self.height})"
    
if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area)
    print(s.perimeter)
