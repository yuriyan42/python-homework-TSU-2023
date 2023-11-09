class Number:
############initialization############
    def __init__(self, value = 0, system = 'DEC'):
            def TEST(val, sysch :set = 0, sys = 'DEC'):
                if sys == 'DEC':
                    try:
                        number = int(val)
                    except ValueError:
                        print('Your input is incorrect. Try again or change the system')
                else:
                    try:
                        for i in set(str(val)):
                            if i not in sysch:
                                raise ValueError
                            number = str(val)
                    except ValueError:
                        print('Your input is incorrect. Try again or change the system')
                return number
                    
            match system:
                case 'DEC':
                    self._dec = TEST(value)
                case 'BIN':
                    self._dec = int(TEST(value, {'0', '1'}, 'BIN'), base = 2)
                case 'HEX':
                    self._dec = int(TEST(value, {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}, 'HEX'), base = 16)
                case 'ROM':
                    ROM_num = TEST(value, {'I', 'V', 'X', 'L', 'C', 'D', 'M'}, 'ROM')
                    romch = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
                    d_number = 0
                    for i, j in romch:
                        while ROM_num.startswith(j):
                            d_number += i
                            ROM_num = ROM_num[len(j):]
                        self._dec = d_number
#############################################

############arithmetic operations############
    def __add__(self, other):
        result = Number()
        result._dec = self._dec + other._dec
        return result
    
    def __sub__(self, other):
        result = Number()
        result._dec = self._dec - other._dec
        return result
    
    def __mul__(self, other):
        result = Number()
        result._dec = self._dec * other._dec
        return result
    
    def __truediv__(self, other):
        result = Number()
        result._dec = self._dec / other._dec
        return result
#############################################

##################properties#################   
    @property
    def dec(self):
        """decimal system representation"""
        return self._dec
    
    @property
    def bin(self):
        """binary system representation"""
        return bin(self._dec)
    
    @property
    def hex(self):
        """hexadecimal system representation"""
        return hex(self._dec)
    
    @property
    def roman(self):
        """roman system representation"""
        romch = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        num  = self._dec
        r_number = ''
        while num > 0:
            for i, j in romch:
                while num >= i:
                    r_number += j
                    num -= i
        return r_number



##################CHECK#################
n = Number(401)
n = n + Number(100)

print(n.dec)
print(n.bin)
print(n.hex)
print(n.roman)

b = Number('DI', 'ROM')
c = Number('1f5', 'HEX')

d = n + b + c

print(d.dec)