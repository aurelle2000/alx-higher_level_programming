#!/usr/bin/python3
""" module Rectangle """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor Rectangle
            Arguments:
            @width: width of rectangle
            @height: height of rectangle
            @x: x position
            @y: y position
            @id: instances
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (self.validator('type', 'width', value) and
                self.validator('value', 'width', value)):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (self.validator('type', 'height', value) and
                self.validator('value', 'height', value)):
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (self.validator('type', 'x', value) and
                self.validator('value', 'x', value)):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (self.validator('type', 'y', value) and
                self.validator('value', 'y', value)):
            self.__y = value

    def validator(self, valtype, name, value):
        """
        method validator
        Arguments;
        @valtype: validation of type
        @name: attribute to validate
        @value: value to validate
        Returns:
        Type or Value error if is not an integer or
        if is not a positive number.
        """
        if valtype == 'type':
            if type(value) is not int:
                raise TypeError("{:} must be an integer".format(name))
        elif valtype == 'value':
            if name == 'width' or name == 'height':
                if value <= 0:
                    raise ValueError("{:} must be > 0".format(name))
            elif name == 'x' or name == 'y':
                if value < 0:
                    raise ValueError("{:} must be >= 0".format(name))
        return True

    def area(self):
        """
        method area
        Returns: the area of the Rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        method display - prints in stdout the Rectangle
        instance with the character #
        """
        for pos_y in range(self.__y):
            print()
        for row in range(self.__height):
            for pos_x in range(self.__x):
                print(' ', end='')
            for column in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """ magic method __str__ """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ method update - assigns an argument to each attribute """
        count = 1
        if args:
            for arg in args:
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.width = arg
                elif count == 3:
                    self.height = arg
                elif count == 4:
                    self.x = arg
                elif count == 5:
                    self.y = arg
                count += 1
        else:
            if kwargs:
                for key in kwargs:
                    if key == 'id':
                        self.id = kwargs[key]
                    if key == 'width':
                        self.width = kwargs[key]
                    if key == 'height':
                        self.height = kwargs[key]
                    if key == 'x':
                        self.x = kwargs[key]
                    if key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        """
        method to_dictionary
        Returns: the dictionary representation of a Rectangle
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
