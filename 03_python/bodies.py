import math

class Sphere:
    """A simple sphere."""

    def __init__(self, pos, radius = 1):
        self.pos = tuple(pos)
        self.radius = float(radius)

    def volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def translate(self, t):
        self.pos = tuple(xi + ti for xi, ti in zip(self.pos, t))

class Planet(Sphere):
    """A simple planet."""

    def __init__(self, name, pos, mass, radius):
        self.name = str(name)
        self.pos = tuple(pos)
        self.mass = float(mass)
        self.radius = float(radius)

    def density(self):
        """Compute density of the planet"""
        return self.mass / self.volume()
