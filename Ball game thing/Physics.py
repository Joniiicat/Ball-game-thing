import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mag(self):
        return math.sqrt(self.x**2 + self.y**2)

    def hat(self):
        x = self.x / self.mag()
        y = self.y / self.mag()
        return Vector2(x, y)