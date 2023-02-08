class Rectangle:
  
  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def __str__(self):
    output = f"Rectangle(width={self.width}, height={self.height})"
    return output
  
  def set_width(self,W):
    self.width = W;
  
  def set_height(self,H):
    self.height = H;
  
  def get_area(self):
    return (self.width * self.height)
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.height)
  
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if (self.width >= 50 | self.height >=50):
      return "Too big for picture."
    else:
      return "".join([f"{'*' * self.width}\n" for i in range(self.height)])
  
  def get_amount_inside(self,shape):
    area = self.get_area() / shape.get_area()
    return int(area)
      
  



class Square(Rectangle):
  def __init__(self,side):
    Rectangle.__init__(self,side,side)
  
  def __str__(self):
    return f"Square(side={self.width})"
  
  def set_side(self,side):
    self.height = side
    self.width = side

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