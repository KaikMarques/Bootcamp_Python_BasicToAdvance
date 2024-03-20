# Trabalhando com números aleatórios

import random

# valor = random.randint(1, 20) # gera um num aleatorio entre 1 e 20 
# print(valor)

# gerando vários num aleatorios tipo int
# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5): # vai rodar 5 vezes o laço for
#     n = random.randint(1, 50) # gerando numeros aleatórios inteiro do 1 ao 50
#     print(f'O número gerado: {n}') # imprimindo o numero cada vez que cair nessa condição que será 5 vezes

# Usando  random para numeros aleatórios float
# valor = random.random()
# print(f'Número gerado: {round(valor * 10, 2)}') # trabalhando com ponto flutuante (float) entre 0 e 10. Round para arredondar e 2 para a quantidade de casas decimais

# valor = random.uniform(1, 100)
# print(f'Número: {round(valor, 3)}')

# Criando uma lista de valores previamente criada e gerar selecionar/sortear um num apartir da lista
L = [2,3,4,5,6,7,8,12,23,55,67,74]
# for _ in range(5): #No Python, é comum utilizar o _ como variável de iteração quando não é necessário utilizar o valor dessa variável em si. Nesse caso, estamos utilizando o _ para ignorar o valor da iteração.
#     n = random.choice(L)
#     print(f'Número escolhido: {n}')

# Extraindo vários valores ao mesmo tempo da lista usando o método SAMPLE
# n = random.sample(L, 3) # n vai receber a lista com 3 itens da minha lista L
# print(f'Número extraidos: {n}')

# Embaralhando os elementos da sequencia da lista
print(f'Exibir a lista original: \n{L}')
print('Embaralhar a lista e exibi-la:')
n = random.shuffle(L)
print(L)



