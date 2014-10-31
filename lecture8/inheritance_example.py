class Shape:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color=color

	def print_color(self):
		print("COLOR=", self.color)

class Circle(Shape):
	def __init__(self, x, y, color, radius):
		super().__init__(x,y,color)
		self.radius = radius

	def print_color(self):
		print("CIRCLE COLOR=", self.color)

class Square(Shape):
	def __init__(self, x, y, color, side):
		super().__init__(x,y,color)
		self.side = side

c = Circle(3, 4, "red", 2)
c.print_color()

s = Square(5, 6, "blue", 3)
s.print_color()


