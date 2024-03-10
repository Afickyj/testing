import math


class Shape: # vytvoříme třídu a definujeme metody

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle: # vytvoříme konkrétní třídu

    def __init__(self, radius): # vytvoříme init s proměnnou radius
        self.radius = radius

    def area(self): # vytvoříme vzoreček pro výpočet obsahu kruhu
        return math.pi * (self.radius ** 2) # importujeme knihovnu math
