"""
Task01 module
=============

Shapes
"""


class Coordinates:
    """Coordinates class"""
    def __init__(self):
        raise NotImplemented('Use static methods.')

    @staticmethod
    def linear(x, y):
        return type('Coordinates', (), {'x': x, 'y': y, 'type': 'linear'})

    @staticmethod
    def spherical(p, theta, phi):
        return type('Coordinates', (),
                    {'p': p, 'theta': theta, 'phi': phi, 'type': 'spherical'})

    @staticmethod
    def cylindrical(p, phi, z):
        return type('Coordinates', (),
                    {'p': p, 'phi': phi, 'z': z, 'type': 'cylindrical'})


class Point(object):
    """Point"""
    def __init__(self, coords, color='black'):
        self.coordinates = coords
        self.color = color


class Circle(Point):
    """Circle"""
    def __init__(self, coords, radius, color='black', transparent=True):
        super(Circle, self).__init__(coords, color)
        self.radius = radius
        self.transparent = transparent


class Line(object):
    """Line"""
    def __init__(self, coords, pattern, color='green'):
        self.color = color
        self.coordinates = coords
        self.pattern = pattern


class Triangle(object):
    """Triangle"""
    points_count = 3

    def __init__(self, coords, patterns,  color='red', transparent=True):
        self.color = color
        self.transparent = transparent
        if len(coords) != self.points_count or len(coords) != len(patterns):
            raise ValueError('Bad triangle params')
        else:
            self.coordinates = coords
            self.lines = []
            for i in xrange(self.points_count - 1):
                self.lines.append(Line([coords[i], coords[i + 1]], patterns[i]))
            self.lines.append(Line([coords[-1], coords[0]], patterns[-1]))


class Rectangle(Triangle):
    """Rectangle"""
    points_count = 4
