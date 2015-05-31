__author__ = 'snowwolf'

import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = float(x)
        self.y = float(y)

    def point_distance(self, p):
        return math.sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)


class Segment:
    def __init__(self, pa=Point(), pb=Point()):
        self.pa = pa
        self.pb = pb

    def point_distance(self, p):
        cross = (self.pb.x - self.pa.x) * (p.x - self.pa.x) + (self.pb.y - self.pa.y) * (p.y - self.pa.y)
        if cross < 0:
            return p.point_distance(self.pa)

        d = (self.pa.x - self.pb.x) ** 2 + (self.pa.y - self.pb.y) ** 2
        if cross > d:
            return p.point_distance(self.pb)

        r = cross / d
        pc = Point(self.pa.x + (self.pb.x - self.pa.x) * r, self.pa.y + (self.pb.y - self.pa.y) * r)
        return p.point_distance(pc)

if __name__ == '__main__':
    s = Segment(Point(0, 0), Point(1, 1))
    p = Point(1, 0)
    print s.point_distance(p)