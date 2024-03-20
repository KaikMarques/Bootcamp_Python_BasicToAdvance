# for cont_ex in range(1,6): # vai rodar 5 vezes sendo 6 - 1. CONT_EX = contador externo
#     print(f'\nRodada: {cont_ex}')
#     for cont_in in range(5, 0, -1): # fazendo a contagem regressiva de 5 até 0 diminuindo de 1 em 1 .CONT_IN = contador interno
#         print(f"Valor: {cont_in}")

#     print("Fim dos laços")
# Obs: Primeiro entra laço da primeira condição "Rodada", porque o laço for interno vai rodas todas condições para depois sair e voltar para o laço externo e assim sucessivamente.


import random

# Nesta versão será gerado numeros aleatórios onde os mesmos podem ser repetidos
# for A in range(1, 6):
#     print(f'\nConjunto {A}')
#     for B in range(5):
#         num = random.randint(1, 100) #variavel num recebe um numero aleatório interno entre 1 e 100
#         print(f'Valor: {num}')    

# Nesta versão foi tratado o problema dos numeros aleatórios repetidos

for A in range(1, 6):  # Loop externo que itera de 1 a 5
    print(f'\nConjunto {A}')  # Imprime o número do conjunto
    numeros_gerados = []  # Cria uma lista vazia para armazenar os números gerados
    for B in range(5):  # Loop interno que itera 5 vezes
        num = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100
        while num in numeros_gerados:  # verifica se o número atual (num) já foi gerado anteriormente e está presente na lista numeros_gerados.
            num = random.randint(1, 100)  # Gera um novo número aleatório até ser único
        numeros_gerados.append(num)  # Adiciona o número gerado à lista de números gerados
        print(f'Valor: {num}')  # Imprime o valor gerado no conjunto atual


"""
Este código gera 5 conjuntos, cada um com 5 valores aleatórios únicos no intervalo de 1 a 100. O primeiro loop externo for A in range(1, 6) itera de 1 a 5 e imprime o número do conjunto.

Dentro do loop externo, criamos uma lista vazia numeros_gerados que será usada para armazenar os números gerados.

Em seguida, temos o segundo loop interno for B in range(5), que itera 5 vezes para gerar os números de cada conjunto.

Dentro do loop interno, geramos um número aleatório num usando num = random.randint(1, 100).

Para garantir que o número gerado seja único dentro do conjunto atual, usamos um loop while que verifica se o número já está na lista numeros_gerados. Se ele já existir, geramos um novo número aleatório até obtermos um número único.

Após obter um número único, adicionamos o número à lista de numeros_gerados usando numeros_gerados.append(num) e, em seguida, imprimimos o valor gerado usando print(f'Valor: {num}').

"""




