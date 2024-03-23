# Sequências são estruturas de dados que permitem armazenar vários dados de uma vez dentro de uma única variável na memória
# Outras listas que existem: Tuplas, Dicionários ou conjunto de sets
# Listas: representa uma sequência de valores, e os itens da lista são acessados pelo número do indice que começa em 0
# Listas podem ser concatenadas

# Sintaxe: nome_lista = [valores]

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,4]
valores = n1 + n2 # concatenado listas
valores[0] = 9 # Alterando o valor pelo indice
# print(valores[0:2]) # imprimindo valores começando pelo indice 0 e dizendo a quantidade que quero imprimir que será 2 valores sendo 9 e 6
# print(valores[3:3]) # me retornaria um vazio porque são números iguais, tem que ser diferente os números sendo o valor até menos 1 ou +1


# print(len(valores))# verificando quantos elementos existe na lista
# print(sorted(valores))# retorna uma versão ordenada da lista em ordem crescente
# print(sorted(valores, reverse=True))# retorna uma versão ordenada da lista em ordem decrescente
# print(sum(valores)) # para ver a somatória dos valores da lista
# print(min(valores)) # verifica o menor valor da lista
# print(max(valores)) # verifica o maior valor da lista

# valores.append(13) # acresta o valor 13 ao final da lista
# valores.pop() # remove o ultimo valor da lista
# valores.pop(3) # remove o valor da posição 3
# valores.insert(3, 21) # no indice 3 adiciona o número 21. Esse método adiciono o número pelo indice
# print(12 in valores) # estou fazendo uma pergunta: 12 está em valores, sim ou não? vai me retornar True ou False


# planetas = ['Mercúrio', 'Vénus', 'Marte', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas: # planeta é minha variável de iteração e planetas é minha lista
#     print(planeta)


""" _________________ Exercicio ____________________
 Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
  Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repetição for.
"""


# script que armazena 5 bebidas digitadas pelo usuário
bebidas = []

for i in range(5):
    bebida = input(f'Digite uma bebida favorita: ')
    bebidas.append(bebida)

bebidas.sort() # este método classifica e ordena o conteudo da lista automáticamente.

# script que imprime as bebidas digitadas
print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'\nSaúde! ')