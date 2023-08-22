#This problem was recently asked by Google.

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?

lista_numeros = [19, 11, 2 ,20]
k = 13

def verifica_soma(lista, k):
    for n in lista:
        if k - n in lista:
            return print("Existe dois valores na lista que somados chegam em k")
    return print("Não existe soma que chegue em k")

verifica_soma(lista_numeros, k)