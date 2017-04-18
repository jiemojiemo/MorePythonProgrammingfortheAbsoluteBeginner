class Point():
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("Point constructor")

    def ToString(self):
        return "{X:" +  str(self.x) + ",Y:" + str(self.y) + "}"

class Circle(Point):
    radius = 0.0

    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        print("Circle constructor")

    def CalcCircum(self):
        PI = 3.14159
        return 2*PI*self.radius;

    def ToString(self):
        return super().ToString() + ",{RADIUS=" + str(self.radius) + "}"

class Size():
    width = 0.0
    height = 0.0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        print("Size constructor")

    def ToString(self):
        return "{WIDTH=" + str(self.width) + ",HEIGHT=" + str(self.height) + "}"

class Rectangle(Point, Size):
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)
        print("Rectangle constructor")


    def CalcArea(self):
        return self.width * self.height

    def ToString(self):
        return Point.ToString(self) + "," + Size.ToString(self)

class Ellipse(Point):
    # Horizontal radius
    h_radius = 0.0
    # Vetical radius
    v_radius = 0.0

    def __init__(self, x, y, h_r, v_r):
        Point.__init__(self, x, y)
        self.h_radius = h_r
        self.v_radius = v_r

    def ToString(self):
        return Point.ToString(self) + "{HORIZAONTAL RADIUS=" + str(self.h_radius) + \
                ",VERTICAL RADIUS=" + str(self.v_radius) + "}"


p = Point(10, 20)
print(p.ToString())

c = Circle(100, 100, 50)
print(c.ToString())
print(c.CalcCircum())

s = Size(80, 70)
print(s.ToString())

r = Rectangle(200, 250, 40, 50)
print(r.ToString())
print(r.CalcArea())

e = Ellipse(0,0,50,80)
print(e.ToString())
