#This problem was asked by Facebook.
#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#You can assume that the messages are decodable. For example, '001' is not allowed.

mensagem = '111'
if mensagem[0] != '0':
    possibilidades = 1
    for i in range(len(mensagem) - 1):
        if int(mensagem[i] + mensagem[i+1]) <=26:
            possibilidades += 1
else:
    possibilidades = 0
print(possibilidades)