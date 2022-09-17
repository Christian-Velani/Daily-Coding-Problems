#This problem was asked by Facebook.
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

mensagem = '6457515676521328765165'

if mensagem[0] != '0':
    if '0' not in mensagem:
        numero_solucoes = 1
    else:
        numero_solucoes = 0
    lista_duplas = []
    for c in range(len(mensagem) - 1):
        if mensagem[c] != '0' and int(mensagem[c] + mensagem[c+1]) <= 26:
            lista_duplas.append(mensagem[c] + mensagem[c+1])
    numero_solucoes += len(lista_duplas)
    multiplicador = 2
    auxiliar = 1
for i in range(len(lista_duplas)):
    print(f'i: {i}')
    o = i + 1
    print(f'o: {o}')
    fator = len(lista_duplas) - o - 1
    print(f'fator: {fator}')
    if fator >= 0:
        if i == 0 or i == 1:
            numero_solucoes += fator
            print(f'solucoes: {numero_solucoes}')
        else:
            numero_solucoes += fator * multiplicador
            print(f'solucoes: {numero_solucoes}')
            auxiliar, multiplicador = multiplicador, multiplicador + auxiliar
            print(f'auxiliar: {auxiliar}, multiplicador: {multiplicador}')

print(numero_solucoes)
print(lista_duplas)
