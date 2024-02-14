#!/usr/bin/python3
"""Base Module
"""
import json
import csv
from turtle import *
from random import choice


class Base:
    """Base class

    Attributes:
        __nb_objects (int): provate class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init method

        Initializes the class

        Args:
            id: keyword argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dict to JSON and returns it"""
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file
        """
        file = '{}.json'.format(cls.__name__)
        with open(file, 'w') as f:
            if not list_objs:
                f.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy = cls(**dictionary)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = '{}.json'.format(cls.__name__)
        newlist = []
        try:
            with open(file, 'r') as f:
                new = cls.from_json_string(f.read())
                for dictionary in new:
                    newlist.append(cls.create(**dictionary))
                return newlist
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves an object to a csv file"""
        file = '{}.csv'.format(cls.__name__)
        with open(file, 'w', newline='') as f:
            doc = csv.writer(f, dialect='excel')
            if not list_objs:
                doc.writerow('')
            else:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        row = [
                                obj.id,
                                obj.width,
                                obj.height,
                                obj.x,
                                obj.y
                                ]
                        doc.writerow(row)
                    else:
                        row = [obj.id, obj.size, obj.x, obj.y]
                        doc.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """loads from a csv file"""
        templist = []
        file = '{}.csv'.format(cls.__name__)
        try:
            with open(file, newline='') as f:
                docreader = csv.reader(f, delimiter=',')
                for row in docreader:
                    row = [int(x) if x.isdigit() else x for x in row]
                    if cls.__name__ == 'Rectangle':
                        temp = cls(1, 1)
                    else:
                        temp = cls(1)
                    temp.update(*row)
                    templist.append(temp)
                return templist
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws a list of rectangle and squares

        Colors used are from pantone color palette 2015
        """
        t = Turtle()
        t.hideturtle()
        screen = Screen()
        screen.bgcolor('#006994')
        color_list = [
                '#9dc6d8',
                '#00b3ca',
                '#7dd0b6',
                '#1d4e89',
                '#d2b29b',
                '#e38690',
                '#f69256',
                '#ead98b',
                '#965251',
                '#c6cccc'
                ]
        for rectangle in list_rectangles:
            t.color(choice(color_list))
            t.penup()
            t.goto(rectangle.x * 3, rectangle.y * 3)
            t.pendown()
            t.begin_fill()
            for _ in range(2):
                t.fd(rectangle.width)
                t.right(90)
                t.fd(rectangle.height)
                t.right(90)
            t.end_fill()
            t.penup()

        for square in list_squares:
            t.color(choice(color_list))
            t.penup()
            t.goto(square.x * 3, square.y * 3)
            t.pendown()
            t.begin_fill()
            for _ in range(4):
                t.fd(square.size)
                t.right(90)
            t.end_fill()
            t.penup()

        done()
