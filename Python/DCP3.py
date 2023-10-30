#This problem was asked by Google;

#Given the root to a binary tree, implement serialize(root), 
#which serializes the tree into a string, and deserialize(s), 
#which deserializes the string back into the tree.
#For example, given the following Node class

#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

#The following test should pass:

#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'


class No:
    def __init__(self, raiz, esquerda = None, direita = None):
        self.raiz = raiz
        self.esquerda = esquerda
        self.direita = direita


def Serializar(arvore, separador):
    arvoreSerializado = arvore.raiz
    if arvore.esquerda != None:
        if separador == "-":
            separador2 = ";"
        else:
            separador2 = "-"
        arvoreSerializado += separador + Serializar(arvore.esquerda, separador2)
    if arvore.direita != None:
        if separador == "-":
            separador2 = ";"
        else:
            separador2 = '-'
        arvoreSerializado += separador + Serializar(arvore.direita, separador2)

    return arvoreSerializado

def Desserializar(arvoreSerializada, separador):
    partes = arvoreSerializada.split(separador)
    arvore = No(partes[0])
    try:
        if separador == "-":
            separador = ";"
        arvore.esquerda = Desserializar(partes[1], separador)
    except IndexError:
        arvore.esquerda = None

    try:
        if separador == "-":
            separador = ";"
        arvore.direita = Desserializar(partes[2], separador)
    except IndexError:
        arvore.direita = None

    return arvore


arvore = No("raiz", No("esquerda", No("esquerda.esquerda")), No("direita"))
arvoreSerializada = Serializar(arvore, '-')
arvore2 = Desserializar(arvoreSerializada, '-')

print(arvore.esquerda.esquerda.raiz == "esquerda.esquerda")

    