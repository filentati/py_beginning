class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
       return self.a*self.b


class Square(Rectangle):
    def __init__(self, a):
       super().__init__(a, a)


class CalculatePerimeterMixin(Rectangle):
    def calculate_perimeter(self):
       return 2*(self.a+self.b)


class SquareWithMixin(CalculatePerimeterMixin, Square):
    def __eq__(self, other):
       return self.a == other.a

    def __gt__(self, other):
       return self.calculate_area() > other.calculate_area()

    def __add__(self, other):
       return self.calculate_area() + other.calculate_area()


square_with_mixin1 = SquareWithMixin(3)
square_with_mixin2 = SquareWithMixin(2)
print(square_with_mixin1.calculate_area())
print(square_with_mixin1.calculate_perimeter())
print(square_with_mixin1 == square_with_mixin1)
print(square_with_mixin1 == square_with_mixin2)
print(square_with_mixin1 > square_with_mixin2)
print(square_with_mixin1 > square_with_mixin1)
print(square_with_mixin1 + square_with_mixin1)
