class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return ((self.x - p2.x)**2 + (self.y-p2.y)**2)**0.5


class Circle:
    def __init__(self, parameter_list):
        pass

    pass

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
print(p1.dist(p2) == 1)

pass
