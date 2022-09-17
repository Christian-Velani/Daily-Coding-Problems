#This problem was asked by Airbnb.
#Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

numeros = [5, 1, 1, 5]
lista_somas = []
lista_controle = []

for indice1 in range(len(numeros)): #indice utilizado para primeira passada na lista
    for indice2 in range(len(numeros)): #indice utilizado para segunda passada na lista
        if indice2 > indice1 + 1: #verificação se a soma pode ser feita
            lista_somas.append(numeros[indice1] + numeros[indice2]) #adiciona a soma na lista de somas
            lista_controle.append([indice1, indice2]) #adiciona na lista de controle os indices utilizados para a soma

for n in range(len(numeros)): #nova passagem na lista para procurar novas somas
    for n2 in range(len(lista_somas)): #passagem na lista de somas
        if n > lista_controle[n2][-1] + 1: #verificação se o numero pode ser somado
            lista_somas[n2] += numeros[n] #aumenta o valor da soma
            lista_controle[n2].append(n) #adiciona o indice extra o qual foi utilizado para gerar o novo valor da soma
            
print(max(lista_somas))