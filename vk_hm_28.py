class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius ** 2


class SemiCircle(Circle):
    def calculate_area(self):
       return super().calculate_area()*0.5
  
semi_circle = SemiCircle(2)
print(semi_circle.calculate_area())
