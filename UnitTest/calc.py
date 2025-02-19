class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_add(self):
        return self.a + self.b
    
    def do_minus(self):
        return self.a - self.b
    
    def do_multiply(self):
        return self.a * self.b
    
    def do_division(self):
        return self.a / self.b