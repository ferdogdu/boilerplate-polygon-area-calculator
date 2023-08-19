from math import floor


class Rectangle:

  def __init__(self, w, h):
    self.width = w
    self.height = h

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, w):
    self.width = w

  def set_height(self, h):
    self.height = h

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    else:
      picture = ""
      x = self.width
      y = self.height
      while y > 0:
        picture += f"{'*'*x}\n"
        y -= 1
      return picture

  def get_amount_inside(self, shape):
    if (self.width % shape.width == 0) and (self.height % shape.height == 0):
      return self.get_area() / shape.get_area()
    elif (self.width > shape.width) and (self.height > shape.height):
      return floor(self.get_area() / shape.get_area())
    else:
      return 0


class Square(Rectangle):

  def __init__(self, s):
    super().__init__(s, s)

  def __repr__(self):
    return f"Square(side={self.width})"

  def set_side(self, s):
    self.width = s
    self.height = s

  def set_width(self, s):
    self.set_side(s)

  def set_height(self, s):
    self.set_side(s)
