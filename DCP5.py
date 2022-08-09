#This problem was asked by Jane Street.
#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#Given this implementation of cons:
#def cons(a, b):
#    def pair(f):
#        return f(a, b)
#    return pair
#Implement car and cdr.

def cons(a, b):
    def par(f):
        return f(a,b)
    return par

def esquerda(c):
    def esq(a,b):
        return a
    return c(esq)

def direita(d):
    def dir(a,b):
        return b
    return d(dir)

print(esquerda(cons(5,6)))
print(direita(cons(5,6)))
