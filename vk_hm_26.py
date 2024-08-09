class Person:
    def __init__(self, age = 0):
       self._age = age

    @property
    def age(self):
       return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0
        else:
            self._age = value
    

person = Person()
person.age = 19
print(person.age)
