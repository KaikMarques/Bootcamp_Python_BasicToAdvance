# import math as m # as m é um apelido para o modulo

# from math import * Este simbolo está dizendo para importar tudo sendo o importe universal. O problema disso é que eu posso ter uma variavel com o mesmo nome de uma função e pode gerar erro

import mod_func as mf # mod_func é o nome do meu arquivo onde criei meus módulos
import numpy as np

"""
o bloco abaixo é uma instrução condicional usada para controlar o fluxo de execução do código. Ela verifica se uma variável especial interna do Python chamada
Name é igual ao valor Main, se for o bloco de código é executado se não é ignorado
O name é uma variável que tem o nome do módulo atual, quando o módulo é executado como se fosse o programa princial o valor de Name é definico como Main. QUando o módulo
é importado como estou fazendo com mod_func o valor de name é definido como nome do módulo
Serve para evitar que partes do código sejam executadas quando a gente importa o módulo
Usando essa estrutura de name e main evito que alguma função do meu módulo seja executado antes da hora.
"""

if __name__ == '__main__': # Verifica se o arquivo está sendo executado diretamente como um programa principal
    mf.mensagem()

    num = int(input("Digite um número inteiro: "))

    print(f"\nCalcular fatorial do número:")
    fat = mf.fatorial(num)
    print(f"O fatorial é {fat}")

    
    print(f"\nCalcular sequência de fibonacci:")
    fib = mf.fibo(num)
    print(f"O fatorial é {fat}")

# listas = np.array([1,2,3,4,5,6,7,8,9])
# print(listas)













