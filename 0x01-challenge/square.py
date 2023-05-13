#!/usr/bin/env python3
class Square:
    
    def __init__(self, **kwargs):
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)
    
    @property
    def area(self):
        """Area of the square"""
        return self.width * self.width
    
    @property
    def perimeter(self):
        """Perimeter of the square"""
        return (self.width * 2) + (self.height * 2)
    
    def __str__(self):
        return f"{self.width}/{self.height}"
    
if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area)
    print(s.perimeter)
