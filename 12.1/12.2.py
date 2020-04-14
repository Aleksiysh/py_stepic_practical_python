class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return ((self.x - p2.x)**2 + (self.y-p2.y)**2)**0.5


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def square(self):
        return 3.14 * self.radius ** 2

    def do_intersect(self, other):
        return ((self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2) ** 0.5 <= self.radius + other.radius


circ = Circle(Point(0, 3), 4)
circ.radius == 4
circ.center.x == 0
print(
    Circle(Point(0, 0), 0).square() == 0,
    circ.center.x
)
