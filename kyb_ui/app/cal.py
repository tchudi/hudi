# Calculator.py
class calculator(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return (self.a + self.b)
    def minus(self):
        return (self.a - self.b)
    def multip(self):
        return (self.a * self.b)
    def divide(self):
        return (self.a / self.b)