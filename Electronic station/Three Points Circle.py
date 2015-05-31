import re


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, pa=Point(), pb=Point()):
        self.pa = pa
        self.pb = pb

    def intersection(self, line):
        ret = self.pa

        t = float((self.pa.x - line.pa.x) * (line.pb.y - line.pa.y) - (self.pa.y - line.pa.y) * (line.pb.x - line.pa.x)) \
            / ((self.pa.x - self.pb.x) * (line.pb.y - line.pa.y) - (self.pa.y - self.pb.y) * (line.pb.x - line.pa.x))
        ret.x += (self.pb.x - self.pa.x) * t
        ret.y += (self.pb.y - self.pa.y) * t

        return ret


def checkio_complex(data):
    p = a, b, c = eval(data.replace("(", "complex("))
    q = h, i, g = [p[i - 2].conjugate() * (p[i - 1] - p[i]) for i in range(3)]
    s = (a * g + b * h + c * i) / sum(q)
    return "(x-{})^2+(y-{})^2={}^2".format(*((format(t, ".{}g".format(3 - (t < 1)))
                                              for t in (s.real, s.imag, abs(s - a)))))


def checkio(data):
    xys = map(int, re.findall(r'\d+', data))
    a = Point(xys[0], xys[1])
    b = Point(xys[2], xys[3])
    c = Point(xys[4], xys[5])
    la = Line()
    la.pa = Point(float(a.x + b.x) / 2, float(a.y + b.y) / 2)
    la.pb = Point(la.pa.x + (la.pa.y - a.y), la.pa.y - (la.pa.x - a.x))
    lb = Line()
    lb.pa = Point(float(a.x + c.x) / 2, float(a.y + c.y) / 2)
    lb.pb = Point(lb.pa.x + (lb.pa.y - a.y), lb.pa.y - (lb.pa.x - a.x))
    ip = la.intersection(lb)
    r = float((ip.x - a.x) ** 2 + (ip.y - a.y) ** 2) ** 0.5
    return "(x-%.3g)^2+(y-%.3g)^2=%.3g^2" % (ip.x, ip.y, round(r, 2))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
