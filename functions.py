class PolynomialFunc:
    def __init__(self, *coefficients):
        self.coefficients = coefficients
    
    def substitute(self, x):
        result = 0

        for degree, coefficient in enumerate(self.coefficients):
            result += coefficient * x ** degree
        
        return result
    
    def differentiate(self) -> "PolynomialFunc":
        if (len(self.coefficients) == 0):
            return PolynomialFunc()

        coefficients = []

        for degree, coefficient in enumerate(self.coefficients):
            coefficients.append(degree*coefficient)

        del coefficients[0]

        return PolynomialFunc(*coefficients)


