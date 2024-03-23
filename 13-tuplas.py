# Tuplas são parecidos com listas. Elas permitem que tenha vários dados armazenados dentro da mesma estrutura e que
# os dados sejam acessados por meio de números/índices. Elas aceitam qualquer tipo de dado.

# Elas são imutáveis comparado com a lista. Os valores não podem ser alterados

# tupla = (2,4,6,7,9)
# tupla[1] = 5# atribuindo o valor 5 na posição 1. Vai apresentar erro porque tupla é imutavel

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres # concatenando as tuplas
t1 = (1,2,4,3,5,5,2,3,2,5,6,7,8,6,6,8,9)
# print(t1.count(5)) # conta quantos numeros 5 tem na tupla
# print(halogenios[-1]) # imprimindo o conteudo do indice 3 sendo I
print('Cl' in halogenios) # Operador In para verificar se algo está presente. Cl está presente em halogenio?

# Posso usar na tuplas:
print(sum(t1))
print(min(t1))
print(max(t1))

# Operações não disponivel na tupla
# .sort(), .append(), .reverse(), .pop()

# Condição FOR com tuplas
# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')


# Criando uma lista apartir de uma tupla
# grupo17 = list(halogenios)
# grupo17[0] = 'H' # Como agora é uma lista consigo alterar
# print(grupo17)


# Criando uma tupla apartir da lista
# grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
# alcalinos = tuple(grupo1)
# alcalinos[0] = 'H' # Como agora é uma tupla não consigo alterar
# print(alcalinos)

# Ordenando os elementos de uma tupla
# A unica forma é criando uma nova tupla, com os elementos da tupla classificados usando a função sorted
# print(sorted(alcalinos))



