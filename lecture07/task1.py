class Dual:
    """
        Dual numbers class
    """
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        result = Dual(None, None)
        result.a = self.a + other.a
        result.b = self.b + other.b
        return result
    
    def __sub__(self, other):
        result = Dual(None, None)
        result.a = self.a - other.a
        result.b = self.b - other.b
        return result
    
    def __mul__(self, other):
        result = Dual(None, None)
        result.a = self.a * other.a
        result.b = self.a * other.b + other.a * self.b
        return result
    
    def __truediv__(self, other):
        result = Dual(None, None)
        result.a = self.a / other.a
        result.b = (self.a * other.b - other.a * self.b) / other.a**2
        return result
    
    def root(self, n = 2):
        result = Dual(None, None)
        result.a = self.a ** (1/n)
        result.b = self.b / (n * self.a ** ((n - 1) / n))
        return result
    
##CHECK##
A = Dual(2,3)
B = Dual(4,5)
C = A + B
D = A - B
E = A * B
F = A / B
G = B.root()
print(C.a, C.b)
print(D.a, D.b)
print(E.a, E.b)
print(F.a, F.b)
print(G.a, G.b)
