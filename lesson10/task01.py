"""
Task01 module
=============

Shapes
"""

class Color():
    def __init__(self, r, g, b, alpha=1):
        self.r, self.g, self.b = r, g, b
        self.alpha = alpha

class Coordinates(object):
    """Coordinates class"""
    def __init__(self):
        raise NotImplemented('Use static methods.')

    @staticmethod
    def linear(x, y):
        return type('Coordinates', (), {'x': x, 'y': y, 'type': 'linear'})

    @staticmethod
    def spherical(r, phi):
        return type('Coordinates', (),
                    {'r': r, 'phi': phi, 'type': 'spherical'})

    @staticmethod
    def cylindrical(r, theta):
        return type('Coordinates', (),
                    {'r': r, 'theta': theta, 'type': 'cylindrical'})


class Point(object):
    """Point"""
    def __init__(self, coordinates, color):
        self.coordinates = coordinates
        self.color = color


class Circle(Point):
    """Circle"""
    def __init__(self, coordinates, radius, line, color):
        super(Circle, self).__init__(coordinates, color)
        self.radius = radius
        self.line = line


class Line(object):
    """Line"""
    def __init__(self, coordinates, pattern, color):
        self.color = color
        self.coordinates = coordinates
        self.pattern = pattern


class Polygon(object):
    def __init__(self, coordinates, patterns, color, cyclically=True):
        self.coordinates = coordinates
        self.patterns = patterns
        self.color = color
        self.cyclically = cyclically


class Triangle(Polygon):
    """Triangle"""
    def __init__(self, coordinates, patterns, color):
        if len(coordinates) != 3 or len(coordinates) != len(patterns):
            raise ValueError('Bad triangle params.')

        super(Triangle, self).__init__(coordinates, patterns, color)


class Rectangle(Polygon):
    """Rectangle"""
    def __init__(self, coordinates, patterns, color):
        if len(coordinates) != len(patterns):
            raise ValueError('Bad rectangle params.')

        if len(coordinates) < 3 or len(coordinates) > 4:
            raise ValueError('Bad rectangle params.')

        # @todo add more validation rules

        super(Rectangle, self).__init__(coordinates, patterns, color)
