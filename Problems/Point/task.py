from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, pt2):
        return sqrt(((self.x - pt2.x) ** 2) + ((self.y - pt2.y) ** 2))
