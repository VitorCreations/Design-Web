class Equação2:

    def __init__(self,a,b,c):
        self.__a = 0
        self.__b = 0
        self.__c = 0
        self.set_a(a)
        self.set_b(b)
        self.set_c(c)

        def set_a(self,x):
            if x >=0: self.__a = x
            else:
                raise ValueError
        def set_b(self,x):
            if x >=0: self.__b = x
            else:
                raise ValueError
        def set_c(self,x):
            if x >=0: self.__c = x
            else:
                raise ValueError

        def get_a(self):
            return self.__a
        def get_b(self):
            return self.__b
        def get_c(self):
            return self.__c

        def calc_delta(self):
            return self.__b ** 2 * (-4) * self.__a * self.__c
        
        def TemRaizesReais(self):
            if self.calc_delta >=1: return "Possui Raizes Reais"
            else:
                return "Não possui Raizes Reais"