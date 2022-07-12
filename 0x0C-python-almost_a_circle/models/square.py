#!/usr/bin/python3
""" module Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ magic method __str__ """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ method update - assigns an argument to each attribute """
        count = 1
        if args:
            for arg in args:
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.size = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        else:
            if kwargs:
                for key in kwargs:
                    if key == 'id':
                        self.id = kwargs[key]
                    if key == 'size':
                        self.size = kwargs[key]
                    if key == 'x':
                        self.x = kwargs[key]
                    if key == 'y':
                        self.y = kwargs[key]

    def to_dictionary(self):
        """ that returns the dictionary representation of a Square """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
