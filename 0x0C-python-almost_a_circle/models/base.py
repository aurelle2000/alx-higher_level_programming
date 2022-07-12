#!/usr/bin/python3
""" base """
import json
import csv


class Base:
    """ the first class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        that returns the JSON string representation of list_dictionaries
        Arguments:
        @list_dictionaries: list of dictionaries
        Returns:
        If list_dictionaries is None or empty, return the string: "[]"
        Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            s = json.dumps(list_dictionaries)
            return s

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - writes the JSON string representation
        of list_objs to a file
        Arguments:
        @cls: class
        @list_objs: list of instances who inherits of Base
        """
        with open('{}.json'.format(cls.__name__), mode='w') as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                myList = []
                for i in list_objs:
                    i = i.to_dictionary()
                    myList.append(i)
                f.write(cls.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        """
        that returns the list of the JSON string representation json_string
        Arguments:
        @json_string: string representing a list of dictionaries
        Returns:
        If json_string is None or empty, return an empty list
        Otherwise, return the list represented by json_string
        """
        if json_string is None:
            return ([])
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create - class method
        Arguments:
        @cls: class
        @dictionary: can be thought of as a double pointer to a dictionary
        Returns:
        an instance with all attributes already set
        """
        dummy = None
        if cls.__name__ == 'Rectangle':
            dummy = cls(dictionary['width'], dictionary['height'])
            dummy.update(**dictionary)
        elif cls.__name__ == 'Square':
            dummy = cls(dictionary['size'])
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - that returns a list of instances
        Arguments:
        @cls: class
        Returns:
        If the file doesn’t exist, return an empty list
        Otherwise, return a list of instances - the type of
        these instances depends on cls
        """
        try:
            with open("{}.json".format(cls.__name__), "r") as file:
                my_list = cls.from_json_string(file.read())
        except IOError:
            my_list = []

        final_list = []
        for item in my_list:
            obj = cls.create(**item)
            final_list.append(obj)
        return final_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv - that serializes in CSV
        @cls: class
        @list_objs: list of instances
        Retuns:
        """
        with open('{}.csv'.format(cls.__name__), 'w') as f:
            if cls.__name__ == 'Rectangle':
                writer = csv.writer(f)
                for obj in list_objs:
                    r = [
                            [
                                str(obj.id),
                                str(obj.width),
                                str(obj.height),
                                str(obj.x),
                                str(obj.y)
                            ]
                        ]
                    writer.writerows(r)
            elif cls.__name__ == 'Square':
                writer = csv.writer(f)
                for obj in list_objs:
                    s = [[str(obj.id), str(obj.size), str(obj.x), str(obj.y)]]
                    writer.writerows(s)

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv - that deserializes in CSV
        @cls: class
        Retuns:
        list of instances
        """
        with open('{}.csv'.format(cls.__name__), 'rt') as f:
            reader = csv.reader(f)
            final_list = []
            for item in reader:
                if cls.__name__ == 'Rectangle':
                    instance = cls(
                                    int(item[1]),
                                    int(item[2]),
                                    int(item[3]),
                                    int(item[4]),
                                    int(item[0])
                                )
                elif cls.__name__ == 'Square':
                    instance = cls(
                                    int(item[1]),
                                    int(item[2]),
                                    int(item[3]),
                                    int(item[0])
                                )
                final_list.append(instance)

        return final_list
