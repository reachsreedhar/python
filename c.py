#!/usr/bin/python3
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  @property
  def width(self):
    return self._width
    
  @width.setter
  def width(self, width):
    if width <= 0:
      raise ValueError('Width should be positive')
    self._width = width

  @property
  def height(self):
    return self._height
    
  @height.setter
  def height(self, height):
    if height <= 0:
      raise ValueError('Height should be positive')
    self._height = height

  def __str__(self):
    return 'Rectangle: _width: {0}, _height: {1}'.format(self._width, self._height)

  def __repr__(self):
    return 'Rectangle({0}, {1})'.format(self._width, self._height)

  def __eq__(self, other):
    if isinstance(other, Rectangle):
      return self._width == other._width and self._height == other._height
    else:
      return False

  def __lt__(self, other):
    if isinstance(other, Rectangle):
      return self.area() < other.area()
    else:
      return NotImplemented

r1 = Rectangle(10, 20)
#r2 = Rectangle(10, 20)

print(r1.width)
print(r1)
