
class Mycalculator(object):
    
    def __init__(self):
        pass

    def add(self, n1, n2):
        return n1 + n2

    def subs(self, n1, n2):
        return n1-n2

    def mult(self, n1, n2):
        return n1*n2

    def div(self, n1, n2):
        return n1/n2


if __name__ == '__main__':
    calc = Mycalculator()
    print("Done:", calc.mult(0.1,0.2))

