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
        return ((self.center.x - other.center.x) ** 2 + (self.center.y - other.center.y) ** 2
                ) ** 0.5 <= self.radius + other.radius

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __eq__(self, other):
        return self.square() == other.square()

    def __ne__(self, other):
        return self.square() != other.square()


sm = Circle(Point(12, 12), 425)
bg = Circle(Point(9, 1), 10293.4)
print(
    sm > bg,
    sm == sm,
    sm != bg,
    sm == bg

)
