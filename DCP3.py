#This problem was asked by Google.
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class
#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#The following test should pass:
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

import pickle
class Arvore:
    def __init__(self, raiz, esquerda, direita):
        self.raiz = raiz
        self.esquerda = esquerda
        self.direita = direita
    def mostrarArvore(self):
        print(f'{self.esquerda} <- {self.raiz} -> {self.direita}')

arvore = Arvore(5, 4, 3)
arvore.mostrarArvore()

arvore = pickle.dumps(arvore)
print(arvore)
arvore = pickle.loads(arvore)
arvore.mostrarArvore()