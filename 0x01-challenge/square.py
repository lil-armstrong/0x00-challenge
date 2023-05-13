#!/usr/bin/python3
""" square class ,odule """
class Square():
    """ square class """
    width = 0
    height = 0
    
    def __init__(self, *args, **kwargs):
        """ initialize a square instance """
        self.width = kwargs.get('width', 0)
        self.height = kwargs.get('height', 0)

    def area(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter(self):
        """ calculate perimeter of square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ string represemtation square instance """
        return f"{self.width}/{self.height}"

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area)
    print(s.perimeter)
