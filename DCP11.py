#This problem was asked by Twitter.
#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
#Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

dicionario = {'a': ['ação', 'acordado', 'afável','amizade', 'amor', 'atividade', 'aurora', 'autêntico'],
              'b': ['bagunceiro', 'barragem', 'batom', 'berinjela', 'bidimensional', 'biosfera', 'blitz', 'blusa'],
              'c': ['cafajeste', 'cauteloso', 'cavalheiro', 'censo', 'compassivo', 'conciso', 'conservador', 'correto'],
              'd': ['decompor', 'decreto', 'desembarque', 'deserto', 'desgastar', 'deslocamento', 'desordem', 'despretensioso'],
             }
respostas = []
inicio_palavra = input().lower()

for palavra in dicionario[inicio_palavra[0]]:
    if inicio_palavra in palavra:
        respostas.append(palavra)
        
print(', '.join(respostas))