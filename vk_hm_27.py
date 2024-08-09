class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length):
        return 2*cls.pi*pow((length/cls.g), 0.5)

print(Pendulum.calculate_period(10))
