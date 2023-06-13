#!/usr/bin/python3
"""Student to json"""


class Student():
    """Class for definition of student"""

    def __init__(self, first_name, last_name, age):
        """sets attributes for student object

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): current age of student
         """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student instance"""

        if type(attrs) is list:
            if all(type(var) is str for var in attrs):
                resultant = {}
                for key in attrs:
                    if key in self.__dict__:
                        resultant[key] = self.__dict__[key]
                return resultant
        else:
            return self.__dict__
