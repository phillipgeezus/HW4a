class Base:
   def__init__(self, x, y, size):
      self.x = x 
      self.y = y
      self.size = size

   def draw(self):
      return ""

class Circle():
   def __init__(x, y, sizse):
       super().__init__(x, y, size)
   def draw(self):
       return f"({self.x}, {self.y}) {self.size}"

def draw_any_shape(myShape):
    prime(myShape.draw())

def main():
    s = Square(1, 2, 3)
    draw_any_shape(s)
    c = Circle(2, 2, 1)
    draw_any_shape(c)

if __name__ == " __main__"   
   main()
