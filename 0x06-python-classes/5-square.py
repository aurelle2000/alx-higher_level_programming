#!/usr/bin/python3
class Square:
                def __init__(self, size=0):
                                    self.size = size

                                        def area(self):
                                                            return self.__size * self.__size

                                                    @property
                                                        def size(self):
                                                                            return self.__size

                                                                    @size.setter
                                                                        def size(self, value):
                                                                                            if type(value) == int and value >= 0:
                                                                                                                    self.__size = value
                                                                                            else:
                                                                                                                    raise TypeError("size must be an integer")
                                                                                                                if value < 0:
                                                                                                                                        raise ValueError("size must be >= 0")

                                                                                                                                def my_print(self):
                                                                                                                                                    if self.size is 0:
                                                                                                                                                                            print()
                                                                                                                                                                                    for x in range(self.size):
                                                                                                                                                                                                            for y in range(self.size):
                                                                                                                                                                                                                                        print('#', end='')
                                                                                                                                                                                                                                                    print()
                                                                                                                                                                                                                                                    
