# Dicionário permite armazenar sequências de dados em pares chave e valor. 
# Não pode ter chaves repetidas. Elas são imutáveis
# Posso usar string, valor número e até mesmo tuplas com chaves más não itens que sejam mutáveis como por exemplo listas como chave dentro do dicionário

elemento = {
    'z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f'Elemento: {elemento['nome']}') # Utilizo a notação de colchetes que já usei para listas e tuplas, ao invés de colocar o número de posição, vou colocar o nome da chave que tem o valor associado
print(f'Densidade: {elemento['densidade']}')

# Consultando o tamanho do dicionário
print(f'O dicionário possui {len(elemento)} elementos.')

# Atualizar uma entrada
elemento['grupo'] = 'Alcalinos'
print(elemento)

# Adicionar uma entrada
elemento['periodo'] = 1
print(elemento)

# Exclusão de itens em dicionários
# del elemento['periodo']
# print(elemento)

# elemento.clear() # removendo todo o conteúdo do diionário, porém ele continua existindo
# print(elemento)

# del elemento # Excluindo meu dicionário da memória
# print(elemento) # vai apresentar erro


print(elemento.items()) # Esse método me retorna da lista e cada item está dentro de uma tupla indicado pelo parênteses
for i in elemento.items(): # Com o for, organizo cada tupla uma em cada linha para ficar mais facil de acessar
    print(i)

print(elemento.keys()) # Esse método me retorna a lista com os nomes das chaves
for i in elemento.keys():
    print(i)

print(elemento.values()) # Esse método me retorna a lista com os nomes daos valores
for i in elemento.values():
    print(i)

for i, j in elemento.items(): # Imprime uma chave e valor em cada linha
    print(f'{i}: {j}')

















