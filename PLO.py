class square():
    def __init__(self, a):
        self.a = a
    def p(self):
        return (self.a ** 2)
    
    
    
class round():
    def __init__(self, r):
        self.r = r
    def p(self):
        return (3.14 * self.r * self.r)
    
    
    
    
class rect():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def p(self):
        return (self.a * self.b)
    
    
    
sq = square(5)
ro = round(2)
re = rect(4, 2)
pl = [sq, ro, re]
for i in pl:
    print(i.p())






