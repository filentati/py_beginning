'''класс для расчета площади окружности'''
class Circle:
    pi = 3.14

    def calculate_area(self, radius):
       self.radius = radius
       return self.pi*pow(radius, 2)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
 
