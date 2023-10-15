from models.base import Base
class Rectangle(Base):
	"""Rectangle class child of base class"""

	def __init__(self, width, height, x=0, y=0, id=None):
		"""
		Constructor for rectangle
		Parameters:
		widht(int): width of rect
		height(int): height of rectangle
		x(int): x coordinate of rectangle
		y(int): y coordinate of rectangle
		id(int): ID of rectangle 
		
		Returns:
		None
		"""
		super().__init__(id)

		self.width = width
		self.height = height
		self.x = x
		self.y =y

	@property
	def width(self):
		"""Getter for width."""
		return self.__width	

	@property
	def height(self):
		"""Getter for height."""
		return self.__height

	@property
	def x(self):
		"""Getter for x."""
		return self.__x

	@property
	def y(self):
		"""Getter for y."""
		return self.__y

	@width.setter
	def width(self, value):
		"""Setter for width."""
		if type(value) is not int:
			raise TypeError("width must be an integer")
		if value <= 0:
			raise ValueError("width must be > 0")
		self.__width = value

	@height.setter
	def height(self, value):
		"""Setter for height."""
		if type(value) is not int:
			raise TypeError("height must be an integer")
		if value <= 0:
			raise ValueError("height must be > 0")
		self.__height = value
	@x.setter
	def x(self, value):
		"""Setter for x."""
		if type(value) is not int:
			raise TypeError("x must be an integer")
		self.__x = value

	@y.setter
	def y(self, value):
		"""Setter for y."""
		if type(value) is not int:
			raise TypeError("y must be an integer")
		self.__y = value
