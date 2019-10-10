"""
This week I want you to make a class that represents a circle.

The circle should have a radius, a diameter, and an area. It should also have a nice string representation.

For example:

>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
Additionally the radius should default to 1 if no radius is specified when you create your circle:

>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2
There are three bonuses for this exercise.
"""
import math


class Circle:
    def __init__(self, radius=1, diameter=1, area=1):
        self._radius = radius
        self._diameter = diameter
        self._area = area

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        self._diameter = self.radius * 2
        return self._diameter

    @property
    def area(self):
        self._area = math.pi * math.pow(self.radius, 2)
        return self._area

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        else:
            self._radius = value

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError("Diameter cannot be negative")
        else:
            # self._diameter = value
            self._radius = diameter / 2

    @area.setter
    def area(self, value):
        if value:
            raise AttributeError("Area cannot be a set")

    def __repr__(self):
        # return "Circle(radius: {}, diameter: {}, area: {})".format(self.radius, self.diameter, self.area)
        return f'Circle({self._radius})'
